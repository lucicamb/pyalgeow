# File: hilbert.py - ok
# Date: 22 feb 23
# Note: curva di Hilbert

from lsistemi import *

assioma = 'L'
regole = {'L':'+RF-LFL-FR+','R':'-LF+RFR+FL-'}
disegno = sostituisci(assioma,regole,4)  
#print("D=",disegno)
angolo, passo = 90, .3
hide() #per velocizzare il disegno
setcol('black')
left(90)
disegna(disegno,angolo,passo)


