# File: mod_triangolo.py - ok
# Date: 19 ago 22
# Note: modulo di funzioni sui triangoli.

#from math import sqrt,atan2,atan,sin,cos,pi
#from kinter import *

from costruzioni import *  

# input di un triangolo in modalita' rabber-band;
# ritorna la lista dei punti acquisiti in input
# vengono impostati gli attributi attuali (colore, stato, ...)
def input_triangolo(vertices=['','','']) -> list :
    #print('---- entrato in mod_input ----')
    A = Point(INPUT,state=DRAGABLE,name=vertices[0]) 
    B = Point(INPUT,node=A,state=DRAGABLE,name=vertices[1])
    s = Segment(A,B,state=DRAGABLE) 
    C = Point(INPUT,node=(A,B),state=DRAGABLE,name=vertices[2])
    Segment(B,C,state=DRAGABLE)
    Segment(C,A,state=DRAGABLE)
    return [A,B,C]

def perimetro(t:list) -> float :
    return dist(t[0],t[1])+dist(t[1],t[2])+dist(t[2],t[0])

#'''
# area del triangolo di dati vertici
def area(t:list) -> float:
    a = dist(t[1],t[2])
    b = dist(t[0],t[2])
    c = dist(t[0],t[1])
    p = (a+b+c)/2
    #ris = math.sqrt(p*(p-a)*(p-b)*(p-c))
    ris = (p*(p-a)*(p-b)*(p-c)).sqrt()
    return ris
#'''

# circonferenza circoscritta al triangolo t
def circcirc(t:list) -> Circle:
    #''' ok
    #a1 = asse(t[0],t[1])
    #a2 = asse(t[1],t[2])
    #P = inters(a1,a2)
    #r = dist(P,t[0])
    #return Circle(P,r)
    #'''
    return circonf3punti(t[0],t[1],t[2])


'''
def incentro(t:Triangolo) -> Point:  
    alfa = dist(t._a,t._b)/((dist(t._a,t._b)+dist(t._a,t._c)))
    H = hom(t._b,t._c,alfa)
    beta = dist(t._b,t._a)/((dist(t._b,t._a)+dist(t._b,t._c)))
    K = hom(t._a,t._c,beta)
    I = inters(Line(t._a,H),Line(t._b,K))
    #r = dist(C,piede(C,Line(t._a,t._b)))
    return I #Circle(C,r) #C #H #K   con C va, con Circle da ERRORE

def circinscr(t:Triangolo) -> Circle:
    I = incentro(t)
    r = dist(I,piede(I,Line(t._a,t._b)))
    return Circle(I,r) 
'''    

'''
#=============================
if __name__ == '__main__':
    t = input_triangolo()
    a = area(t)
    write('area triangolo =',a)
'''
message('selezionate i 3 vertici del triangolo ...')
t = input_triangolo()
a = area(t)
write('area triangolo =',a)
c = circcirc(t)
c.config(color='red')
 



    

   
