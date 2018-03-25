'''
Created on Jun 3, 2016

@author: Lazar-PC
'''
#from ucitati.korisnike import listaPotrazitelja
#from datum.datum_vreme import parsirajDatum
import time
from objekti.entiteti import Roba
from ucitati import entitete
from objekti.entiteti import ucitajDuzinu, ucitajSirinu, ucitajVisinu
from zahtevi.ZahtevZaTransport import ZahtevZaTransport

from ucitati.entitete import roba
from ucitati.ucitavanjeZahtevaZaRobu import zahteviZaTransport
from ucitati.robu import ucitavanjeRobe
from glavni.main import cisti



#from glavni import vrednosti
#from glavni.vrednosti import ulogovan

relacije = []
robaPotrazitelj = []

def potraziteljUloga():
    from glavni.vrednosti import logovanjePotrazitelji
    print("Uloga korisnika sistema: Potrazitelj")
    print("[1]- nova usluga")
    print("[2]- pregled svih transporta robe")
    print("[0]- izlaz")

    unos=str(input("unesi broj: "))
    if unos == "1":
        cisti()
        novaUsluga()
        potraziteljUloga()
    elif unos =="2":
        cisti()
        pregledUsluga()
        potraziteljUloga()
    elif unos=="0":
        cisti()
        print("izlaz")
        logovanjePotrazitelji()
    else:
        print("-------------")
        print("pogresan unos")
        print("-------------")
    potraziteljUloga()

def izborRelacije():
    relacije.clear()
    for avion in entitete.avioni:
        if avion.hangar is not None:
            if avion.relacija not in relacije:
                relacije.append(avion.relacija)
    for relacija1 in relacije:
        print(relacija1)
    
    izbor = input("Uneti tacan naziv relacije >> ")
    
    for relacija1 in relacije:
        if izbor == relacija1:
            relacija = relacija1
        
    return relacija
            
            
    

relacijeAvioni = []
def pregledUsluga():
    cisti()
    from glavni.main import robaTxt
    from glavni.vrednosti import ulogovan
    entitete.roba.clear()
    for ulogovani in ulogovan:
        a=ulogovani.identifikacioniKod
    print("ID kod:  ",a)
    ulaz=a
    ucitavanjeRobe(robaTxt)
    formatheader()
    for roba in entitete.roba:
        roba1=roba.identifikacioniKodPotrazitelja
        if ulaz==roba1:
            print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
      
    entitete.roba.clear()
    potraziteljUloga()   
def novaUsluga():
    """Kreiranje novog zahteva za transport"""
    identifikacioniKod = str(len(zahteviZaTransport))
    #Datume treba srediti
    datumKreiranjaZahteva = time.strftime("%d/%m/%Y")
    datumTransportovanjaRobe = "None"
    
    odrediste = izborRelacije()
    
    
    from glavni.vrednosti import ulogovan
    for u in ulogovan:
        identifikacioniKodPotrazitelja = u.identifikacioniKod
    oznakaAviona = None
    statusZahteva = "kreiran"
    dodavanjeRobe()
    listaRobe = robaPotrazitelj
    z = ZahtevZaTransport(identifikacioniKod, datumKreiranjaZahteva,
                      datumTransportovanjaRobe, odrediste,
                      identifikacioniKodPotrazitelja, oznakaAviona,
                      listaRobe, statusZahteva)   
    zahteviZaTransport.append(z)
    
          
def dodavanjeRobe():
    """Ciscenje liste u kojoj se nalazi roba za trenutni zahtev i dodavanje robe"""
    robaPotrazitelj.clear()
    dodavanjeRobe1()
    
def dodavanjeRobe1():
    oznaka = str(len(entitete.roba))
    naziv = input("Uneti naziv robe>> ")
    opis = input("Uneti opis robe>> ")
    tezinaRobe = ucitajTezinu()
    from glavni.vrednosti import ulogovan
    for u in ulogovan:
        identifikacioniKodPotrazitelja = u.identifikacioniKod
    prostorZaTeret = None
    duzina = ucitajDuzinu()
    sirina = ucitajSirinu()
    visina = ucitajVisinu()
    r = Roba(oznaka, naziv, opis, tezinaRobe, identifikacioniKodPotrazitelja,
             prostorZaTeret, duzina, sirina, visina)
    
    entitete.roba.append(r)
    robaPotrazitelj.append(r)
    print(robaPotrazitelj)
    izbor = input("Zelite li da dodate jos robe? (y/n)")
    if izbor == "y":
        dodavanjeRobe1()
    else:
        print("Hvala!")
