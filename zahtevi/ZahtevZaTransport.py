'''
Created on Jun 12, 2016

@author: Vasic
'''

class ZahtevZaTransport(object):
    '''
    Zahtev za transport robe
    '''


    def __init__(self, identifikacioniKodZahteva, datumKreiranjaZahteva,
                 datumTransportovanjaRobe, odrediste, 
                 identifikacioniKodPotrazitelja, avion,
                 listaRobe, statusZahteva):
        '''
        Constructor
        '''
        
        self.identifikacioniKodZahteva = identifikacioniKodZahteva
        self.datumKreiranjaZahteva = datumKreiranjaZahteva
        self.datumTransportovanjaRobe = datumTransportovanjaRobe
        self.odrediste = odrediste
        self.identifikacioniKodPotrazitelja = identifikacioniKodPotrazitelja
        self.avion = avion
        self.listaRobe = listaRobe
        self.statusZahteva = statusZahteva
        


