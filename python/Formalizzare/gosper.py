# File: gosper.py - ok
# Date: 22 feb 23
# Note: curva esagonale di Gosper

assioma = 'X'
regole = {'X':'X+YF++YF-FX--FXFX-YF+','Y':'-FX+YFYF++YF+FX--FX-Y'}
disegno = sostituisci(assioma,regole,3)  
#print("D=",disegno)
angolo, passo = 60, .5  
hide() #per velocizzare il disegno
setcol('black')
left(90)
disegna(disegno,angolo,passo)
