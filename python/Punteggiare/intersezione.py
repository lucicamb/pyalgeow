# File: intersezione.py 
# Date: 20 feb 23 
# Note: intersezione fra due rette con operazioni sui punti
#       (algoritmo iterativo approssimato)
#       funziona ma servono molte iterazioni se le due rette sono quasi parallele

_cons_color = 'gray' # colore delle linee di costruzione

# proiezione del punto P sulla retta AB 
def pro(P:Point, A:Point, B:Point) -> Point:
    return med(P,sym(P,A,B))   

# intersezione fra due rette AB e CD
def intersezione(A:Point, B:Point, C:Point, D:Point) -> Point:  
    #P = A #Point(RANDOM,on=Line(A,B))
    P = (A+B+C+D)/4 #baricentro dei punti base
    for k in range(3):
        P = pro(P,C,D)
        P = pro(P,A,B)
    return P

#---- main ----
A = Point((1,1),name='A',color='grey',state=DRAGABLE)
B = Point((4,2),name='B',color='grey',state=DRAGABLE)
C = Point((4,0),name='C',color='grey',state=DRAGABLE)
D = Point((5,-1),name='D',color='grey',state=DRAGABLE)
Line(A,B,color='orange',state=VISIBLE,width=MEDIUM)
Line(C,D,color='orange',state=VISIBLE,width=MEDIUM)

K = intersezione(A,B,C,D)
K.config(name='K',color='blue',width=3,state=VISIBLE)
show('intersezione K = ',K) 

'''
P = pro(C,A,B)
P.config(name='P',color='red',width=3,state=VISIBLE)
write('proiezione di C su AB = ',P) 
'''

