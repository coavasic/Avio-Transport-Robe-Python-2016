'''
Created on Jul 3, 2016

@author: Lazar-PC
'''
import time
from ucitati.ucitavanjeZahtevaZaRobu import zahteviZaTransport


def sortiranje():
    from korisnici.menadzerTransporta import ulogaMenadzeraTransporta
    print("[1]- sortirani po datumu kreiranja")
    print("[0]- izlaz")
    unos = str(input("izaberi: "))
    if unos == "1":
        formatheaderZahtevi()
        zahteviZaTransport.sort(key = lambda x: time.mktime(tuple(time.strptime (x.datumKreiranjaZahteva, "%d/%m/%Y"))))
        for zahtev in zahteviZaTransport:      
            print("{0:14}|{1:17}|{2:24}|{3:16}|{4:19}|{5:13}".format(zahtev.identifikacioniKodZahteva,zahtev.datumKreiranjaZahteva,zahtev.datumTransportovanjaRobe,zahtev.odrediste,zahtev.identifikacioniKodPotrazitelja,zahtev.statusZahteva))
        print("")
        sortiranje()
    elif unos=="0":
        ulogaMenadzeraTransporta()
    else:
        sortiranje()
     
def formatheaderZahtevi():
    print(
      "ID kod zahteva| Datum Kreiranja | Datum Transportovanja  |    Odrediste   |ID kod Potrazitelja|  Status  |\n" 
      "--------------+-----------------+------------------------+----------------+-------------------+----------")  