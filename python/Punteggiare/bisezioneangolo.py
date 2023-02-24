# File: bisezioneangolo.py - ok
# Date: 20 feb 23
# Note: bisettrice di un angolo

# punto che insividua la bisettrice dell'angolo AVB
def biseca(A:Point,V:Point,B:Point) -> Point:
    a = dist(A,V)
    b = dist(B,V)
    k = a/(a+b)
    K = hom(A,B,k)
    return K

#---- main ----
V = Point(INPUT,name='V',color='brown',state=DRAGABLE) 
r = Ray(INPUT,node=V,state=DRAGABLE,color='brown')
s = Ray(INPUT,node=V,state=DRAGABLE,color='brown')
A = tail(r)
B = tail(s)
K = biseca(A,V,B)
b = Ray(V,K,color='orange',state=VISIBLE)
show('b=',b)
