'''
Created on May 12, 2016

@author: Vasic
'''


class Korisnik(object):
    """Klasa korisnici
    """
    def __init__(self, identifikacioniKod, ime, prezime):
        self.identifikacioniKod = identifikacioniKod
        self.ime = ime
        self.prezime = prezime
    def __str__(self):
        return self.ime+" "+self.prezime
             
class Potrazitelj(Korisnik):
    """Klasa Potrazitelj usluga"""
    def __init__(self,email,adresa,brTelefona,identifikacioniKod,ime, prezime):
        Korisnik.__init__(self,identifikacioniKod,ime,prezime)
        self.email=email
        self.adresa=adresa
        self.brTelefona=brTelefona
    def __str__(self):
        return Korisnik.__str__(self)+" "+self.identifikacioniKod

class KorisnikZaLogovanje(Korisnik):
    menadzerTransporta="Menadzer transporta"
    menadzerHangara="Menadzer hangara"
    radnik="Radnik"
    def __init__(self,identifikacioniKod,korisnickoIme,lozinka,tipKorisnika,ime,prezime):
        Korisnik.__init__(self, identifikacioniKod, ime, prezime)    
        self.korisnickoIme=korisnickoIme
        self.lozinka=lozinka
        self.tipKorisnika=tipKorisnika
        def __str__(self):
            return Korisnik.__str__(self)+" "+self.tipKorisnika
        

        