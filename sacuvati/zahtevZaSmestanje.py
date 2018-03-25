'''
Created on Jul 5, 2016

@author: Vasic
'''

# idZahteva, oznakaAviona,datumKreiranja,
#                       hangar, identifikacioniKodMenadzera



def sacuvatiZahteveZaSmestanje(fajl, lista):
    with open(fajl, "w") as f:
        for zahtev in lista:
            f.write(zahtev.idZahteva)
            f.write("|")
            f.write(zahtev.oznakaAviona)
            f.write("|")
            f.write(zahtev.datumKreiranja)
            f.write("|")
            f.write(zahtev.oznakaHangara)
            f.write("|")
            f.write(zahtev.identifikacioniKodMenadzera)
            f.write("|")
            f.write("\n")