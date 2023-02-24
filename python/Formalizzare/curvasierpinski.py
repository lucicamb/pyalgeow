# File: curvasierpinsky - ok
# Date: 22 feb 23
# Note: curva di Sierpinsky

from lsistemi import *

assioma = 'F--XF--F--XF'
regole = {'X':'XF+F+XF--F--XF+F+X'}  
disegno = sostituisci(assioma,regole,3)  
#print("D=",disegno)
angolo, passo = 45, .5   
hide() #per velocizzare il disegno
setcol('black')
disegna(disegno,angolo,passo)
