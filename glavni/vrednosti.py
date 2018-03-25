'''
Created on May 16, 2016

@author: Lazar-PC
'''
import os
import random
from objekti.korisnici import Potrazitelj
from sacuvati.korisnike import sacuvatiPotrazitelje
from ucitati.korisnike import ucitatiPotrazitelja,ucitatiKorisnike
from ucitati import korisnike
from korisnici.menadzerTransporta import ulogaMenadzeraTransporta
from korisnici.menadzerHangara import ulogaHangara
from korisnici.radnik import ulogaRadnika
import time
from korisnici.potrazitelji import potraziteljUloga
from glavni.main import cisti
from glavni.prikaziSve import prikaziSve


ulogovan = []

def apsolutnaPutanja(fajl):
    return os.path.join(os.path.dirname(__file__),"..",fajl)

potraziteljTxt=apsolutnaPutanja("potrazitelji.txt")
korisniciTxt=apsolutnaPutanja("korisnici.txt")
potrazitelji=[]
korisnici=[]
ulogovan = []

def logovanjeKorisnici():
    cisti()
   
    ime=input("Unesite vas korisnicko ime: ")
    lozinka=input("Unesite vasu lozinku: ")  
    print("")
    ucitatiKorisnike(korisniciTxt)       
   
    for korisnici in korisnike.listaKorisnika:
        idkodod=korisnici.korisnickoIme
        lozinka1=korisnici.lozinka
        if ime==idkodod and lozinka==lozinka1:
            ulogovan.clear()
            ulogovan.append(korisnici)
            print(korisnici.ime,korisnici.prezime,": ",korisnici.tipKorisnika)
            if korisnici.tipKorisnika =="Menadzer transporta":
               
                ulogaMenadzeraTransporta()
            elif korisnici.tipKorisnika=="Menadzer hangara":
                ulogaHangara()
            elif korisnici.tipKorisnika=="radnik":
                ulogaRadnika()
    else:
        print("pogresna korisnicko ime ili sifra")
        print("")
        cisti()
        logovanjeKorisnici()
def pretragaPoIdkodu():
    cisti()
    idKod=input("Unesite vas ID kod: ")
    print("[exit]- Izlaz")
    ucitatiPotrazitelja(potraziteljTxt)
            
    for potrazitelj in korisnike.listaPotrazitelja:
        idkodod=potrazitelj.identifikacioniKod
        if idKod==idkodod:
            print(potrazitelj.ime)
            ulogovan.clear()
            ulogovan.append(potrazitelj)
            potraziteljUloga() 
    if idKod=="exit":
        logovanjePotrazitelji()
      
    else:           
        print("--------------------------")
        print("       nema id koda       ")
        print("--------------------------") 
        pretragaPoIdkodu()  
def logovanjePotrazitelji():
    cisti()
    print("[1] Novi korisnik")
    print("[2] Pristup sa ID Kodom")
    print("[3] Izlaz")
    a=str(input("unos: "))
        
    if a=="1":
        ime=input("vase ime: ")
        prezime=input("vase prezime: ")
        email=input("vas email: ")
        adresa=input("vasa adresa")
        brTelefona=input("vas br. Telefona: ")
        identifikacioniKod=str(random.randrange(1000, 100000, 20))
        print("------------")
        print("vas ID za pristup", identifikacioniKod)                      
        print("------------")
        p=Potrazitelj(email,adresa,brTelefona,identifikacioniKod,ime,prezime)
        potrazitelji.append(p)
        ulogovan.clear()
        ulogovan.append(p)
        sacuvatiPotrazitelje(potraziteljTxt,potrazitelji)
        potraziteljUloga()      
        #upisati funkciju koja salje dalje
    elif a=="2": 
        pretragaPoIdkodu()
    elif a=="3":
        logovanje()
    else:
        print("-------------")
        print("pogresan unos")
        print("-------------")  
        cisti()  
        logovanjePotrazitelji()
  
    
def logovanje():
    localtime = time.asctime( time.localtime(time.time()) )
    print("Trenutno vreme:", localtime)
    print("")
    print("Aerodrom 'Nikola Tesla'")
    print("------------------------")
    print("\n")
    print("[1] Korisnik sistema")
    print("[2] Potrazitelj")
    print("[3] Prikazi strukturu aerodroma")
    print("[exit] - Exit")
    unos=str(input("unesite izbor: "))
    
    if unos=="1":
        cisti()
        logovanjeKorisnici()        
    elif unos=="2":
        cisti()
        logovanjePotrazitelji()
    elif unos == "3":
        cisti()
        prikaziSve()
        logovanje()
    elif unos == "exit":
        from glavni.main import cuvanja
        cuvanja()
    
    else:
        print("pogresan unos")
        cisti()
        logovanje()


    
if __name__ == '__main__':
  
    logovanje()
    
    
    
    