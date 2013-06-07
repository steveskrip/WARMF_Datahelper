import csv
import os
import sys

dir = os.path.dirname(__file__)

def cdir(nfile):
    return os.path.join(dir, nfile)

files = [("Hydrology",.111),("Air Quality",.111),("Observed Hydrology",111),
        ("Observed Water Quality",111),("Managed Flow",.111),
        ("Point sources",111),("Pictures",111)]


