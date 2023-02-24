# File: triangolosierpinsky - ok
# Date: 22 feb 23
# Note: triangolo Sierpinsky

from lsistemi import *

assioma = 'F+G+G'
regole = {'F':'F+G-F-G+F','G':'GG'}   
home()
left(180)
disegno = sostituisci(assioma,regole,4)
#print("D=",disegno)
angolo, passo = 120, .2
disegna(disegno,angolo,passo)
