# File: usa_Slider.py - ok
# Date: 23 feb 23
# Note: slider di un punto che si muove su un segmento

#import Slider
from Slider import *

#---- main ----
s = Slider(30,40,100,3,9,0.7,'red')  #valori da 3 a 9
t = Slider(-150,-80,100,3,9,0.7,'blue')  # label in basso a destra
O = Point(1,2).config(name='O',width=3,color='lime green')
A = Point(3,1).config(name='A',width=3,color='lime green')
B = Point(-2,-1).config(name='B',width=3,color='lime green')
a = Circle(O,s.value(),width=1,color='red',state=DRAGABLE) # ?
#show('scale:',scale())
