# File: drago - ok
# Date: 22 feb 23
# Note: curva del drago

from lsistemi import *

assioma = 'FX'
regole = {'X':'X+YF+', 'Y':'-FX-Y'}
disegno = sostituisci(assioma,regole,8)
angolo, passo = 90, .2
#print("D=",disegno)
disegna(disegno,angolo,passo)


