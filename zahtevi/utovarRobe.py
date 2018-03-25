'''
Created on Jul 3, 2016

@author: Vasic
'''
from zahtevi.odobravanjaZahteva import formatiranjeZahteva
from ucitati.ucitavanjeZahtevaZaRobu import zahteviZaTransport


def utovarRobe():
    formatiranjeZahteva("odobren")
    izbor = input("Izabrati zahtev za obradu >> ")
    for zahtev in zahteviZaTransport:
        if izbor == zahtev.identifikacioniKodZahteva:
            zahtev.statusZahteva = "utovarena"
            
    
    izbor = input("Zelite li da obradite jos neki zahtev? (y/n) >> ")
    if izbor == "y":
        utovarRobe()