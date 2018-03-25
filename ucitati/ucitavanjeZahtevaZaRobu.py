from zahtevi.ZahtevZaTransport import ZahtevZaTransport
from ucitati.entitete import roba, avioni



zahteviZaTransport = []
                      

def ucitavanjeZahteva(fajl):
     
    with open(fajl, "r") as f:
        for line in f.readlines():
            listaRobe = [] 
            atributi = line.split("|")
            datumTransportovanja = atributi[2]
            if datumTransportovanja == " ":
                datumTransportovanjaRobe = None
            
            else:
                datumTransportovanjaRobe = atributi[2]
            
            oznaka = atributi[5]
            
            if oznaka == " ":
                avion = None
            
            for avion1 in avioni:
                if oznaka == avion1.oznaka:
                    avion = avion1
            
            robaT = atributi[6].split("/")
            for y in robaT[:-1]:
                r = dodeliRobu(y)
                listaRobe.append(r)
                
            
           
            z = ZahtevZaTransport(atributi[0], atributi[1], datumTransportovanjaRobe,
                                  atributi[3], atributi[4], avion,
                                  listaRobe, atributi[7])
            
            
                
            
        
    
    
          
            zahteviZaTransport.append(z)
            
def dodeliRobu(rob):
    for r in roba:
        if rob == r.oznaka:
            return r
        