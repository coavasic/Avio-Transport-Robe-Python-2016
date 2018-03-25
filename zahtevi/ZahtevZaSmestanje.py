'''
Created on Jun 12, 2016

@author: Vasic
'''
from ucitati import entitete
from objekti.entiteti import prikazHangara
from glavni.pronadji import pronadjiAvione
from zahtevi.odobravanjaZahteva import formatiranjeAviona
import time

from ucitati.zahtevZaSmestanje import zahteviZaSmestanje




class ZahtevZaSmestanje(object):
    '''
    Klasa zahtev za smestanje aviona u hangar
    '''


    def __init__(self, idZahteva, oznakaAviona,datumKreiranja,
                oznakaHangara,
                 identifikacioniKodMenadzera):
        '''
        Constructor
        '''
        self.idZahteva = idZahteva
        self.oznakaAviona = oznakaAviona
        self.datumKreiranja = datumKreiranja
        self.oznakaHangara = oznakaHangara
        self.identifikacioniKodMenadzera = identifikacioniKodMenadzera
        
        

def kreiranjeZahtevaZaSmestanje():
    """Kreiranje zahteva za smestanje aviona u hangar"""
    idZahteva = str(len(zahteviZaSmestanje)+1)
    prikazAvionaVanHangara()
    #Pronalazenje trazenog aviona koji nije u hangaru
    idAviona = input("Uneti identifikacioni kod aviona >> ")
    for i in entitete.avioni:
        if i.oznaka == idAviona:
            if i.hangar is None:
                oznakaAviona = i
    
    #Datume sreditii
    datumKreiranja = time.strftime("%d/%m/%Y")
    prikazHangara()
    hangar = izborHangara()
    hangar1 = hangar.oznaka
    from glavni.vrednosti import ulogovan
    if ulogovan:
        for u in ulogovan:
            identifikacioniKodMenadzera = u.identifikacioniKod
    else:
        identifikacioniKodMenadzera = "blabla"
    #Poziv funkcije za proveru da li avion moze da stane u izabrani hangar
    #Kreiranje zahteva za smestanje i smestanje aviona u habgar
    #avion.hangar   None -> izabrani hangar       
    if proveraAvionUHangar(hangar, oznakaAviona.duzina, oznakaAviona.rasponKrila, oznakaAviona.visina) is True:
    
        z = ZahtevZaSmestanje(idZahteva, oznakaAviona.oznaka ,datumKreiranja,
                      hangar1, identifikacioniKodMenadzera)
        
        oznakaAviona.hangar = hangar             
        zahteviZaSmestanje.append(z)
        izbor = input("Zelite li jos zahteva za smestanje? (y/n)")
        if izbor == "y":
            kreiranjeZahtevaZaSmestanje()
    
    else:
        print("Avion ne moze da stane u hangar")
        kreiranjeZahtevaZaSmestanje()
    
        
        
    
        


def proveraAvionUHangar(oznakaHangara, duzina, sirina, visina):
    """Provera da li avion moze da stane u hangar"""
    
    #Lista aviona za izabrani hangar
    listaAviona = pronadjiAvione(oznakaHangara)
    for hangar1 in entitete.hangari:
        if oznakaHangara.oznaka == hangar1.oznaka:
            hangar = hangar1
    
    if len(listaAviona) > 0:       
        for avion in listaAviona:
            #oduzimanje sirine aviona koji su vec u hangaru
            hangarSirina = float(hangar.sirina) - float(avion.rasponKrila)
    else:
        hangarSirina = hangar.sirina
    
    if hangar.duzina >= float(duzina) and hangarSirina >= float(sirina):
        return True
    else:
        return False



def izborHangara():
    """Izbor hangara"""
    prikazHangara()
    oznakaHangara = input("Oznaka hangara>> ")
    for hangar1 in entitete.hangari:
        if oznakaHangara == hangar1.oznaka:
            hangar = hangar1
            return hangar
    print("Ne postoji izabrani hangar!")
    return izborHangara()

#Prikazivanje aviona koji nisu u hangaru
def prikazAvionaVanHangara():
    lista = []
    
    for i in entitete.avioni:
        if i.hangar is None:
            lista.append(i)   
    if lista:
        formatiranjeAviona(lista)
    else:
        print("Ne postoji avion van hangara!")
        from korisnici.menadzerHangara import ulogaHangara
        ulogaHangara()         