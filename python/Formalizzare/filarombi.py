# File: filarombi - ok
# Date: 22 feb 23
# Note: fila di rombi

from lsistemi import *

assioma = 'X'
#regole = {'X':'F+F+F-F-FX'}  #rombi [1] ok anche cosi'
regole = {'X':'TX','T':'F+F+F-F-F'}  #rombi [1] ?
#regole = {'X':'ABX','A':'CC','B':'DD','C':'F+','D':'F-',}  #cosi' no  [1bis]
#regole = {'X':'F+X'}  #esagono [2]
disegno = sostituisci(assioma,regole,6)  
#print("D=",disegno)
angolo, passo = 120, 1   #per [1]
#angolo, passo = 60, 1    #per [2]
hide() #per velocizzare il disegno
setcol('black')
right(120)
disegna(disegno,angolo,passo)
