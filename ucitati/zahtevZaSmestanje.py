'''
Created on Jul 5, 2016

@author: Vasic
'''


# idZahteva, oznakaAviona,datumKreiranja,
#                       hangar, identifikacioniKodMenadzera



zahteviZaSmestanje = []
def ucitavanjeZahtevaZaSmestanje(fajl):
    from zahtevi.ZahtevZaSmestanje import ZahtevZaSmestanje
    with open(fajl, "r") as f:
        for line in f.readlines():
            atributi = line.split("|")
            
            z = ZahtevZaSmestanje(atributi[0], atributi[1],
                                  atributi[2], atributi[3],
                                  atributi[4])
        
            zahteviZaSmestanje.append(z)