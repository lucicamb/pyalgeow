# File: angoloacuto.py - ok
# Date: 13 dic set 22
# Note: esempi sugli angoli

# test se l'angolo PVQ di vertice V e' acuto
def acuto(P:Point,V:Point,Q:Point) -> bool:
    a = dist(P,V)
    b = dist(V,Q)
    c = dist(P,Q)
    circ = Circle((P+Q)/2,P,state=VISIBLE,color='red',width=THIN) #per controllo visivo
    
    '''
    write('a=',a)
    write('b=',b)
    write('c=',c)
    a2 = a*a
    b2 = b*b
    a2pb2 = a2+b2
    c2 = c*c
    write('a2=',a2)
    write('b2=',b2)
    write('a2pb2=',a2+b2)
    write('c2=',c2)
    eq = (c*c) == ((a*a)+(b*b)) 
    ne = (c*c) != ((a*a)+(b*b)) 
    lt = (c*c)  < ((a*a)+(b*b)) 
    gt = (c*c)  > ((a*a)+(b*b))
    le = (c*c) <= ((a*a)+(b*b)) 
    ge = (c*c) >= ((a*a)+(b*b))     
    write('eq=',eq)
    write('ne=',ne)
    write('lt=',lt)
    write('gt=',gt)
    write('le=',le)
    write('ge=',ge)
    '''
    
    return (c*c) < ((a*a)+(b*b))

#---- main ----

#---- test di angolo acuto ---- ok 13dic22
V = Point(INPUT,name='V',color='brown',state=DRAGABLE) 
r1 = Ray(INPUT,node=V,state=DRAGABLE,color='brown')
r2 = Ray(INPUT,node=V,state=DRAGABLE,color='brown')
A = tail(r1)
B = tail(r2)
acu = acuto(A,V,B)
write('acuto=',acu)

#c = Cond(acu,'red','blue') #oggetto condizionale
#V.config(color=c)
#'''



