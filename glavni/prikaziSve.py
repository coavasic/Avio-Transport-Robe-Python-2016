'''
Created on Jul 3, 2016

@author: Vasic

Prikaz cele arhitekture aerodroma
'''
from ucitati.entitete import hangari, avioni, prostori
from glavni.main import cisti

cisti()
print("Aerodrom Nikola Tesla")
def prikaziSve():
    for hangar in hangari:
        print("    " + hangar.naziv)
        for avion in avioni:
            if avion.hangar is not None:
                if avion.hangar.oznaka == hangar.oznaka:
                    print("        " + avion.naziv)
                    for prostor in prostori:
                        if prostor.avion.oznaka == avion.oznaka:
                            print("            " + prostor.oznaka)