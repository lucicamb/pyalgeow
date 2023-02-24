# File: Poligono.py
# Date: 25 nov 22
# Note: classe dei poligoni - DA COMPLETARE

#from math import sqrt,atan2,atan,sin,cos,pi
from kinter import *
#from costruzioni import *  

#poligono individuato da una lista di punti (vertici)
class Poligono:
 
    # poligono da un array di punti
    def __init__(self,a:list,color,width,state):
        self._a = a
        for i in range(len(a)-1):
            Segment(a[i],a[i+1],state=state,color=color,width=width)
        Segment(a[0],a[len(a)-1],state=state,color=color,width=width)    
        
    ''' DA SISTEMARE
    # input di un triangolo in modalita' rubberbanding
    #def __init__(self,color='black',vertices=('','','')):
    def __init__(self,vertices=('','','')):
        #print('------ in Triangolo.py ------')
        A = Point(INPUT,state=DRAGABLE,name=vertices[0]) 
        B = Point(INPUT,node=A,state=DRAGABLE,name=vertices[1])
        s = Segment(A,B,state=DRAGABLE,color='brown') 
        C = Point(INPUT,node=(A,B),state=DRAGABLE,name=vertices[2])
        Segment(B,C,state=DRAGABLE,color='brown')
        Segment(C,A,state=DRAGABLE,color='brown')
        
        self._a = A
        self._b = B
        self._c = C
    '''
    def perimetro(self):
        return 1.23 #provvisorio

def fperimetro(t:Poligono):
    return 4.56 #provvisorio


#=============================
if __name__ == '__main__':
    '''
    '''
 



    

   
