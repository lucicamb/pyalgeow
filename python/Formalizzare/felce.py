# File: felce.py - ok
# Date: 22 feb 23
# Note: pianta di felce

from lsistemi import *

assioma = 'X'
#regole = {'X':'F[+X]F[-X]+X','F':'FF'}  #fig.1
regole = {'X':'F[+X][-X]FX','F':'FF'}  #fig.2 - prezzemolo
disegno = sostituisci(assioma,regole,7)  
print("D=",disegno)
#angolo, passo = 18, .1  #fig.1
angolo, passo = 14, .1   #fig.2
left(90)
hide() #per velocizzare il disegno
setcol('green4')
disegna(disegno,angolo,passo)
