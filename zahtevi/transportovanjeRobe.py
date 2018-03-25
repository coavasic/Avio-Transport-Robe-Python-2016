'''
Created on Jul 5, 2016

@author: Vasic
'''
from ucitati.ucitavanjeZahtevaZaRobu import zahteviZaTransport
from zahtevi.odobravanjaZahteva import formatiranjeAviona
from ucitati.entitete import prostori, roba
import time


def transportovanjeRobe():
    avioniT = avioniZaTransport()
    formatiranjeAviona(avioniT)
    unos = input("Uneti avion za transport >> ")
    for avion1 in avioniT:
        if avion1.oznaka == unos:
            avion = avion1
    
    try:        
        for zahtev in zahteviZaTransport:
            if zahtev.statusZahteva == "utovarena":
                if avion.oznaka == zahtev.avion.oznaka:
                    zahtev.datumTransportovanjaRobe = time.strftime("%d/%m/%Y %H:%M")
                    zahtev.statusZahteva = "transportovano"
    except UnboundLocalError:
        transportovanjeRobe()
    avion.hangar = None
    praznjenjeProstora(avion)
    praznjenjeRobe(zahteviZaTransport, avion)
    
    
    

def praznjenjeProstora(avion):
    for prostor in prostori:
        if prostor.avion.oznaka == avion.oznaka:
            prostor.zapremina = prostor.sirina * prostor.duzina * prostor.visina


def praznjenjeRobe(zahteviZaTransport, avion):
    for r in roba:
        for zahtev in zahteviZaTransport:
            for r1 in zahtev.listaRobe:
                if r.oznaka == r1.oznaka:
                    r.prostorZaTeret = None



def avioniZaTransport():
    avioniTransport = []
    for zahtev in zahteviZaTransport:
        if zahtev.statusZahteva == "utovarena":
            if zahtev.avion not in avioniTransport:
                avioniTransport.append(zahtev.avion)
    if avioniTransport:
        return avioniTransport
    else:
        from korisnici.menadzerHangara import ulogaHangara
        ulogaHangara()
