'''
Created on May 24, 2016

@author: Lazar-PC
'''

from ucitati import entitete
from zahtevi.utovarRobe import utovarRobe
from ucitati.ucitavanjeZahtevaZaRobu import zahteviZaTransport
import time
from glavni.main import cisti

def ulogaRadnika():
    
    """  Uloga korisnika sistema: Ranik 
    radnik moze da odobrava zahteve za utovar
    da vidi koji su odobreni  zahtevi , pretrazuje
    Robu, Avione i Hangare"""
    
    from glavni.vrednosti import logovanje
    print("radnik")
    print("-------------------")
    print("[1] Odobravanje zahteva za utovar")
    print("[2] Odobreni zahtevi za smestaj-pregled")
    print("[3] Pretraga hangara")
    print("[4] Pretraga aviona")
    print("[5] Pretraga robe")
    print("[0] Izlaz")
    print("")
    unos=str(input("Izbor: "))
    if unos == "1":
        cisti()
        utovarRobe()
        ulogaRadnika()
    if unos=="2":
        cisti()
        print("")
        odobreniZahtevi()
        ulogaRadnika()
    if unos=="3":
        cisti()
        pretragaHangara()
        ulogaRadnika()
    elif unos=="4":
        cisti()
        pretragaAviona()
        ulogaRadnika()
    elif unos=="5":
        cisti()
        pretragaRobe()
        ulogaRadnika()
    elif unos=="0":
        cisti()
        logovanje()
    else:
        print("pogresan unos")
        print("")
        ulogaRadnika()
        
        
def pretragaHangara():
    
    """ Pretraga hangara se pretrazuje po oznaci,
    nazivu, sirini, duzini, visini, dok je pokrenuta funkcija
    pretraga je pokrenuta"""     
    
    
    print("[1]-prikazi sve hangare")
    print("[2]-pretraga hangara po oznaci")
    print("[3]-pretraga hangara po nazivu")
    print("[4]-pretraga hangara po sirini")
    print("[5]-pretraga hangara po duzini")
    print("[6]-pretraga hangara po visini")
    print("[0]-Izlaz")
    unos=str(input("Izbor: "))
    if unos=="1":
        cisti()
        formatheader()
        for hangari in entitete.hangari:    
            print("{0:10}|{1:11}|{2:12}|{3:10}|{4:10}|".format(hangari.oznaka,hangari.naziv,hangari.sirina, hangari.duzina, hangari.visina))
        print("")
        pretragaHangara()
        
    elif unos=="2":
        cisti()
        hangar1=str(input("trazeni hangar: "))
        formatheader()
        for hangari in entitete.hangari:
            hangar2=hangari.oznaka
            if hangar1==hangar2:
                print("{0:10}|{1:11}|{2:12}|{3:10}|{4:10}|".format(hangari.oznaka,hangari.naziv,hangari.sirina, hangari.duzina, hangari.visina))
        print("")
        pretragaHangara()
    elif unos=="3":
        cisti()
        hangar1=str(input("trazeni hangar: "))
        formatheader()
        for hangari in entitete.hangari:
            hangar2=hangari.naziv
            if hangar1==hangar2:
                print("{0:10}|{1:11}|{2:12}|{3:10}|{4:10}|".format(hangari.oznaka,hangari.naziv,hangari.sirina, hangari.duzina, hangari.visina))
                
        print("")
        pretragaHangara()
    elif unos=="4":
        cisti()
        hangar1=float(input("trazeni hangar: "))
        formatheader()
        for hangari in entitete.hangari:
            hangar2=hangari.sirina
            if hangar1==hangar2:
                print("{0:10}|{1:11}|{2:12}|{3:10}|{4:10}|".format(hangari.oznaka,hangari.naziv,hangari.sirina, hangari.duzina, hangari.visina))
        print("")
        pretragaHangara()
    elif unos=="5":
        cisti()
        hangar1=float(input("trazeni hangar: "))
        formatheader()
        for hangari in entitete.hangari:
            hangar2=hangari.duzina
            if hangar1==hangar2:
                print(hangari.naziv,hangari.duzina)  
        print("")
        pretragaHangara()        
    elif unos=="6":
        cisti()
        hangar1=float(input("trazeni hangar: "))
        formatheader()
        for hangari in entitete.hangari:
            hangar2=hangari.visina
            if hangar1==hangar2:
                print("{0:10}|{1:11}|{2:12}|{3:10}|{4:10}|".format(hangari.oznaka,hangari.naziv,hangari.sirina, hangari.duzina, hangari.visina))
        print("")
        pretragaHangara()            
    elif unos=="0":
        cisti()
        ulogaRadnika()
    else:
        print("--------------")
        print("pogresan unsos")
        print("")
        pretragaHangara()           
        
