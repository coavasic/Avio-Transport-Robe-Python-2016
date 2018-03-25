'''
Created on May 16, 2016

@author: Vasic
'''

from ucitati import entitete

def pronadjiAvione(oznaka):
    """Pronalazi sve avione za odredjeni hangar"""
    listaAviona = []
    for avion in entitete.avioni :
        if avion.hangar is not None:
            if oznaka == avion.hangar.oznaka:
                listaAviona.append(avion)
    return listaAviona
            
     
def pronadjiProstorZaTeret(oznaka, prostoriZaTeret):
    """Pronalazi sve prostore za teret po oznaci aviona"""
    listaProstoraZaTeret = []
    for prostorZaTeret in prostoriZaTeret:
        if oznaka == prostorZaTeret.avion:
            listaProstoraZaTeret.append(prostorZaTeret)
    
    return listaProstoraZaTeret


def pronadjiRobu(oznaka, robe):
    """Pronalazi svu robu po oznaci prostora za teret"""
    
    listaRoba = []
    
    for roba in robe:
        if oznaka == roba.prostorZaTeret:
            listaRoba.append(roba)
    
    return listaRoba

