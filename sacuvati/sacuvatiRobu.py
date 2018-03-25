'''
Created on Jun 9, 2016

@author: Lazar-PC
'''


def sacuvatiRobu(fajl,lista):
    with open(fajl,"w")as f:
        for roba in lista:
            f.write(roba.oznaka)
            f.write("|")
            f.write(roba.naziv)
            f.write("|")
            f.write(roba.opis)
            f.write("|")
            f.write(str(roba.tezinaRobe))
            f.write("|")
            f.write(roba.identifikacioniKodPotrazitelja)
            f.write("|")
            if roba.prostorZaTeret is None:
                f.write(" ")
            else:    
                f.write(roba.prostorZaTeret.oznaka)
            f.write("|")
            f.write(str(roba.duzina))
            f.write("|")
            f.write(str(roba.sirina))
            f.write("|")
            f.write(str(roba.visina))
            f.write("|")
            f.write("\n")