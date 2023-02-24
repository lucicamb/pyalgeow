# File: Triangolo.py
# Date: 25 nov 22
# Note: classe dei triangoli
#       circiscr e' un po' lento; provare con dist(Punto, retta) [17mag22]

#from math import sqrt,atan2,atan,sin,cos,pi
#from kinter import *
from costruzioni import *  

class Triangolo:
    "triangolo individuato dai 3 vertici"

    # triangolo di 3 dati vertici
    def __init__(self, A:Point, B:Point, C:Point):
        self._a = A
        self._b = B
        self._c = C

    # input di un triangolo in modalita' rubberbanding
    #def __init__(self,color='black',vertices=('','','')):
    #def __init__(self,vertices=('','','')):
    def __init__(self,vertices=('','',''),color='brown',state=DRAGABLE,width=MEDIUM):
        #print('------ in Triangolo.py ------')
        A = Point(INPUT,state=state,name=vertices[0]) 
        B = Point(INPUT,node=A,state=state,name=vertices[1])
        s = Segment(A,B,state=state,color=color,width=width) 
        C = Point(INPUT,node=(A,B),state=state,name=vertices[2])
        Segment(B,C,state=state,color=color,width=width)
        Segment(C,A,state=state,color=color,width=width)
        
        self._a = A
        self._b = B
        self._c = C

    def perimetro(self):
        return dist(self._a,self._b)+dist(self._b,self._c)+dist(self._c,self._a)
       

def fperimetro(t:Triangolo):
    return dist(t._a,t._b)+dist(t._b,t._c)+dist(t._c,t._a)

#formula di Erone
def xarea(t:Triangolo) -> float:
    a = dist(t._b,t._c)
    b = dist(t._a,t._c)
    c = dist(t._a,t._b)
    p = (a+b+c)/2
    #ris = math.sqrt(p*(p-a)*(p-b)*(p-c))
    ris = (p*(p-a)*(p-b)*(p-c)).sqrt()
    return ris

#formula di geometria analitica
def area(t:Triangolo) -> float:
    xa = coordx(t._a)
    ya = coordy(t._a)
    xb = coordx(t._b)
    yb = coordy(t._b)
    xc = coordx(t._c)
    yc = coordy(t._c)
    area = xa*yb + xc*ya + xb*yc - xc*yb - xb*ya - xc*ya
    return area/2
    
def circcirc(t:Triangolo) -> Circle:
    a1 = asse(t._a,t._b)
    a2 = asse(t._b,t._c)
    C = inters(a1,a2)
    r = dist(C,t._a)
    return Circle(C,r)

# incentro: punto di incontro delle bisettrici
# e' anche il centro della circonferenza inscritta
def incentro(t:Triangolo) -> Point:  
    alfa = dist(t._a,t._b)/((dist(t._a,t._b)+dist(t._a,t._c))) 
    #write('alfa=',alfa)
    K = hom(t._b,t._c,alfa) #.config(name='K',color='red',state=DRAGABLE)  
    #K = hom(t._b,t._c,1/alfa)  #causa ERR for /: 'int' and 'DOdivDO'
    beta = dist(t._b,t._a)/((dist(t._b,t._a)+dist(t._b,t._c)))  
    #write('beta=',beta)
    L = hom(t._a,t._c,beta) #.config(name='L',color='red',state=VISIBLE) 
  
    #write('A=',t._a)
    #write('B=',t._b)
    #write('C=',t._c)
    #write('K=',K)
    #write('L=',L)
    
    # no come segue
    #I = inters(Line(t._a,K),Line(t._b,L))  #ok, ma disegna le rette
    #a1 = asse(t._a,t._b)
    #a2 = asse(t._b,t._c)
    #I = inters(a1,a2)
    
    b1 = Line(t._a,K).config(state=VISIBLE,color='orange',width=THIN)
    b2 = Line(t._b,L).config(state=VISIBLE,color='orange',width=THIN)
    I = inters(b1,b2).config(state=VISIBLE,color='red')
    
    #I.config(state=VISIBLE,color='red')
    #r = dist(C,piede(C,Line(t._a,t._b)))
    return I #Circle(C,r) #C #H #K   con C va, con Circle da ERRORE

#circonferenza inscritta in un triangolo
def circinscr(t:Triangolo) -> Circle:
    I = incentro(t)
    #r = dist(I,piede(I,Line(t._a,t._b)))  #lento
    #return Circle(I,r) 
    #r = Line(t._a,t._b).config(state=INVISIBLE,color='green') #no, rende invisibili anche i vertici del t.
    r = Line(t._a,t._b) #,state=INVISIBLE,color='green')
    #P = piede(I,Line(t._a,t._b))
    P = piede(I,r)
    return Circle(I,P) 
    
#circonferenza circoscritta ad un triangolo
def circcirc(t:Triangolo) -> Circle:
    a1 = asse(t._a,t._b) 
    a2 = asse(t._a,t._c) 
    C = inters(a1,a2)
    return Circle(C,t._a) 

#=============================
if __name__ == '__main__':
    '''
    '''
 



    

   
