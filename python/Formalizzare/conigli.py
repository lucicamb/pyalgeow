# File: conigli.py - ok
# Date: 22 feb 23
# Note: conigli di Fibonacci

from lsistemi import *

assioma = 'F'
#regole = {'F':'G','G':'GF'}  #ok per stringa lineare
#regole = {'F':'G','G':'G[+F]F'}  #..
regole = {'F':'G','G':'F[+F]G'}  #..
#regole = {'F':'F[+F]F'}  #quasi
#regole = {'F':'FF[+F]'}  #no
for k in range(8):
    popolazione = sostituisci(assioma,regole,k)
    write("popolazione="+popolazione)
    #print("popolazione=",popolazione)

disegno = popolazione #ultima generata
angolo, passo = 45, .5
left(90)
disegna(disegno,angolo,passo)
