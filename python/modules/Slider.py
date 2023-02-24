# File: Slider.py - ok
# Date: 23 feb 23
# Note: slider di un punto che si muove su un segmento

from kinter import * #serve! [23feb23]

# una slider serve per selezionare un valore compreso in un dato range;
# una slider ha una posizione e grandezza fissa su video (in unita' pixel);
# puo' essere riferita all'angolo alto-sx o basso-dx
#
class Slider:
          
    # x, y  : coppia di coordinate (in pixel) del primo punto della slider:
    #         se sono positive si riferiscono al punto 'corner' in alto-sx
    #         altrimenti si riferiscono al punto 'dimens' in basso-dx
    # size  : grandezza (in pixel) della slider
    # start : valore iniziale (estremo sinistro)
    # end   : estremo destro
    # param : parametro di posizionamento iniziale del pallino
    #
    def __init__(self,x,y,size,start,end,param=.5,col='black'): 
        fact = scale()*pixunit()
        pr = corner1() if x>0 else corner2()
        self._p1 = pr+Point(x/fact,-y/fact)
        self._p2 = pr+Point((x+size)/fact,-y/fact)
        self._seg = Segment(self._p1,self._p2,color=col,state=VISIBLE,width=THICK)
        self._start = start
        self._range = end-start
        self._length = dist(self._p1,self._p2)
        self._point = PointOn(self._seg,param,color=col,state=DRAGABLE) #cursore
        pv = self._point + Point(0/fact,-5/fact)   #posizione del testo del valore 
        self._label = Label(pv,"{0}",[self.value()],color=col,state=VISIBLE) 
              
    # Value corrispondente al valore dello slider    
    def value(self):
        d = dist(self._p1,self._point)
        return self._start+(self._range/self._length)*d    

'''
#---- main ----
s = Slider(30,40,100,3,9,0.7,'red')  #valori da 3 a 9
t = Slider(-150,-80,100,3,9,0.7,'blue')  # label in basso a destra
O = Point(1,2).config(name='O',width=3,color='lime green')
A = Point(3,1).config(name='A',width=3,color='lime green')
B = Point(-2,-1).config(name='B',width=3,color='lime green')
a = Circle(O,s.value(),width=1,color='red',state=DRAGABLE) # ?
show('scale:',scale())
'''
