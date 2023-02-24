# File: parallelogramma.py - ok
# Date: 20 feb 23
# Note: quarto punto di un parallelogramma

# quarto punto del parallelogramma di vertici fra A, B, C
def puntopar(A:Point, B:Point, C:Point) -> Point:
    return sym(B,med(A,C))

#---- main ----
A = Point(INPUT,name='A',color='grey',state=DRAGABLE)
B = Point(INPUT,name='B',node=A,color='grey',state=DRAGABLE)
Segment(A,B,color='gray',state=VISIBLE,width=MEDIUM)
C = Point(INPUT,name='C',node=B,color='grey',state=DRAGABLE) 
Segment(B,C,color='gray',state=VISIBLE,width=MEDIUM)
D = puntopar(A,B,C).config(color='red',state=VISIBLE)
Segment(C,D,color='gray',state=VISIBLE,width=MEDIUM)
Segment(D,A,color='gray',state=VISIBLE,width=MEDIUM)
show('D = ',D) #P==Q

#Q = puntopar(C,D,puntopar(A,B,D)).config(color='blue',state=VISIBLE)  #coincide con D
#show('Q = ',Q)
