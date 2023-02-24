# File: main_pyalgeo.py - ok
# Date: 23 gen 23
# Note: esempio di un programma Python che usa le librerie PyAlGeo

# logo del programma:
def logo():
    setwidth(THICK)
    setcol('orange')
    x = 1
    y = 1
    k = 1
    setpos(x,y)
    setang(90)
    forward(2*k)
    right(90)
    forward(k*.9)
    right(90)
    forward(k)
    right(90)
    forward(k*.9)
    x += 1
    #y += 1
    setpos(x,y)
    setang(0)
    forward(k*.9)
    left(90)
    forward(2*k)

#---- import della libreria PyAlGeo ----
import sys
sys.path.insert(0,"./pyalgeo.zip")  # inserisce pyalgeo.zip nel sys.path
#sys.path.insert(0,"../python/modules/pyalgeo.zip")  # inserisce pyalgeo.zip nel sys.path
#import pyalgeo
from pyalgeo import *
#from kinter import *

#---- creazione finestra grafica ----
aginit() #esegue init.py

#---- main ----
grid()   # reticolo del piano
#execprog('/Tracciare/tangenti.py') #nella cartella ../python

logo()

'''
# grafica della tartaruga:
col = ['black','blue','green','red']
penup()
setpos(1,1)
pendown()
P = pos()
forward(1)
left(90)
forward(2)
Q = pos()
move(P)
draw(Q)
show()

# spirale:
for i in range(25):
   forward(0.2*i)
   left(90)
   setcol(col[i % len(col)])

# quadrato con move/draw/close:
col = ['black','blue','green','red']
penup()
setpos(1,1)
pendown()
forward(1)
show()

# grafo completo:
a = [] # array dei vertici
move((-2,-2))
lato = 2
nver = 7
penup()
for i in range(nver):
    a += [pos()]
    forward(lato)
    left(360/nver)
pendown()
setcol('red')
for i in range(nver):
    for j in range(i,nver):
        move(a[i])
        draw(a[j])
'''


