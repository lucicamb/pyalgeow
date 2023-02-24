# File: test_op_punti.py - ok
# Date: 8 feb 23
# Note: operazioni sui punti - cfr cap. Punteggiare
#       vengono utilizzate le funzioni di base: med, sym, (A,B) 

#       ESTRARRE QUALCHE ES. SIGNIFICATIVO [8feb23]

# punto sul segmento AB, d unita' oltre B
def oltre(A:Point, B:Point, d:float) -> Point:
    #return hom(A,B,1+1/dist(A,B))  #ERR
    #return hom(A,B,1.+1./dist(A,B))
    #t = 1.1+dist(A,B)  #prova ok
    #t = 1.1-dist(A,B)  #prova ok
    #t = 1.1*dist(A,B)  #prova ok
    #t = 1.1/dist(A,B)  #prova ERR <------------------!!!
    #t = ~dist(A,B)  #prova ok (reciproco: __invert__ in graph.py)
    #t = dist(A,B)/1.1  #prova ok
    
    #t = (dist(A,B)+d)/dist(A,B) #ok
    t = 1+d*~dist(A,B)          #ok
    #t = 1.+d/dist(A,B)           #ERR <----------------- SISTEMABILE?
    return hom(A,B,t) 


# disegna quadrilatero ABCD
def disegna(A:Point, B:Point, C:Point, D:Point) -> None:
    Segment(A,C,color='orange',state=VISIBLE)
    Segment(B,D,color='orange',state=VISIBLE)
    Segment(A,B,color='orange',state=VISIBLE)
    Segment(C,D,color='orange',state=VISIBLE)
    #Segment(A,D,color='orange',state=VISIBLE)
    #Segment(B,C,color='orange',state=VISIBLE)

#------------------ main -------------------

''' 
#---- operazioni algebriche sui punti ---- ok 2gen23
mes = 'input di un punto ...'
A = Point(INPUT,msg=mes,name='A',color='blue',state=DRAGABLE)
A1 = Point(coordy(A),coordx(A),name='A1',color='orange',state=DRAGABLE)
v = coordx(A)*coordy(A)
write('v=',v)
B = Point(INPUT,msg=mes,name='B',color='blue',state=DRAGABLE)
X = (A+B).config(name='A+B',color='red',state=SENSIBLE)
#Y = 1.2 * A
Z = coordx(A) * B
#Y.config(name='Y',color='orange',state=SENSIBLE)
Z.config(name='Z',color='brown',state=SENSIBLE)
setmode(DRAG)
#X.dump('X:')
'''


'''
Y = (A-B).config(name='A-B',color='red',state=SENSIBLE)
#Z = (B+(Point(A)-A)).config(name='Z',color='green',state=SENSIBLE)
Z = (B+Point(A)-A).config(name='Z',color='green',state=SENSIBLE)
W = A+Point(2,2)
W.config(color='red',state=VISIBLE,name='W')
Q = Point(coordx(A)+.5/scale(),coordy(B)-.5/scale())
Q.config(color='orange',state=VISIBLE,name='Q')
t = Text(Q,"abcde...",color='blue') 
'''


''' 
#---- clone di punti ---- ok.. 9ago22
message('input di un punto ...') 
A = Point(INPUT,name='A',color='blue',state=DRAGABLE)

B = Point(INPUT,name='B',color='green',state=DRAGABLE) #appare un attimo verde
B.config(state=INVISIBLE)  #B e la sua label diventano invisibili

C = clone(A)  #clona anche gli attributi grafici
D = Point(B)  #clona solo gli attributi geometrici
D.config(name='D',color='red',state=DRAGABLE)
'''


''' 
#---- test della funzione 'oltre' ---- ok 1ago22
message('input di un punto x ...') 
A = Point(INPUT,name='A',color='blue',state=DRAGABLE)
B = Point(INPUT,name='B',color='blue',state=DRAGABLE)
message('...') # clear
P = oltre(A,B,2).config(color='red',state=DRAGABLE)
'''

'''
# punti con label variabile - PROVA ABBANDONATA [3ago22]
P = Point(INPUT).config(name='',color='green',state=DRAGABLE)
x = coordx(P)
write('x=',x)   
#P.config(name='nuovoP')  #ok
#P.config(name=("P= {0}",x))  #quasi
s = StringVar()
s.set(("P= {0}",x))
#write('s=',s)   
#s.set(x)
t=Text((3,2), "x = {0}",x, color='orange')
#t=Text((3,2),s, color='orange')  #ERR
#write('t=',t)   
#P.config(name=("X = {0}",x))  #statico-fisso
#P.config(name=t._gettext())  #..
#P.config(name=x)  #..
P.config(name=t)  #..
'''

