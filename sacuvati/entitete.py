'''
Created on May 13, 2016

@author: Vasic
'''


def sacuvatiHangare(fajl, lista):
    with open(fajl, "w") as f:
        for hangar in lista:
            f.write(hangar.oznaka)
            f.write("|")
            f.write(hangar.naziv)
            f.write("|")
            f.write(str(hangar.sirina))
            f.write("|")
            f.write(str(hangar.duzina))
            f.write("|")
            f.write(str(hangar.visina))
            f.write("|")
            f.write(hangar.stanje)
            f.write("|")
            f.write("\n")
            
            
            
def sacuvatiAvione(fajl, lista):
    with open(fajl, "w") as f:
        for avion in lista:
            f.write(avion.oznaka)
            f.write("|")
            f.write(avion.naziv)
            f.write("|")
            f.write(avion.godiste)
            f.write("|")
            f.write(str(avion.rasponKrila))
            f.write("|")
            f.write(avion.ukupnaNosivost)
            f.write("|")
            f.write(avion.relacija)
            f.write("|")
            if avion.hangar is None:
                f.write(" ")
            else:
                f.write(avion.hangar.oznaka)
            f.write("|")
            f.write(str(avion.sirina))
            f.write("|")
            f.write(str(avion.duzina))
            f.write("|")
            f.write(str(avion.visina))
            f.write("|")
            f.write(avion.stanje)
            f.write("|")
            f.write("\n")
            
def sacuvatiProstorZaTeret(fajl, lista):
    with open(fajl, "w") as f:
        for prostor in lista:
            f.write(prostor.oznaka)
            f.write("|")
            f.write(str(prostor.sirina))
            f.write("|")
            f.write(str(prostor.duzina))
            f.write("|")
            f.write(str(prostor.visina))
            f.write("|")
            f.write(str(prostor.zapremina))
            f.write("|")
            f.write(prostor.avion.oznaka)
            f.write("|")
            f.write(prostor.stanje)

            