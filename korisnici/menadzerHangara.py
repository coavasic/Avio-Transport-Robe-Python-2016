'''
Created on May 24, 2016

@author: Lazar-PC
'''
from korisnici.menadzerTransporta import pretragaHangara, pretragaAviona
from ucitati import entitete
from ucitati.entitete import ucitavanjeAviona
from glavni.main import avioniTxt, cisti
from objekti.entiteti import dodavanjeAviona, dodavanjeHangara
from korisnici.pretragaRobe import pretragaRobe
from zahtevi.ZahtevZaSmestanje import kreiranjeZahtevaZaSmestanje
from zahtevi.transportovanjeRobe import transportovanjeRobe


def ulogaHangara(): 
    
    """  Uloga korisnika sistema: Menadzer Hangara 
   moze da odbrava zahtev za smestanje aviona u hangar
   da vidi odobrene zahteve transporta, dodaje hanagre
   dodaje avione u hanagare i prostor za teret,
   pretrazuje:  Robu, Avione i Hangare  """
     
    from glavni.vrednosti import logovanje
    print("")
    print("Menadzer Hangara")
    print("-------------------")
    print("[x] Transportovanje robe")
    print("[1] Zahtev za smestanje aviona u hangar")
    print("[2] Dodavanje hangara")
    print("[3] Dodavanje novih aviona i prostora za teret" )
    print("[4] pretraga hangara")
    print("[5] pretraga aviona")
    print("[6] pretraga robe")
    print("[0] izlaz")
    print("")
    unos=str(input("Izbor: "))
    if unos == "x":
        cisti()
        transportovanjeRobe()
        ulogaHangara()
    if unos=="1":
        cisti()
        kreiranjeZahtevaZaSmestanje()
        ulogaHangara()      
    elif unos=="2":
        cisti()
        print("")
        dodavanjeHangara()
        ulogaHangara()       
    elif unos=="3":
        cisti()
        print("")
        dodavanjeAviona()
        ulogaHangara()
    elif unos=="4":
        cisti()
        pretragaHangara()
    elif unos=="5":
        cisti()
        pretragaAviona()
    elif unos=="6":
        cisti()
        pretragaRobe()
    elif unos=="0":
        cisti()
        logovanje()
    
    else:
        print("pogresan unos")
        print("")
        ulogaHangara()


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
        ulogaHangara()
        
    else:
        print("--------------")
        print("pogresan unsos")
        print("")
        cisti()
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
        cisti()
        formatheader1()
        for avion in entitete.avioni:
            print("{0:12}|{1:11}|{2:12}|{3:16}|{4:12}|".format(avion.oznaka,avion.naziv, avion.godiste, avion.rasponKrila, avion.ukupnaNosivost))
        print("")
        pretragaAviona()
        
    elif unos=="2":
        cisti()
        oznaka1=str(input("uneseite oznaku aviona: "))
        formatheader1()
        for avion in entitete.avioni:
            oznaka2=avion.oznaka
            if oznaka1==oznaka2:
                print("{0:12}|{1:11}|{2:12}|{3:16}|{4:12}|".format(avion.oznaka,avion.naziv, avion.godiste, avion.rasponKrila, avion.ukupnaNosivost))
        print("")
        pretragaAviona()
        
    elif unos=="3":
        cisti()
        oznaka1=str(input("uneseite naziv aviona: "))
        ucitavanjeAviona(avioniTxt)
        formatheader1()
        for avion in entitete.avioni:
            oznaka2=avion.naziv
            if oznaka1==oznaka2:
                print("{0:12}|{1:11}|{2:12}|{3:16}|{4:12}|".format(avion.oznaka,avion.naziv, avion.godiste, avion.rasponKrila, avion.ukupnaNosivost))           
        print("")
        pretragaAviona()
        
    elif unos=="4":
        cisti()
        oznaka1=str(input("uneseite godiste aviona: "))
        ucitavanjeAviona(avioniTxt)
        formatheader1()
        for avion in entitete.avioni:
            oznaka2=avion.godiste
            if oznaka1==oznaka2:
                print("{0:12}|{1:11}|{2:12}|{3:16}|{4:12}|".format(avion.oznaka,avion.naziv, avion.godiste, avion.rasponKrila, avion.ukupnaNosivost))           
        print("")
        pretragaAviona()
        
    elif unos=="5":
        cisti()
        oznaka1=str(input("uneseite raspon krila: "))
        formatheader1()
        for avion in entitete.avioni:
            oznaka2=avion.rasponKrila
            if oznaka1==oznaka2:
                print("{0:12}|{1:11}|{2:12}|{3:16}|{4:12}|".format(avion.oznaka,avion.naziv, avion.godiste, avion.rasponKrila, avion.ukupnaNosivost))           
        print("")
        pretragaAviona()            
        
    elif unos=="6":
        cisti()
        oznaka1=str(input("uneseite nosivosti aviona: "))
        formatheader1()
        for avion in entitete.avioni:
            oznaka2=avion.ukupnaNosivost
            if oznaka1==oznaka2:
                print("{0:12}|{1:11}|{2:12}|{3:16}|{4:12}|".format(avion.oznaka,avion.naziv, avion.godiste, avion.rasponKrila, avion.ukupnaNosivost)) 
        print("")
        pretragaAviona()
        
    elif unos == "0":
        cisti()
        ulogaHangara()    
    else:
        cisti()
        print("-------------")
        print("pogresan unos")
        print("")
        pretragaAviona()


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
