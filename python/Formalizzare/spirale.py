# File: spirale - ok
# Date: 22 feb 23
# Note: spirale quadrata

from lsistemi import *

assioma = 'X'
regole = {'X':'XY+','Y':'YF'}
disegno = sostituisci(assioma,regole,16)
#print("D=",disegno)
angolo, passo = 90, .2
disegna(disegno,angolo,passo)
