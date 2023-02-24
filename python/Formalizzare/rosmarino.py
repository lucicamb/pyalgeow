# File: rosmarino - ok
# Date: 22 feb 23
# Note: pianta di rosmarino

from lsistemi import *

assioma = 'F'
regole = {'F':'FF+[+F-F-F]-[-F+F+F]'}
disegno = sostituisci(assioma,regole,4)  
#print("D=",disegno)
angolo, passo = 20, .2
left(90)
hide() #per velocizzare il disegno
setcol('green4')
disegna(disegno,angolo,passo)
