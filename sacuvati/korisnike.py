'''
Created on May 13, 2016

@author: Vasic
'''
def sacuvatiKorisnikeZaLogovanje(fajl,lista):
    with open(fajl,"a") as f:
        for korisnik in lista:
            f.write(korisnik.identifikacioniKod)
            f.write("|")
            f.write(korisnik.korisnickoIme)
            f.write("|")
            f.write(korisnik.lozinka)
            f.write("|")
            f.write(korisnik.tipKorisnika)
            f.write("|")
            f.write(korisnik.ime)
            f.write("|")
            f.write(korisnik.prezime)
            f.write("|")
            f.write("\n")

def sacuvatiPotrazitelje(fajl,lista):
    with open(fajl,"a") as f:
        for korisnik in lista:
            f.write(korisnik.email)
            f.write("|")
            f.write(korisnik.adresa)
            f.write("|")
            f.write(korisnik.brTelefona)
            f.write("|")
            f.write(korisnik.identifikacioniKod)
            f.write("|")
            f.write(korisnik.ime)
            f.write("|")
            f.write(korisnik.prezime)
            f.write("|")
            f.write("\n")
           
