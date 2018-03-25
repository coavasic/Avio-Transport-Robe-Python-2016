'''
Created on May 13, 2016

@author: 
'''
from objekti.korisnici import Potrazitelj, KorisnikZaLogovanje

listaPotrazitelja=[]
listaKorisnika=[]

def ucitatiPotrazitelja(fajl):  
    with open(fajl,"r") as f:
        for line in f.readlines():
            atributi=line.split("|")
            korisnik=Potrazitelj(atributi[0],atributi[1],atributi[2],atributi[3],atributi[4],atributi[5])
            listaPotrazitelja.append(korisnik)
    return listaPotrazitelja

def ucitatiKorisnike(fajl):
    
    with open(fajl,"r") as f:
        for line in f.readlines():
            atributi=line.split("|")
            korisnik=KorisnikZaLogovanje(atributi[0],atributi[1],atributi[2],atributi[3],atributi[4],atributi[5])
            listaKorisnika.append(korisnik)
    return listaKorisnika