# File: mod_input.py 
# Date: 24 apr 22 - ok
# Note: modulo per operazioni di input in varie modalita'

from kinter import * 

# input di un segmento;
# n1 e n2 sono i nomi dei vertici;
# ritorna un Segment
def input_segmento(n1:str, n2:str, col:str) -> Segment :
    print('---- entrato in mod_input ----')
    A = Point(INPUT,name=n1,color=col,state=DRAGABLE)
    B = Point(INPUT,name=n2,color=col,node=A,state=DRAGABLE)
    return Segment(A,B,color=col,state=DRAGABLE)


# input di un quadrilatero di dato colore;
# costruisce il quadrilatero e ritorna una tupla di 4 punti
def input_quadrilatero(col) -> tuple :
    A = Point(INPUT,state=DRAGABLE,color=col) #.config(color=col)
    B = Point(INPUT,node=A,state=DRAGABLE,color=col) #.config(color=col)
    Segment(A,B,state=DRAGABLE,color=col)
    C = Point(INPUT,node=(A,B),state=DRAGABLE,color=col) #.config(color=col)
    Segment(B,C,state=DRAGABLE,color=col)
    D = Point(INPUT,node=(A,C),state=DRAGABLE,color=col) #.config(color=col)
    Segment(B,C,state=DRAGABLE,color=col)
    Segment(C,D,state=DRAGABLE,color=col)
    Segment(D,A,state=DRAGABLE,color=col)
    return (A,B,C,D)

# input di un poligono di dato colore;
# costruisce il poligono e ritorna la lista dei punti
def input_poligono(col) -> tuple :
    A = Point(INPUT,state=DRAGABLE,color=col) 
    B = Point(INPUT,node=A,state=DRAGABLE,color=col) 
    Segment(A,B,state=DRAGABLE,color=col)
    P = [A,B]
    while True:
        C = Point(INPUT,node=(A,B),state=DRAGABLE,color=col) 
        if dist(C,A)==0:
            Segment(B,C,state=DRAGABLE,color=col)
            break
        Segment(B,C,state=DRAGABLE,color=col)
        B = C 
        P += [C]
    return P

def perimetro_poligono(P:tuple):
    per = dist(P[0],P[len(P)-1])
    for i in range(len(P)-1):
        per += dist(P[i],P[i+1])
    return per
    


#kgrid()


#portare i blocchi che seguono in test_input.py [24apr22]

'''
#input di un Point con nodo su un altro - ok
A = Point(INPUT,state=DRAGABLE).config(name='A',color='red')
B = Point(INPUT,node=A,state=DRAGABLE).config(name='B',color='blue')
#'''

'''
#input di un triangolo A,B,C
A = Point(INPUT,state=DRAGABLE).config(name='A',color='green')
B = Point(INPUT,node=A,state=DRAGABLE).config(name='B',color='green')
s = Segment(A,B,state=DRAGABLE).config(color='green')
#Segment(A,B,state=DRAGABLE).config(color='green')
s.config(name='c')
C = Point(INPUT,node=B,state=DRAGABLE).config(name='C',color='green')
#s = Segment(B,C,state=DRAGABLE).config(color='green')
#s = Segment(C,A,state=DRAGABLE).config(color='green')
Segment(B,C,state=DRAGABLE).config(color='green')
Segment(C,A,state=DRAGABLE).config(color='green')
'''

#C.config(name='C')  #ERR: SIST!!
#Segment(A,C,state=VISIBLE,color='green')          # verde DIVERSO che da sotto:
#Segment(A,C,state=VISIBLE).config(color='green')   # perche'????
#'''


'''
#s = Segment(INPUT,color='green').config(name='s',state=DRAGABLE)
s = Segment(INPUT,color='green',state=DRAGABLE).config(name='s',state=DRAGABLE) #ERR: i vertci non risultano draggabili
f = Circle(head(s),1.5,color='blue',name='E',state=DRAGABLE)
f.config(color='red') #ERR: rende rosso anche il vertice di f: SIST

#---- circ fisso traslabile ----
#c2 = Circle(Point((-1,-1),2)).config(state=DRAGABLE,color='red')
c2 = Circle(Point((-3,-2),color='brown',state=DRAGABLE),2,color='red',state=DRAGABLE)#.config(state=DRAGABLE,color='red')
li = Line(INPUT,color='red',state=DRAGABLE) 
t = Segment(INPUT,on=li,color='green',state=DRAGABLE) #ERR: non impone il vincolo solo per il primo punto
t2 = Segment(INPUT,on=c2,color='blue',state=DRAGABLE)
'''

