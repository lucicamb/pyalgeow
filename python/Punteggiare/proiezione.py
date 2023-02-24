# File: proiezione.py - ok
# Date: 20 feb 23
# Note: proiezione e perpendicolarita' fra rette

# proiezione del punto P sulla retta AB 
def pro(P:Point, A:Point, B:Point) -> Point:
    return med(P,sym(P,A,B))   

# distanza del punto P dalla retta AB 
def distpr(P:Point, A:Point, B:Point) -> Value:
    return dist(P,pro(P,A,B))   

# perpendicolarita' fra le due rette AB e CD 
def per(A:Point, B:Point, C:Point, D:Point) -> bool:
    return equal(pro(C,A,B),pro(D,A,B))

# isometria dei due segmenti AB e CD
def iso(A:Point, B:Point, C:Point, D:Point) -> bool:
    return dist(A,B)==dist(C,D)

#---- main ----
A = Point((1,1),name='A',color='grey',state=DRAGABLE)
B = Point((4,2),name='B',color='grey',state=DRAGABLE)
C = Point((2,4),name='C',color='grey',state=DRAGABLE)
D = Point((3,1),name='D',color='grey',state=DRAGABLE)
P = Point((6,4),name='P',color='blue',state=DRAGABLE)
Q = pro(P,A,B).config(name='Q',color='red',state=VISIBLE) #proiezione
Line(A,B,color='red',state=DRAGABLE,width=MEDIUM)
Line(C,D,color='red',state=DRAGABLE,width=MEDIUM)
show('A = ',A) 
show('B = ',B) 
show('C = ',C) 
show('D = ',D)
show('P = ',P)
show('Q = ',Q)
show('dist(P,AB) = ',distpr(P,A,B))
p = per(A,B,C,D)
show('AB perpendicolare CD = ',p)


