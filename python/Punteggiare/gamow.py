# File: gamow.py - ok
# Date: 21 mag 22
# Note: problema di gamow

#from kinter import * 

#kgrid()

#M = Point((6,-2),name='M',color='orange',state=DRAGABLE)    # ok cosi' ...
M = Point(6,-2,name='M',color='orange',state=DRAGABLE)       # ed anche cosi' [28giu21]
P = Point((10,1),name='P',color='orange',state=DRAGABLE)
Q = Point((3,-1),name='Q',color='orange',state=DRAGABLE)
Segment(M,P,color='brown',state=SENSIBLE)
Segment(M,Q,color='brown',state=SENSIBLE)

#P1 = Rot(P,M,torad(90)).config(name='P1',width=3,color='red')
#P2 = Rot(Q,M,torad(-90)).config(name='P2',width=3,color='red')
#P1 = Rot(P,M,math.radians(90)).config(name='P1',width=3,color='red')
#P2 = Rot(Q,M,math.radians(-90)).config(name='P2',width=3,color='red')
P1 = Rot(P,M,math.radians(90)).config(name='P1',color='red',state=VISIBLE)
P2 = Rot(Q,M,math.radians(-90)).config(name='P2',color='red',state=VISIBLE)
Segment(P1,P2,color='orange')
Segment(P,P1,color='brown')
Segment(Q,P2,color='brown')
T = (P1+P2)/2
T.config(name='T',width=3,color='blue',state=DRAGABLE) #OK: NON E' DRAGGABILE 

