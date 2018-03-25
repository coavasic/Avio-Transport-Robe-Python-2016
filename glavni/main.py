'''
Created on May 12, 2016

@author: Vasic
'''

from ucitati import entitete
import os
from sacuvati.entitete import sacuvatiHangare, sacuvatiProstorZaTeret
from sacuvati.entitete import sacuvatiAvione
from ucitati.entitete import ucitavanjeHangara, ucitavanjeAviona,\
    ucitavanjeProstorZaTeret
from sacuvati.sacuvatiRobu import sacuvatiRobu
from ucitati.ucitavanjeZahtevaZaRobu import ucitavanjeZahteva,\
    zahteviZaTransport
from ucitati.robu import ucitavanjeRobe
from sacuvati.zahtevZaSmestanje import sacuvatiZahteveZaSmestanje
from ucitati.zahtevZaSmestanje import ucitavanjeZahtevaZaSmestanje






def cisti():
    os.system('cls' if os.name == 'nt' else 'clear')




def apsolutnaPutanja(fajl):
        return os.path.join(os.path.dirname(__file__),"..",fajl)
hangariTxt = apsolutnaPutanja("hangari.txt")
avioniTxt = apsolutnaPutanja("avioni.txt")
robaTxt=apsolutnaPutanja("roba.txt")
prostorTxt = apsolutnaPutanja("prostorZaTeret.txt")
zahtevZaTransportTxt = apsolutnaPutanja("zahtevZaTransport.txt")
zahtevZaSmestanjeTxt = apsolutnaPutanja("zahtevZaSmestanje.txt")
if __name__ == '__main__':
    
    
    
    
    ucitavanjeHangara(hangariTxt)
    ucitavanjeAviona(avioniTxt)
    ucitavanjeProstorZaTeret(prostorTxt)
    ucitavanjeRobe(robaTxt)
    ucitavanjeZahteva(zahtevZaTransportTxt)
    ucitavanjeZahtevaZaSmestanje(zahtevZaSmestanjeTxt)
    
    

  
    

    
    
    from glavni.vrednosti import logovanje
    cisti()
    logovanje()
    cisti()

def cuvanja():
    hangariTxt = apsolutnaPutanja("hangari.txt")
    avioniTxt = apsolutnaPutanja("avioni.txt")
    robaTxt=apsolutnaPutanja("roba.txt")
    prostorTxt = apsolutnaPutanja("prostorZaTeret.txt")
    zahtevZaTransportTxt = apsolutnaPutanja("zahtevZaTransport.txt")
    zahtevZaSmestanjeTxt = apsolutnaPutanja("zahtevZaSmestanje.txt")
    sacuvatiAvione(avioniTxt, entitete.avioni)
    sacuvatiHangare(hangariTxt, entitete.hangari)
    sacuvatiProstorZaTeret(prostorTxt, entitete.prostori)
    sacuvatiRobu(robaTxt, entitete.roba)
    from sacuvati.zahtevZaRobu import sacuvatiZahtev
    sacuvatiZahtev(zahteviZaTransport)
    from ucitati.zahtevZaSmestanje import zahteviZaSmestanje
    sacuvatiZahteveZaSmestanje(zahtevZaSmestanjeTxt, zahteviZaSmestanje)
    quit()

    
    
        

        
    