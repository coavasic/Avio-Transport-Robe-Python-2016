'''
Created on Jun 13, 2016

@author: Vasic
'''
from objekti.entiteti import Roba
from ucitati import entitete
from ucitati.entitete import prostori




def ucitavanjeRobe(fajl):
    
    with open(fajl, "r") as f:
        for line in f.readlines():
            atributi = line.split("|")
            if atributi[5] == " ":
                prostorZaTeret = None
            for prostor in prostori:
                if atributi[5] == prostor.oznaka:
                    prostorZaTeret = prostor
                
            r = Roba(atributi[0], atributi[1], atributi[2],
                    float(atributi[3]), atributi[4],
                    prostorZaTeret, float(atributi[6]),
                    float(atributi[7]), float(atributi[8]))
    
    
            entitete.roba.append(r)
            