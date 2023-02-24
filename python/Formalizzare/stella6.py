# File: stella6 - ok
# Date: 22 feb 23
# Note: stella esagonale

from lsistemi import *

assioma = 'X'
regole = {'X':'[F+F++F]+X'}  
disegno = sostituisci(assioma,regole,6)  
#print("D=",disegno)
angolo, passo = 60, 1   
hide() #per velocizzare il disegno
setcol('black')
disegna(disegno,angolo,passo)
