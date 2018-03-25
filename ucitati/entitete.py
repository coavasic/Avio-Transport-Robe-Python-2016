'''
Created on May 13, 2016

@author: Vasic
'''




hangari = []
prostori = []
avioni = []
roba = []



def ucitavanjeHangara(fajl):
    from objekti.entiteti import Hangar
    with open(fajl, "r") as f:
        for line in f.readlines():
            atributi = line.split("|")
            x = Hangar(atributi[0], atributi[1], float(atributi[2]), float(atributi[3]), float(atributi[4]), atributi[5])
            hangari.append(x)
    
    return hangari
            
def ucitavanjeAviona(fajl):
    from objekti.entiteti import Avion
    with open(fajl, "r") as f:
        for line in f.readlines():
            atributi = line.split("|")
            oznakaHangara = atributi[6]
            if oznakaHangara == " ":
                hangar2 = None
            else:
                for hangar1 in hangari:
                    if oznakaHangara == hangar1.oznaka:
                        hangar2 = hangar1
          
            x = Avion(atributi[0], atributi[1], atributi[2], atributi[3], atributi[4], atributi[5] , hangar2,
                    atributi[7], atributi[8], atributi[9], atributi[10])
            avioni.append(x)
    return avioni

def ucitavanjeProstorZaTeret(fajl):
    from objekti.entiteti import ProstorZaTeret
    with open(fajl, "r") as f:
        for line in f.readlines():
            atributi = line.split("|")
            oznakaAviona = atributi[5]
            
            for avion1 in avioni:
                if oznakaAviona == avion1.oznaka:
                    avion = avion1
            x = ProstorZaTeret(atributi[0], float(atributi[1]), float(atributi[2]),
                               float(atributi[3]),float(atributi[4]), avion, atributi[6])
            prostori.append(x)
    return prostori


def ucitavanjeRobe(fajl):
    from objekti.entiteti import Roba

    with open(fajl,"r") as f:
        for line in f.readlines():
            atributi = line.split("|")
            x = Roba(atributi[0], atributi[1], atributi[2]/
                     atributi[3], atributi[4], atributi[5]/
                     atributi[6], atributi[7], atributi[8])
            roba.append(x)
    return roba

    
    
    