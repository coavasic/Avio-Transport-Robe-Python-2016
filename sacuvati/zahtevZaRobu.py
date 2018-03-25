'''
Created on Jun 2, 2016

@author: Lazar-PC
'''


def sacuvatiZahtev(lista):
    from glavni.main import zahtevZaTransportTxt
    with open(zahtevZaTransportTxt, "w") as f:
        for zahtev in lista:
            f.write(zahtev.identifikacioniKodZahteva)
            f.write("|")
            f.write(zahtev.datumKreiranjaZahteva)
            f.write("|")
            if zahtev.datumTransportovanjaRobe is None:
                f.write(" ")
            else:
                f.write(zahtev.datumTransportovanjaRobe)
            f.write("|")
            f.write(zahtev.odrediste)
            f.write("|")
            f.write(zahtev.identifikacioniKodPotrazitelja)
            f.write("|")
            if zahtev.avion is None:
                f.write(" ")
            else:
                f.write(zahtev.avion.oznaka)
            f.write("|")
            for roba in zahtev.listaRobe:
                f.write(roba.oznaka)
                f.write("/")
            f.write("|")
            f.write(zahtev.statusZahteva)
            f.write("|")
            f.write("\n")