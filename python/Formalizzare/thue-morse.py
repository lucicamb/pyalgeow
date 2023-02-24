# File: thue-morse.py - ok
# Date: 22 feb 23
# Note: successione di Thue-Morse

from lsistemi import *

#assioma = '0'
#regole = {'0':'01','1':'10'}  #..
assioma = '+'
regole = {'+':'+F','F':'F+'}  #..
for k in range(12):
    stringa = sostituisci(assioma,regole,k)
    write("stringa="+stringa)
    #print("stringa=",stringa)


disegno = stringa #ultima generata
angolo, passo = 120, .2
right(210)
disegna(disegno,angolo,passo)