def pretragaAviona():
    
    """ Pretraga aviona se pretrazuje po sledecim atributima: 
    oznaci, nazivu, godini proizvodnje, rasponu krila, po nosivosti"""
    
    print("[1] prikazi sve avione")
    print("[2] trazi po oznaci")
    print("[3] trazi po nazivu")
    print("[4] trazi po godini proizvodnje")
    print("[5] trazi po rasponu krila")
    print("[6] trazi po nosivosti")
    print("[0] exit")
    unos=str(input("unesi broj: "))
    
    if unos=="1":
        formatheader1()
        for avion in entitete.avioni:
            print("{0:12}|{1:11}|{2:12}|{3:16}|{4:12}|".format(avion.oznaka,avion.naziv, avion.godiste, avion.rasponKrila, avion.ukupnaNosivost))
        print("")
        pretragaAviona()
        
    elif unos=="2":
        oznaka1=str(input("uneseite oznaku aviona: "))
        formatheader1()
        for avion in entitete.avioni:
            oznaka2=avion.oznaka
            if oznaka1==oznaka2:
                print("{0:12}|{1:11}|{2:12}|{3:16}|{4:12}|".format(avion.oznaka,avion.naziv, avion.godiste, avion.rasponKrila, avion.ukupnaNosivost))
        print("")
        pretragaAviona()
    
    elif unos=="3": 
        oznaka1=str(input("uneseite naziv aviona: "))
        formatheader1()
        for avion in entitete.avioni:
            oznaka2=avion.naziv
            if oznaka1==oznaka2:
                print("{0:12}|{1:11}|{2:12}|{3:16}|{4:12}|".format(avion.oznaka,avion.naziv, avion.godiste, avion.rasponKrila, avion.ukupnaNosivost))           
        print("")
        pretragaAviona()
    
    elif unos=="6":
        oznaka1=str(input("uneseite nosivosti aviona: "))
        formatheader1()
        for avion in entitete.avioni:
            oznaka2=avion.ukupnaNosivost
            if oznaka1==oznaka2:
                print("{0:12}|{1:11}|{2:12}|{3:16}|{4:12}|".format(avion.oznaka,avion.naziv, avion.godiste, avion.rasponKrila, avion.ukupnaNosivost)) 
        print("")
        pretragaAviona()
    
    elif unos == "0":
        ulogaRadnika()

    else:
        print("-------------")
        print("pogresan unos")
        print("")
        pretragaAviona()
    
