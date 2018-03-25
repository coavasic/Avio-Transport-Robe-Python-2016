'''
Created on May 12, 2016

@author: Vasic
'''

from ucitati import entitete

class Dimenzija:
    """Klasa za dimenzije"""
    def __init__(self, sirina,duzina,visina):
        self.sirina=sirina
        self.duzina=duzina
        self.visina=visina
        
class Naziv:
    """klasa za oznake i naziv"""
    def __init__(self, naziv, oznaka):
        self.naziv = naziv
        self.oznaka = oznaka

class Aerodrom(object):
    """Klasa Aerodrom"""
    def __init__(self, naziv, adresa, lokacija):
        self.naziv = "Nikola Tesla"
        self.adresa = "Surcin"
        self.lokacija = "Beograd"



class Hangar(Dimenzija):
    """Klasa Hangar"""
    def __init__(self, oznaka, naziv, sirina, duzina, visina, stanje):
        Dimenzija.__init__(self, sirina, duzina, visina)
        self.oznaka = oznaka
        self.naziv = naziv
        self.stanje = stanje
        
def dodavanjeHangara():
    """Dodavanje Hangara"""
    print("*" * 25)
    print("* DODAVANJE HANGARA")
    lenHangar = str(len(entitete.hangari)+ 1)
    oznaka = "h" + lenHangar
    naziv = input("Uneti naziv hangara>> ")
    sirina = ucitajSirinu()
    duzina = ucitajDuzinu()
    visina = ucitajVisinu()
    stanje = "true"
    h = Hangar(oznaka, naziv, sirina, duzina, visina, stanje)
    entitete.hangari.append(h)

class Avion(Dimenzija):
    """Klasa Avion"""
    def __init__(self, oznaka, naziv, godiste, rasponKrila, ukupnaNosivost, relacija, hangar, sirina, duzina, visina, stanje):
        Dimenzija.__init__(self, sirina, duzina, visina)
        self.oznaka = oznaka
        self.naziv = naziv
        self.godiste = godiste
        self.rasponKrila = rasponKrila
        self.ukupnaNosivost = ukupnaNosivost
        self.relacija = relacija
        self.hangar = hangar
        self.stanje = stanje
        

def dodavanjeAvionaMain():
    
    dodavanjeAviona()
    print("Zelite li novi avion? (y/n)")
    
    izbor = input("Izbor>> ")
    if izbor == "y":
        dodavanjeAviona()
    else:
        pass
    



def dodavanjeAviona():
    """Dodavanje novog aviona"""
    print("*" * 25)
    print("* DODAVANJE AVIONA")
    lenAvion = str(len(entitete.avioni) + 1)
    oznaka = "a" + lenAvion
    hangar2 = None
    naziv = input("Uneti naziv>> ")
    godiste = input("Unesite godiste>> ")
    rasponKrila = ucitajDuzinu()
    ukupnaNosivost = input("Ukupna nosivost>> ")
    relacije = input("Relacije>> ")
    sirina = ucitajSirinu()
    duzina = ucitajDuzinu()
    visina = ucitajVisinu()
    stanje = "true"
    a = Avion(oznaka, naziv, godiste, rasponKrila, ukupnaNosivost, relacije, hangar2, sirina, duzina, visina, stanje)
    entitete.avioni.append(a)
    #funkciji za automarizovano kreiranje se salje avion, sirina, duzina i visina
    kreiranjeProstoraZaTeret(a, sirina, duzina, visina)
    




def kreiranjeProstoraZaTeret(avion, sirinaAviona, duzinaAviona, visinaAviona):
    """Automatizovano kreiranje ukupnog prostora za teret koji ce se kasnije deliti na manje prostore
        koji se koriste za smestanje robe"""
    ukupanProstorVisina = visinaAviona / 2
    ukupanProstorDuzina = duzinaAviona * 0.7
    ukupanProstorSirina = sirinaAviona * 0.7
    ukupanProstor = UkupanProstor(ukupanProstorSirina, ukupanProstorDuzina, ukupanProstorVisina)
    dodavanjeProstoraZaTeret(ukupanProstor, avion)
    

