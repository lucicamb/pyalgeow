# File: vonkock - ok
# Date: 22 feb 23
# Note: curva di von Kock

from lsistemi import *

assioma = 'F'
regole = {'F':'F-F++F-F'}
disegno = sostituisci(assioma,regole,4)
#print("D=",disegno)
angolo, passo = 60, .2
disegna(disegno,angolo,passo)