def pretragaRobe():
    
    """ Pretraga robe, radnik moze da pretrazuje robu
    po sledecim atributima Oznaci, Nazivu, Opisu, Sirini, Duzini
    Visini, Tezini i ID kodu , nakon pretrage, korisnik ostaje u 
    funkciji pretraga robe sve dok ne izadje """
        
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
        formatheaderRobe()
        for roba in entitete.roba: 
            print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("") 
        pretragaRobe()        
    elif unos=="2":
        ulaz=input("unesite Oznaci: ")
        formatheaderRobe()
        for roba in entitete.roba:
            roba1=roba.oznaka
            if ulaz==roba1:
                print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("")
        pretragaRobe()
    elif unos=="3":
        ulaz=input("unesite Naziv: ")
        formatheaderRobe()
        for roba in entitete.roba:
            roba1=roba.naziv
            if ulaz==roba1:
                print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("")
        pretragaRobe()
    elif unos=="4":
        ulaz=input("unesite Opis: ")
        formatheaderRobe()
        for roba in entitete.roba:
            roba1=roba.opis
            if ulaz==roba1:
                print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("")
        pretragaRobe()
    elif unos=="5":
        ulaz=float(input("unesite Sirinu: "))
        formatheaderRobe()
        for roba in entitete.roba:
            roba1=roba.sirina
            if ulaz==roba1:
                print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("")
        pretragaRobe()
    elif unos=="6":
        ulaz=float(input("unesite Duzinu: "))
        formatheaderRobe()
        for roba in entitete.roba:
            roba1=roba.duzina
            if ulaz==roba1:
                print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("")
        pretragaRobe()
    elif unos=="7":
        ulaz=float(input("unesite Visinu: "))
        formatheaderRobe()
        for roba in entitete.roba:
            roba1=roba.visina
            if ulaz==roba1:
                print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("")
        pretragaRobe()
    elif unos=="8":
        ulaz=float(input("unesite Tezinu robe: "))
        formatheaderRobe()
        for roba in entitete.roba:
            roba1=roba.tezinaRobe
            if ulaz==roba1:
                print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("")
        pretragaRobe()
    elif unos=="9":
        ulaz=input("unesite ID kodu potrazitelja: ")
        formatheaderRobe()
        for roba in entitete.roba:
            roba1=roba.identifikacioniKodPotrazitelja
            if ulaz==roba1:
                print("{0:12}|{1:11}|{2:17}|{3:12}|{4:10}|{5:10}|{6:12}|{7:10}".format(roba.oznaka,roba.naziv,roba.opis,roba.sirina, roba.duzina, roba.visina,roba.tezinaRobe,roba.identifikacioniKodPotrazitelja))
        print("")
        pretragaRobe()
    elif unos=="0":
        ulogaRadnika()
    else:
        print("-------------")
        print("Pogresan unos")
        print("-------------")
        pretragaRobe()
        
def formatheaderRobe():
    print("\n")
    print(
      "   Oznaka   |  Naziv    |      Opis       |   Sirina   |  Duzina  |  Visina  |Tezina robe | ID kod|\n" 
      "------------+-----------+-----------------+------------+----------+----------+------------|-------|") 
    
def odobreniZahtevi():
    
    print("[1]-odobreni zahtevi")
    print("[0]-izlaz")
    unos=str(input("uneti broj: "))
    if unos=="1":   
        formatheaderZaOdobrene()
        a="odobren"
        for zahtev in zahteviZaTransport:
            if zahtev.statusZahteva==a:
                print("{0:14}|{1:17}|{2:24}|{3:16}|{4:19}|{5:13}".format(zahtev.identifikacioniKodZahteva,zahtev.datumKreiranjaZahteva,zahtev.datumTransportovanjaRobe,zahtev.odrediste,zahtev.identifikacioniKodPotrazitelja,zahtev.statusZahteva))
            
        print("")
        odobreniZahtevi()
        
    elif unos=="0":
        ulogaRadnika()
        
def dostavaRobe():
        a="utovarena"
        b="dostavljena"
        for zahtev in zahteviZaTransport:
            if zahtev.statusZahteva==a:
                time.sleep(5)
                zahtev.statusZahteva=b 
                print("{0:14}|{1:17}|{2:24}|{3:16}|{4:19}|{5:13}".format(zahtev.identifikacioniKodZahteva,zahtev.datumKreiranjaZahteva,zahtev.datumTransportovanjaRobe,zahtev.odrediste,zahtev.identifikacioniKodPotrazitelja,zahtev.statusZahteva))

        
def formatheaderZaOdobrene():
    print("\n")
    print(
      "ID kod zahteva| Datum Kreiranja | Datum Transportovanja  |    Odrediste   |ID kod Potrazitelja|  Status  |\n" 
      "--------------+-----------------+------------------------+----------------+-------------------+----------")  
def formatheader():
    print("\n")
    print(
      "  Oznaka  |    Naziv  |   Sirina   |  Duzina  |  Visina  |\n" 
      "----------+-----------+------------+----------+----------+") 
def formatheader1():
    print("\n")
    print(
      "   Oznaka   |    Naziv  |   Godiste  |  Raspon krila  |  Nosivost  |\n" 
      "------------+-----------+------------+----------------+------------+") 
    
    