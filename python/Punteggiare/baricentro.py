# File: baricentro.py - ok
# Date: 15 set 22
# Note: calcolo del baricentro K di un triangolo ABC

from costruzioni import *

# baricentro K del triangolo ABC
def baricentro1(A:Point,B:Point,C:Point) -> Point:  
    M = medio(A,B)
    N = medio(A,C)
    a = Line(C,M).config(color='gray',state=VISIBLE,width=THIN,expand=False)
    b = Line(B,N).config(color='gray',state=VISIBLE,width=THIN,expand=False)
    K = inters(a,b) #.config(color='green',state=VISIBLE)
    return K

# baricentro K del triangolo ABC
def baricentro2(A:Point,B:Point,C:Point) -> Point:  
    #return (A+B+C)/3
    return hom(A,hom(B,C,1/2),2/3)

#---- main ----

#input del triangolo:
col = 'red' #colore del triangolo
A = Point(INPUT,color=col,state=DRAGABLE,name='A') 
B = Point(INPUT,node=A,color=col,state=DRAGABLE,name='B')
s = Segment(A,B,state=DRAGABLE,color=col,width=MEDIUM) 
C = Point(INPUT,node=(A,B),color=col,state=DRAGABLE,name='C')
Segment(B,C,state=DRAGABLE,color=col,width=MEDIUM)
Segment(C,A,state=DRAGABLE,color=col,width=MEDIUM)

#K = baricentro1(A,B,C)
K = baricentro2(A,B,C)
K.config(color='green',state=VISIBLE)




''' calcolo mediante operazioni ibride - ok
#punti medi dei lati
L = (B+C)/2
M = (A+C)/2
N = (A+B)/2

#mediane
ma = Segment(A,L,color='gray',state=VISIBLE,width=THIN)
mb = Segment(B,M,color='gray',state=VISIBLE,width=THIN)
mc = Segment(C,N,color='gray',state=VISIBLE,width=THIN)

#intersezione di 2 mediane:
K = inters(ma,mb).config(color='green',state=VISIBLE)
'''