def ucitajTezinu():
    duzina1 = input("Uneti tezinu>> ")                  
    try:                                            
        duzina = float(duzina1)
        return duzina
    except:
        print("Tezina mora biti float!")
        return ucitajTezinu()       


def pretragaRobe():
    
    """ Pretraga robe, menadzer transporta moze da pretrazuje robu
        po sledecim atributima Oznaci, Nazivu, Opisu, Sirini, Duzini
        Visini, Tezini i ID kodu , nakon pretrage, korisnik ostaje u 
        funkciji pretraga robe sve dok ne izadje """
    
    from korisnici.menadzerTransporta import ulogaMenadzeraTransporta
    print("[1]-prikazi robu")
    print("[2]-pretraga po Oznaci")
    print("[3]-pretraga po Nazivu")
    print("[4]-pretraga po Opisu")
    print("[5]-pretraga po Sirini")
    print("[6]-pretraga po Duzini")
    print("[7]-pretraga po Visini")
    print("[8]-pretraga po Tezini robe")
    print("[9]-pretraga po ID kodu")
    print("[0]-Izlaz")
    unos=str(input("izbor: "))
    if unos=="1": 
        cisti()  
        formatheader()
        for roba in entitete.roba: 
            print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("") 
        pretragaRobe()        
    elif unos=="2":
        cisti()
        ulaz=input("unesite Oznaci: ")
        formatheader()
        for roba in entitete.roba:
            roba1=roba.oznaka
            if ulaz==roba1:
                print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("")
        pretragaRobe()
    elif unos=="3":
        cisti()
        ulaz=input("unesite Naziv: ")
        formatheader()
        for roba in entitete.roba:
            roba1=roba.naziv
            if ulaz==roba1:
                print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("")
        pretragaRobe()
    elif unos=="4":
        cisti()
        ulaz=input("unesite Opis: ")
        formatheader()
        for roba in entitete.roba:
            roba1=roba.opis
            if ulaz==roba1:
                print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("")
        pretragaRobe()
    elif unos=="5":
        cisti()
        ulaz=float(input("unesite Sirinu: "))
        formatheader()
        for roba in entitete.roba:
            roba1=roba.sirina
            if ulaz==roba1:
                print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("")
        pretragaRobe()
    elif unos=="6":
        cisti()
        ulaz=float(input("unesite Duzinu: "))
        formatheader()
        for roba in entitete.roba:
            roba1=roba.duzina
            if ulaz==roba1:
                print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("")
        pretragaRobe()
    elif unos=="7":
        cisti()
        ulaz=float(input("unesite Visinu: "))
        formatheader()
        for roba in entitete.roba:
            roba1=roba.visina
            if ulaz==roba1:
                print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("")
        pretragaRobe()
    elif unos=="8":
        cisti()
        ulaz=float(input("unesite Tezinu robe: "))
        formatheader()
        for roba in entitete.roba:
            roba1=roba.tezinaRobe
            if ulaz==roba1:
                print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("")
        pretragaRobe()
    elif unos=="9":
        cisti()
        ulaz=input("unesite ID kodu potrazitelja: ")
        formatheader()
        for roba in entitete.roba:
            roba1=roba.identifikacioniKodPotrazitelja
            if ulaz==roba1:
                print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("")
        pretragaRobe()
    elif unos=="0":
        cisti()
        ulogaMenadzeraTransporta()
    else:
        print("-------------")
        print("Pogresan unos")
        print("-------------")
        pretragaRobe()
def formatheader():
    print("\n")
    print(
      "   Oznaka   |  Naziv    |      Opis       |   Sirina   |  Duzina  |  Visina  |Tezina robe | ID kod|\n" 
      "------------+-----------+-----------------+------------+----------+----------+------------|-------|") 



    