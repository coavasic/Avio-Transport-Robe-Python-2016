'''
Created on Jun 6, 2016

@author: Lazar-PC
'''
from datetime import datetime

formatDatuma="%d.%m.%Y"

def parsirajDatum(datum):
    return datetime.strptime(datum,formatDatuma)

def formatirajDatum(datum):
    return datum.strftime(formatDatuma)