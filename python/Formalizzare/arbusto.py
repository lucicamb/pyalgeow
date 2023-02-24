# File: arbusto.py - ok
# Date: 22 feb 23
# Note: arbusto

from lsistemi import *

assioma = 'F'
regole = {'F':'F[+F]F[-F]'}  #bello
disegno = sostituisci(assioma,regole,5)  
#print("D=",disegno)
angolo, passo = 30, .2
left(90)
hide() #per velocizzare il disegno
setcol('green4')
disegna(disegno,angolo,passo)