def dodavanjeProstoraZaTeret(ukupanProstor, avion):
    """Deljenje ukupnog prostora za teret na konacne prostore """
    print("*" * 25)
    print("* DODAVANJE PROSTORA ZA TERET")
    oznaka = avion.oznaka + "t" + str(len(entitete.prostori))
    duzina = ucitajDuzinu()
    visina = ukupanProstor.visina
    sirina = ukupanProstor.sirina
    stanje = "true"
    if duzina <= ukupanProstor.duzina:
        zapremina = sirina * duzina * visina
        p = ProstorZaTeret(oznaka, sirina, duzina, visina,zapremina, avion, stanje )
        entitete.prostori.append(p)
        novaDuzina = ukupanProstor.duzina - duzina
        if novaDuzina > 0:
            print("Zelite li da dodate jos prostora za teret? ")
            izbor = input("izbor>> ")
            if izbor == "y":
                ostalo = UkupanProstor(sirina, novaDuzina, visina)
                print("Preostala duzina =  " + str(ostalo.duzina))
                dodavanjeProstoraZaTeret(ostalo, avion)
            else:
                pass
        else:
            print("Nema vise mesta za nove prostore")
    else:
        print("Pogresna duzina")
        dodavanjeProstoraZaTeret(ukupanProstor, avion)
    
        
    
            
    
class UkupanProstor(Dimenzija):
    """Klasa za ukupan prostor koji se automatski dobija na osnovu dimenzija aviona"""
    def __init__(self, sirina, duzina, visina):
        Dimenzija.__init__(self, sirina, duzina, visina)   






def ucitajVisinu():
    visina1 = input("Uneti visinu>> ")                  
    try:                                            
        visina = float(visina1)
        return visina
    except:
        print("Visina mora biti float!")
        return ucitajVisinu()
def ucitajDuzinu():
    duzina1 = input("Uneti duzinu>> ")                  
    try:                                            
        duzina = float(duzina1)
        return duzina
    except:
        print("Duzina mora biti float!")
        return ucitajDuzinu()
    
    
def ucitajSirinu():
    sirina1 = input("Uneti sirinu>> ")                  
    try:                                            
        sirina = float(sirina1)
        return sirina
    except:
        print("Sirina mora biti float")
        return ucitajSirinu()

def prikazHangara():
    formatheader()
    for hangari in entitete.hangari:    
        print("{0:10}|{1:11}|{2:12}|{3:10}|{4:10}|".format(hangari.oznaka,hangari.naziv,hangari.sirina, hangari.duzina, hangari.visina))
    


def formatheader():
    print("\n")
    print(
      "  Oznaka  |    Naziv  |   Sirina   |  Duzina  |  Visina  |\n" 
      "----------+-----------+------------+----------+----------+")   
               
class ProstorZaTeret(Dimenzija,Naziv):
    """Klasa ProstorZaTeret"""
    def __init__(self, oznaka,sirina, duzina, visina, zapremina, avion, stanje):
        Dimenzija.__init__(self, sirina, duzina, visina)
        self.oznaka = oznaka
        self.zapremina = zapremina
        self.avion = avion
        self.stanje = stanje


class Roba(Dimenzija, Naziv):
    """Klasa Roba"""
    def __init__(self, oznaka, naziv, opis, tezinaRobe, identifikacioniKodPotrazitelja, prostorZaTeret, duzina, sirina, visina):
        Dimenzija.__init__(self, sirina, duzina, visina)
        Naziv.__init__(self, naziv, oznaka)
        self.opis = opis
        self.tezinaRobe = tezinaRobe
        self.identifikacioniKodPotrazitelja = identifikacioniKodPotrazitelja
        self.prostorZaTeret = prostorZaTeret
        
        
    
