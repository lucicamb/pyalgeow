# File: in-circo-centro.py - ok
# Date: 20 feb 23
# Note: incentro e circocentro di un triangolo
#       usa l'op. di intersezione fra rette

# proiezione del punto P sulla retta AB 
def pro(P:Point, A:Point, B:Point) -> Point:
    return med(P,sym(P,A,B))   

# distanza del punto P dalla retta AB 
def distpr(P:Point, A:Point, B:Point) -> Value:
    return dist(P,pro(P,A,B))   

# incentro del triangolo ABC 
def incentro(A:Point, B:Point, C:Point) -> Point:
    alfa = dist(A,B) / (dist(A,B)+dist(A,C))
    #show('alfa =',alfa)
    K = hom(B,C,alfa)
    beta = dist(A,B) / (dist(A,B)+dist(B,C))
    #show('beta =',beta)
    L = hom(A,C,beta)
    I = inters(Line(A,K),Line(B,L))
    return I

# circocentro del triangolo ABC 
def circocentro(A:Point, B:Point, C:Point) -> Point:
    M1 = (A+B)/2
    M2 = (B+C)/2
    K1 = rot(M1,A,90)
    K2 = rot(M1,B,90)
    #K1.config(state=VISIBLE,color='green')
    #K2.config(state=VISIBLE,color='green')
    L1 = rot(M2,B,90)
    L2 = rot(M2,C,90)
    #L1.config(state=VISIBLE,color='blue')
    #L2.config(state=VISIBLE,color='blue')
    W = inters(Line(K1,K2),Line(L1,L2))
    return W

#---- main ----
A = Point((1,1),name='A',color='brown',state=DRAGABLE)
B = Point((4,2),name='B',color='brown',state=DRAGABLE)
C = Point((2,4),name='C',color='brown',state=DRAGABLE)
Segment(A,B,color='brown',state=DRAGABLE,width=MEDIUM)
Segment(B,C,color='brown',state=DRAGABLE,width=MEDIUM)
Segment(C,A,color='brown',state=DRAGABLE,width=MEDIUM)

K = circocentro(A,B,C).config(color='red',state=VISIBLE)
show('K = ',K)
c = Circle(K,A)
c.config(state=SENSIBLE,color='orange')

I = incentro(A,B,C).config(color='blue',state=VISIBLE)
show('I = ',I)
d = Circle(I,distpr(I,A,B))
d.config(state=SENSIBLE,color='green')