'''
# punti con label variabile - prova [3ago22]: SISTEMARE MEGLIO ...
# QUASI! sistemare il formato; diventa lento in drag ... e si impianta
P = Point(INPUT).config(name='',color='green',state=DRAGABLE)
x = coordx(P)
y = coordy(P)
#write('x=',x)   
#P.config(name='nuovoP')  #ok
#P.config(name=("P= {0}",x))  #quasi
#t=Text((x+1,y), "P({0}",x, color='orange') #ok
#t=Text((x+1,y), "P({0},{1})",(x,y),color='orange',state=DRAGABLE) #ok ma lentissimo
t=Text((x+1,y), "P({0},{1})",(x,y),color='orange') #ok

#format(self._x,".2f")
'''

''' 
#---- test delle funzioni sym ---- ok 18nov22
mes = 'input di un punto ...'
A = Point(INPUT,msg=mes,name='A',color='blue',state=DRAGABLE)
B = Point(INPUT,msg=mes,name='B',color='blue',state=DRAGABLE)
P = sym(A,B).config(color='red',state=DRAGABLE)  #ok
C = Point(INPUT,msg=mes,name='C',color='blue',state=DRAGABLE)
Q = sym(C,A,B).config(color='green',state=DRAGABLE)  #CREA MOLTI DO 18ott22
'''


'''
#---- test funzione ang ---- ok 12dic22
A = Point(INPUT,name='A',color='grey',state=DRAGABLE)
B = Point(INPUT,name='B',color='grey',state=DRAGABLE)
C = Point(INPUT,name='C',color='grey',state=DRAGABLE)
x = ang(A)
y = ang(A,B)
z = ang(A,B,C)
Ray(B,A,color='red',state=VISIBLE)
Ray(B,C,color='red',state=VISIBLE)
write('ang(A) = ',x) 
write('ang(A,B) = ',y) 
write('ang(A,B,C) = ',z) 
'''

''' prova per valori booleani-DataObject - ok
message('input di un punto ...') 
A = Point(INPUT,name='A',color='red',state=DRAGABLE)
B = Point(INPUT,name='B',color='blue',state=DRAGABLE)
message('...') # clear
dis = dist(A,B)
cfr = dist(A,B) < dist(A,O)
#ugu = (A==B)  #ERR: serve fare una classe Point, oppure uguale(A,B)
ugu = A.uguale(B)  #cosi' ok
print('tipo di dis =',type(dis))   #<class 'graph.sqrtDO'>
print('tipo di cfr =',type(cfr))   #<class 'graph.DOltDO'>
print('tipo di ugu = ',type(ugu))  #<class 'graph.DOltDO'>
write('dis = ',dis)
write('cfr = ',cfr)
write('ugu = ',ugu)  
'''

''' 
#---- test intersezione ---- ?? 11lug22 ... DA COMPLETARE
A = Point((0,0),name='A',color='grey',state=DRAGABLE)
B = Point((0,4),name='B',color='grey',state=DRAGABLE)
C = Point((5,4),name='C',color='grey',state=DRAGABLE)
D = Point((2,4),name='D',color='grey',state=DRAGABLE)
r = Line(A,B)
Segment(A,B,color='orange',state=VISIBLE)
Segment(C,D,color='orange',state=VISIBLE)
write('A = ',A) 
write('B = ',B) 
write('C = ',C) 
write('D = ',D)
write('retta AB = ',r) 
P = x4p(A,B,C,D).config(color='red',state=VISIBLE)
write('P = ',P)
#ugu0 = A==B         #no (__eq__ definito in graph)
#write('ugu0 = ',ugu0)
ugu1 = A.uguale(B)  #ok (uguale definito in graph)
write('ugu1 = ',ugu1)
ugu2 = uguale(A,B)  #ok (uguale definito in tkinter)
write('ugu2 = ',ugu2)    
'''


'''
#---- test di comparazione fra punti ---- ok 12lug22
A = Point((0,0),name='A',color='grey',state=DRAGABLE)
B = Point((2,1),name='B',color='grey',state=DRAGABLE)
ugu1 = A==B     #di tipo bool (serve fare una classe Point in kinter.py)
ugu2 = A.uguale(B)  #definito in graph.py::_PointObject
ugu3 = uguale(A,B)  #definito in kinter.py
#write('ugu1 = ',ugu1)  #ERR perche' ugu1 e' bool
write('ugu2 = ',ugu2)
write('ugu3 = ',ugu3)
'''


