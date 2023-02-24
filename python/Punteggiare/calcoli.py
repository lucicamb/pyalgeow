# File: calcoli.py
# Date: 20 feb 23
# Note: calcoli sui punti, con risultati numerici
#       funziona ma e' molto lento se si trascinano i punti
#       colpa della write del risultato

#from math import sqrt,atan2,atan,sin,cos,pi
#from kinter import *

from costruzioni import *  

# input di un triangolo;
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

# perimetro di un triangolo di dati vertici
def perimetro(A:Point,B:Point,C:Point) -> float :
    return dist(A,B)+dist(A,C)+dist(B,C)

# area del triangolo di dati vertici - formula di Erone
def areaE(A:Point,B:Point,C:Point) -> float:
    a = dist(B,C)
    b = dist(A,C)
    c = dist(A,B)
    p = (a+b+c)/2
    #ris = math.sqrt(p*(p-a)*(p-b)*(p-c))
    ris = (p*(p-a)*(p-b)*(p-c)).sqrt()
    return ris

# area con formula di geometria analitica
def area(A:Point,B:Point,C:Point) -> float:
    xa = coordx(A)
    ya = coordy(A)
    xb = coordx(B)
    yb = coordy(B)
    xc = coordx(C)
    yc = coordy(C)
    a = xa*yb + xc*ya + xb*yc - xc*yb - xb*ya - xa*yc
    return abs(a)/2

# quadrato dell'area del triangolo di dati vertici
# con distm e' un po' piu' veloce, ma l'area non non e' corretta ...
def area2(A:Point,B:Point,C:Point) -> float:
    a = distm(B,C) #distanza manhattan
    b = distm(A,C)
    c = distm(A,B)
    p = (a+b+c)/2
    #ris = math.sqrt(p*(p-a)*(p-  #b)*(p-c))
    ris = p*(p-a)*(p-b)*(p-c)
    #ris = a*b*c #solo per prova: così VELOCE
    #ris = p*(p-a)*b*c #solo per prova: LENTO
    return ris

# test se il punto P e' interno al triangolo ABC
# ok, ma lento nei calcoli (sono DataObjects)
def interno(P:Point,A:Point,B:Point,C:Point) -> bool:
    return (area(A,B,P)+area(B,C,P)+area(A,C,P)) == area(A,B,C)  #ok, veloce
    #return area2(A,B,P)+area2(B,C,P)+area2(A,C,P) < area2(A,B,C) # ok ma lento
    #return areaE(A,B,P)+areaE(B,C,P)+areaE(A,C,P) < areaE(A,B,C) # ok ma lento
    '''
    a1 = area(A,B,P)
    a2 = area(B,C,P)
    a3 = area(A,C,P)
    t = a1+a2+a3
    a = area(A,B,C)
    write('a1=',a1)
    write('a2=',a2)
    write('a3=',a3)
    write('t=',t)
    write('A=',a)
    ris = a==t
    write('ris=',ris)
    return ris   #(a1+a2+a3) < A
    '''
    

# test se 3 punti sono allineati
# ok, ma lento nei calcoli (sono DataObjects)
# 12lug22: velocita' accettabile in drag
def allineati(A:Point,B:Point,C:Point) -> bool:
    return area(A,B,C)==0

# circonferenza circoscritta al triangolo t
def circcirc(t:list) -> Circle:
    #''' ok
    #a1 = asse(t[0],t[1])
    #a2 = asse(t[1],t[2])
    #P = inters(a1,a2)
    #r = dist(P,t[0])
    #return Circle(P,r)
    #'''
    return circonf3p(t[0],t[1],t[2])


#=============================
message('seleziona i 3 vertici del triangolo ...') 
A = Point(INPUT,name='A',color='red',state=DRAGABLE)
B = Point(INPUT,name='B',color='red',state=DRAGABLE)
C = Point(INPUT,name='C',color='red',state=DRAGABLE) 
Segment(A,B,color='red',state=VISIBLE,width=THIN)
Segment(A,C,color='red',state=VISIBLE,width=THIN)
Segment(B,C,color='red',state=VISIBLE,width=THIN)
message('')
Segment(A,B)
Segment(A,C)
Segment(B,C)

message('seleziona il punto da testare se interno...') 
P = Point(INPUT,name='P',color='blue',state=DRAGABLE)
message('')
dentro = interno(P,A,B,C)
show('interno=',dentro)  #<-- questa write rallenta (molto se area con Erone) !!!! Perche'??????

#t = dentro
#write('t=',t)  #ancora lento

#write('interno=',interno(P,A,B,C))  #ancora lento
Text((5,5),"interno = {0}",dentro,color='brown').config(state=DRAGABLE) #ancora lento



    

   
