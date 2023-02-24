# File: allineamento.py - ok 
# Date: 20 feb 23
# Note: proiezione, allineamento e parallelismo di punti

# proiezione del punto P sulla retta AB 
def pro(P:Point, A:Point, B:Point) -> Point:
    return med(P,sym(P,A,B))   

# test di retta AB perpendicolare a CD 
def per(A:Point, B:Point, C:Point, D:Point) -> bool:
    #return pro(C,A,B) == pro(D,A,B)  #NO
    return equal(pro(C,A,B),pro(D,A,B))

# allineamento di tre punti A, B, C 
def ali(A:Point, B:Point, C:Point) -> bool:
    #return par(A,B,B,C)  # ric. infinita se par definito con ali 
    return equal(C,sym(C,A,B))   #ok [con  C==sym(C,A,B)  non funziona]

# allineamento di tre punti A, B, C usando dist 
def ali2(A:Point, B:Point, C:Point) -> Value:
    a = dist(B,C)
    b = dist(A,C)
    c = dist(A,B)
    #m = max(a,b)
    #m = max(m,c)
    m = max(max(a,b),c)
    n = a+b+c-m
    #return m  #==n    #ok ma MOLTO LENTO a causa della write!!!! SISTEMATO!
    return m==n    #cosi' ok! PERCHE?????????????

# predicato di parallelismo: AB || CD - ok 7lug22 - NON VA SE C=A
# M1=vecchio P, M2=vecchio Q
def par(A:Point, B:Point, C:Point, D:Point) -> bool:
    '''
    Segment(A,C,color='orange',state=VISIBLE)
    Segment(B,D,color='orange',state=VISIBLE)
    Segment(A,B,color='orange',state=VISIBLE)
    Segment(C,D,color='orange',state=VISIBLE)
    Segment(A,D,color='orange',state=VISIBLE)
    Segment(B,C,color='orange',state=VISIBLE)
    '''
    
    #metodo 0 - ok 8dic22
    return ali(C,D,sym(B,med(A,C)))
      
    ''' metodo 1
    M1 = med(A,B).config(color='red',state=VISIBLE)
    #M2 = x4p(A,B,x4p(A,D,B,C),x4p(A,C,B,D)).config(color='blue',state=VISIBLE)
    P = x4p(A,D,B,C).config(color='green',state=VISIBLE)
    Q = x4p(A,C,B,D).config(color='blue',state=VISIBLE)
    Segment(A,P,color='orange',state=VISIBLE)
    Segment(B,P,color='orange',state=VISIBLE)
    write('P = ',P) 
    write('Q = ',Q)
    M2 = x4p(A,B,P,Q).config(color='black',state=VISIBLE)
    write('M1 = ',M1) 
    write('M2 = ',M2)
    return uguale(M1,M2)
    '''
    
    '''
    #metodo 2 - sembra ok!! - cfr. dim. alternativa (nelle Note, cap. PUNTEGGIARE
    M = med(A,B).config(color='red',state=VISIBLE)
    N = med(C,D).config(color='red',state=VISIBLE)
    Q = x4p(A,C,B,D).config(color='blue',state=VISIBLE)
    Q1 = x4p(A,C,M,N).config(color='green',state=VISIBLE)
    write('Q = ',Q) 
    write('Q1 = ',Q1)
    return equal(Q,Q1)
    '''


    
#---- main ----

'''
#---- test proiezione ---- ok 17gen23
A = Point((1,1),name='A',color='grey',state=DRAGABLE)
B = Point((4,2),name='B',color='grey',state=DRAGABLE)
Line(A,B,color='orange',state=VISIBLE)
P = Point((3,4),name='P',color='grey',state=DRAGABLE)
show('A = ',A) 
show('B = ',B) 
show('P = ',P) 
Q = pro(P,A,B)
Q.config(name='Q',color='red',state=VISIBLE)
'''


'''
#---- test di perpendicolarita' ---- ok 20feb23
A = Point((1,1),name='A',color='grey',state=DRAGABLE)
B = Point((4,2),name='B',color='grey',state=DRAGABLE)
C = Point((2,2),name='C',color='grey',state=DRAGABLE)
D = Point((1,5),name='D',color='grey',state=DRAGABLE)
Line(A,B,color='orange',state=VISIBLE,width=MEDIUM)
Line(C,D,color='orange',state=VISIBLE,width=MEDIUM)
perpendicolare = per(A,B,C,D)
show('AB perpendicolare CD = ',perpendicolare) 
'''



'''
#---- test allineamento ---- ok 20feb23
A = Point((1,1),name='A',color='grey',state=DRAGABLE)
B = Point((2,2),name='B',color='grey',state=DRAGABLE)
C = Point((3,3),name='C',color='grey',state=DRAGABLE)
show('A = ',A) 
show('B = ',B) 
show('C = ',C) 
a = ali(A,B,C)
show('ali(A,B,C) = ',a)
show('ali2(A,B,C) = ',ali2(A,B,C)) #sensibilita' diversa da ali
'''

'''
#---- test parallelismo AB || CD ---- ok 20feb23
A = Point((0,0),name='A',color='grey',state=DRAGABLE)
B = Point((6,0),name='B',color='grey',state=DRAGABLE)
C = Point((5,3),name='C',color='grey',state=DRAGABLE)
#C = Point((0,0),name='C',color='grey',state=DRAGABLE)
D = Point((2,3),name='D',color='grey',state=DRAGABLE)
#Segment(A,C,color='orange',state=VISIBLE)
#Segment(B,D,color='orange',state=VISIBLE)
Line(A,B,color='orange',state=VISIBLE)
Line(C,D,color='orange',state=VISIBLE)
#Segment(A,D,color='orange',state=VISIBLE)
#Segment(B,C,color='orange',state=VISIBLE)
show('A = ',A) 
show('B = ',B) 
show('C = ',C) 
show('D = ',D) 
p = par(A,B,C,D)
#print('tipo di pret =',type(p))    #<class 'graph.DOltDO'>
show('AB parallelo CD = ',p)
'''


#''' 
#---- test di parallelogramma ABCD ---- ok 20feb23
#A = Point(INPUT,name='A',color='grey',state=DRAGABLE)
#B = Point(INPUT,name='B',color='grey',state=DRAGABLE)
#C = Point(INPUT,name='C',color='grey',state=DRAGABLE) 
#D = Point(INPUT,name='D',color='grey',state=DRAGABLE)
A = Point((1,1),name='A',color='grey',state=DRAGABLE)
B = Point((4,-2),name='B',color='grey',state=DRAGABLE)
C = Point((5,0),name='C',color='grey',state=DRAGABLE)
D = Point((2,3),name='D',color='grey',state=DRAGABLE)
show('A = ',A) 
show('B = ',B) 
show('C = ',C) 
show('D = ',D) 
Segment(A,B,color='orange',state=VISIBLE)
Segment(B,C,color='orange',state=VISIBLE)
Segment(C,D,color='orange',state=VISIBLE)
Segment(D,A,color='orange',state=VISIBLE)
parallelogramma1 = par(A,B,C,D) and par(A,D,B,C)
show('ABCD parallelogramma1 = ',parallelogramma1)
parallelogramma2 = iso(A,B,C,D) and iso(A,D,B,C)
show('ABCD parallelogramma2 = ',parallelogramma2)
#'''






