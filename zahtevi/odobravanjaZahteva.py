'''
Created on Jul 2, 2016

@author: Vasic
'''
from ucitati.ucitavanjeZahtevaZaRobu import zahteviZaTransport
from ucitati.entitete import avioni, prostori
from sacuvati.entitete import sacuvatiProstorZaTeret
from glavni.main import prostorTxt



def odobravanjeZahtevaZaTransport():
    listaAvionaZaRelaciju = []
    
    formatiranjeZahteva("kreiran")
    unos = input("Uneti redni broj zahteva za obradu >> ")
    
    for zahtev1 in zahteviZaTransport:
        if zahtev1.identifikacioniKodZahteva == unos:
            zahtev = zahtev1
            
            
    for avion in avioni:
        try:
            if avion.relacija == zahtev.odrediste and avion.hangar is not None:
                listaAvionaZaRelaciju.append(avion)
        except UnboundLocalError:
            print("Pogresan izbor")
            odobravanjeZahtevaZaTransport()
            
    zapreminaRobe = ukupnaZapreminaRobe(zahtev.listaRobe)
    for avion in listaAvionaZaRelaciju:
        print(avion.naziv)
    
    prostor = izborAviona(listaAvionaZaRelaciju, zahtev, zapreminaRobe)
    
    prostor.zapremina -= zapreminaRobe
    
    sacuvatiProstorZaTeret(prostorTxt, prostori)
    
    zahtev.statusZahteva = "odobren"
    zahtev.avion = avion
    for r in zahtev.listaRobe:
        r.prostorZaTeret = prostor
    
    
    izbor123 = input("Zelite li da odobrite jos neki zahtev? ")
    if izbor123 == "y":
        odobravanjeZahtevaZaTransport()

    
    




def izborAviona(listaAviona, zahtev, zapreminaRobe):
    formatiranjeAviona(listaAviona)
    izbor = input("Uneti oznaku aviona >> ")
    for avion1 in listaAviona:
        if izbor == avion1.oznaka:
            avion = avion1

    
    
    maxVisina = maksVisina(zahtev.listaRobe)
    maxSirina = maksSirina(zahtev.listaRobe)
    maxDuzina = maksDuzina(zahtev.listaRobe)
    try:
        provera = mozeBarUJedan(avion,maxDuzina, maxSirina, maxVisina, zapreminaRobe)
    except UnboundLocalError:
        print("Pogresan avion")
        odobravanjeZahtevaZaTransport()
    if provera is False:
        print("Roba ne moze da stane ni u jedan od aviona!")
        from korisnici.menadzerTransporta import ulogaMenadzeraTransporta
        ulogaMenadzeraTransporta()
        #return izborAviona(listaAviona, zahtev, zapreminaRobe)    
    
    
    prostor = izborProstora(avion,zapreminaRobe, maxDuzina, maxSirina, maxVisina)
    while prostor is False:
        prostor = izborProstora(avion, zapreminaRobe, maxDuzina, maxSirina, maxVisina) 
        
    
    return prostor
        
    
        
        
        
        
def izborProstora(avion, zapreminaRobe, duzina, sirina, visina):
    formatiranjeProstora(avion)
    izbor = input("Izabrati prostor za teret >> ")
    for prostor in prostori:
        if avion.oznaka == prostor.avion.oznaka:
            if izbor == prostor.oznaka:
                if prostor.duzina > duzina and prostor.sirina > sirina and prostor.visina and prostor.zapremina > zapreminaRobe:
                    return prostor
                
    
    return False
    
    


def mozeBarUJedan(avion,duzina, sirina, visina, zapreminaRobe):
    lista = []
    prostoriAvion1 = prostoriAvion(avion)
    for prostor in prostoriAvion1:
        if prostor.visina > visina and prostor.duzina > duzina and prostor.sirina > sirina and prostor.zapremina > zapreminaRobe:
            lista.append(prostor)
    
    if len(lista) > 0:
        return True
    else:
        return False   
    


def prostoriAvion(avion):
    prostoriii = []
    for prostor in prostori:
        if prostor.avion.oznaka == avion.oznaka:
            prostoriii.append(prostor)
    return prostoriii

            

    
    
def ukupnaZapreminaRobe(roba):
    zapremina = 0
    for r in roba:
        zapremina1 = r.duzina * r.sirina * r.visina
        zapremina += zapremina1
        
    return zapremina


def maksVisina(roba):
    maks = []
    for r in roba:
        maks.append(r.visina)
    
    maks1 = max(maks)
    return maks1    
    
    
def maksDuzina(roba):
    maks = []
    for r in roba:
        maks.append(r.duzina)
    
    maks1 = max(maks)
    return maks1    
    
    
def maksSirina(roba):
    maks = []
    for r in roba:
        maks.append(r.sirina)
    
    maks1 = max(maks)
    return maks1    


def formatiranjeZahteva(status):
    zahteviHeader()
    for zahtev in zahteviZaTransport:
        if zahtev.statusZahteva == status:
            if zahtev.avion is None:
                oznaka = " / "
            else:
                oznaka = zahtev.avion.oznaka
            print("{0:14}|{1:17}|{2:24}|{3:16}|{4:19}|{5:13}|{6:11}".format(zahtev.identifikacioniKodZahteva,zahtev.datumKreiranjaZahteva,zahtev.datumTransportovanjaRobe,zahtev.odrediste,zahtev.identifikacioniKodPotrazitelja,oznaka,zahtev.statusZahteva))
            print("") 
            
            
def formatiranjeAviona(listaAviona):
    avionHeader()
    for avion in listaAviona:
        print("{0:12}|{1:11}|{2:12}|{3:16}|{4:12}|".format(avion.oznaka,avion.naziv, avion.godiste, avion.rasponKrila, avion.ukupnaNosivost)) 


def formatiranjeProstora(avion):
    prostorHeader()
    for prostor in prostori:
        if prostor.avion.oznaka == avion.oznaka:
            print("{0:9}|{1:10}|{2:10}|{3:10}|{4:13}|{5:9}|".format(prostor.oznaka,round(prostor.sirina, 2),round(prostor.duzina, 2), round(prostor.visina, 2), round(prostor.zapremina, 2),prostor.avion.oznaka))
            

def avionHeader():
    print("\n")
    print(
      "   Oznaka   |    Naziv  |   Godiste  |  Raspon krila  |  Nosivost  |\n" 
      "------------+-----------+------------+----------------+------------+")  



def zahteviHeader():
    print("\n")
    print(
      "ID kod zahteva| Datum Kreiranja | Datum Transportovanja  |    Odrediste   |ID kod Potrazitelja|Oznaka aviona|  Status  |\n" 
      "--------------+-----------------+------------------------+----------------+-------------------+-------------+----------")  

def prostorHeader():
    print("\n")
    print(
          "  Oznaka |  sirina  |  duzina  |  visina  |  zapremina  |  avion  |\n"
          "---------+----------+----------+----------+-------------+---------+"
          )