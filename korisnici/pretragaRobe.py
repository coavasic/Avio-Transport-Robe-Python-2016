'''
Created on Jun 30, 2016

@author: Lazar-PC
'''
from ucitati import entitete
from ucitati.ucitavanjeZahtevaZaRobu import zahteviZaTransport
from korisnici.menadzerTransporta import ulogaMenadzeraTransporta
from glavni.main import cisti

def pretragaRobe():
    
    """ Pretraga robe, menadzer hangara moze da pretrazuje robu
    po sledecim atributima Oznaci, Nazivu, Opisu, Sirini, Duzini
    Visini, Tezini i ID kodu , nakon pretrage, korisnik ostaje u 
    funkciji pretraga robe sve dok ne izadje """ 
    
    from korisnici.menadzerHangara import ulogaHangara
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
        cisti()
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
        cisti()
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
        cisti()
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
        cisti()
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
        cisti()
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
        cisti()
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
        cisti()
        pretragaRobe()
    
    elif unos=="0":
        cisti()
        ulogaHangara()
    
    else:
        cisti()
        print("-------------")
        print("Pogresan unos")
        print("-------------")
        
        pretragaRobe()
        
def formatheader():
    print("\n")
    print(
      "   Oznaka   |  Naziv    |      Opis       |   Sirina   |  Duzina  |  Visina  |Tezina robe | ID kod|\n" 
      "------------+-----------+-----------------+------------+----------+----------+------------|-------|") 
    
def formatheaderZahtevi():
    print("\n")
    print(
      "ID kod zahteva| Datum Kreiranja | Datum Transportovanja  |    Odrediste   |ID kod Potrazitelja|Oznaka aviona|  Status  |\n" 
      "--------------+-----------------+------------------------+----------------+-------------------+-------------+----------")  

def zahteviRobe():
    print("[1]-Prikazi sve zahteve")
    print("[0]-Izlaz")
    unos=str(input("izbor: "))
    if unos=="1":   
        cisti() 
        formatheaderZahtevi()
        for zahtev in zahteviZaTransport:
            if zahtev.avion is None:
                d=" "
            else:
                d=zahtev.avion.oznaka
            print("{0:14}|{1:17}|{2:24}|{3:16}|{4:19}|{5:13}|{6:11}".format(zahtev.identifikacioniKodZahteva,zahtev.datumKreiranjaZahteva,zahtev.datumTransportovanjaRobe,zahtev.odrediste,zahtev.identifikacioniKodPotrazitelja,d,zahtev.statusZahteva))
        print("")  
        zahteviRobe()  
    elif unos=="0":
        cisti()
        ulogaMenadzeraTransporta()
