# File: usa_Tarta.py - ok
# Date: 23 feb 23
# Note: esempio d'uso della classe di oggetti Tarta

from Tarta import *


#---- main ----
#grid()
P = Point(INPUT,color='red',state=DRAGABLE)

t = Tarta('red')

t.move(Point(-3,-2))
t.draw(Point(1,4))
t.draw(Point(-1,2))
#t.move((-3,-2))
t.forward(2.5)

show('percorso:',t.percorso()) #valore statico
show('npassi:',t.npassi())     #valore dinamico

t.setcol('blue') # ha effetto
t.setcol('green') # non ha effetto
t.poligono(7,3)

#write('distanza:',t.dist(P))
d = t.dpos().dist(P)
show('distanza dinamica:',d)
show('distanza statica:',val(d))

T = t.pos()  #posizione fissa
show('distanza2:',T.dist(P))
D = t.pos()  #posizione dinamica
show('T = ',T)
show('D = ',D)  #posizione dinamica

#circ. di raggio var. che segue la t
c = Circle(D,d,color='blue',state=VISIBLE,width=MEDIUM)

k = 1
for _ in range(100):
    t.forward(k)
    t.left(90)
    k += .1

t.look(P)

   