''' distanza punto-punto e punto-tarta
A = Point(INPUT,name='A',msg='seleziona un punto...',color='green',state=DRAGABLE) #attende clic
B = Point(INPUT,name='M',msg='seleziona un punto...',color='blue',state=DRAGABLE) #attende clic
dAB1 = A.dist(B)
dAB2 = dist(A,B)
write('dist1(A,B)=',dAB1) #ok
write('dist2(A,B)=',dAB2) #ok
d = dist(A)
write('dist(tarta,A)=',d) #ok
'''


'''
#---- test di alcune proprieta' fra A, B, C ---- ok 07lug22
message('input di un punto ...') 
A = Point(INPUT,name='A',color='grey',state=DRAGABLE)
B = Point(INPUT,name='B',color='grey',state=DRAGABLE)
C = Point(INPUT,name='C',color='grey',state=DRAGABLE) 
message('...') # clear
#P = sym(B,med(A,C)).config(color='red',state=VISIBLE) #par della dispensa
P = x4p(A,med(B,C),B,med(C,A)).config(color='red',state=VISIBLE)
Q = x4p(A,med(B,C),C,med(A,B)).config(color='blue',state=VISIBLE)
write('P = ',P) #P==Q
write('Q = ',Q)
'''

'''
#---- simmetrico di P rispetto alla retta AB ---- ok 02lug22
message('input di un punto ...') 
A = Point(INPUT,name='A',color='blue',state=DRAGABLE)
B = Point(INPUT,name='B',color='blue',state=DRAGABLE)
P = Point(INPUT,name='P',color='green',state=DRAGABLE) 
message('...') # clear
Q = sym(P,A,B).config(color='red',state=VISIBLE)
R = sym(A,B).config(color='orange',state=VISIBLE)
write('Q = ',Q)
write('R = ',R)
'''


'''
#---- intersezione fra 4 punti (2 segmenti) ---- ok 02lug22
message('input di un punto ...') 
A = Point(INPUT,name='A',color='blue',state=DRAGABLE)
B = Point(INPUT,name='B',color='blue',state=DRAGABLE)
C = Point(INPUT,name='C',color='brown',state=DRAGABLE) 
D = Point(INPUT,name='D',color='brown',state=DRAGABLE) 
message('...') # clear
P = inters(A,B,C,D).config(color='red',state=VISIBLE)
write('P = ',P)
'''


'''
#---- calcolo del punto medio e baricentro ---- ok 21mag22
message('input di un punto ...') 
A = Point(INPUT,name='A',color='red',state=DRAGABLE)
B = Point(INPUT,name='B',color='orange',state=DRAGABLE)
C = Point(INPUT,name='C',color='brown',state=DRAGABLE) 
dab = dist(A,B)
message('...') # clear
write('A = ',A)
write('B = ',B)
write('C = ',C)
write('dist(A,B)=',dab)

M1 = (A+B)/2
# sembra che config modifichi lo stato degli elementi vincolanti ...
M1.config(name='M1',color='green',state=SENSIBLE)
write('M1 = ',M1)
M2 = ((A+B+C)/3).config(name='M2',color='blue',state=SENSIBLE)
write('M2 = ',M2)
'''



'''
# cfr. esempio del cap. PUNTEGGIARE 
# non mettere width=4 perche' poi in zoom viene rimesso al default=5
#X = hom(B,(A+C)/2,2).config(name='X',width=4,color='red',state=SENSIBLE)
X = hom(B,(A+C)/2,2).config(name='X',color='red',state=SENSIBLE)
write('X = ',X)

s1 = Segment(A,B).config(color='green',state=SENSIBLE)
s2 = Segment(B,C).config(color='green',state=SENSIBLE)
s3 = Segment(C,X).config(color='green',state=SENSIBLE)
s4 = Segment(A,X).config(color='green',state=SENSIBLE)
'''

'''
#---- solo per test di punti su vincoli non esistenti: ----
T = Point(PARAM,on=t1,param=.5,name='T',color='black',state=SENSIBLE) #per test
for _ in range(5):
    P = Point(RANDOM,on=t2,name='T',color='black',state=SENSIBLE)
'''
