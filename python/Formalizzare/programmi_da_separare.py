# File: programmi_da_estrarre.py - ok
# Date: 6 gen 23
# Note: esempi di L-sistemi
#       cfr: 




""" albero - ok 
assioma = 'X'
regole = {'X':'F[+X]F[-X]+X','F':'FF'}
disegno = sostituisci(assioma,regole,5)
print("D=",disegno)
angolo, passo = 20, .2
left(90)
disegna(disegno,angolo,passo)
"""
    




"""
#---- ottagono ---- ok 
assioma = 'X'
regole = {'X':'F+X'}  
disegno = sostituisci(assioma,regole,8)  
print("D=",disegno)
angolo, passo = 45, 1   
hide() #per velocizzare il disegno
setcolor('black')
disegna(disegno,angolo,passo)
"""


"""
#---- raggiera ottagonale ---- ok 
assioma = 'X'
regole = {'X':'[F]+X'}  
disegno = sostituisci(assioma,regole,8)  
print("D=",disegno)
angolo, passo = 45, 1   
hide() #per velocizzare il disegno
setcolor('black')
disegna(disegno,angolo,passo)
"""



#"""
#---- rosa di esagono ---- ok 
assioma = 'X'
regole = {'X':'[F+F+F+F+F+]+X'}  
disegno = sostituisci(assioma,regole,6)  
print("D=",disegno)
angolo, passo = 60, 1   
hide() #per velocizzare il disegno
setcolor('red')
disegna(disegno,angolo,passo)
#"""


"""
#---- rosa di n-poligoni generalizzata ---- ok 3gen23
n = 7 #quadrati/pentagono/esagoni/ottagono/decagoni/...
angolo = 360/n
passo = 1

assioma = 'Y'
regole = {'Y':'F+Y'} 
#F = sostituisci(assioma,regole,n-1)   #5
F = sostituisci(assioma,regole,n-(n-1)%2)   #5
regole = {'X':'[T]+X','T':F} 
disegno = sostituisci('X',regole,n+1)  #7
print("D=",disegno)
hide() #per velocizzare il disegno
setcolor('red')
disegna(disegno,angolo,passo)
"""





"""
#---- foglia (cfr. Yallop-Wadler, p.8) ---- ?? 3gen23
assioma = 'X'
regole = {'X':'X-[[F]+F]+X[+XF]-F','F':'FF'}  
disegno = sostituisci(assioma,regole,4)  
print("D=",disegno)
angolo, passo = 22.5, 1   
hide() #per velocizzare il disegno
setcolor('black')
right(90)
disegna(disegno,angolo,passo)
"""



"""
#---- pentagoni di pentagoni ---- ok 3gen23
assioma = 'F+F+F+F+F'
regole = {'F':'FF+F+F+F+F+FF'}  
disegno = sostituisci(assioma,regole,3)  
print("D=",disegno)
angolo, passo = 72, .5   
hide() #per velocizzare il disegno
setcolor('black')
right(180)
disegna(disegno,angolo,passo)
"""






"""
#---- quadrati di Peano ---- ok 
assioma = 'X'
regole = {'X':'F-F-F-F','F':'F-F+F+F+F-F-F-F+F'}  # [1] ?
disegno = sostituisci(assioma,regole,2)  
print("D=",disegno)
angolo, passo = 90, .5   
hide() #per velocizzare il disegno
setcolor('black')
disegna(disegno,angolo,passo)
"""


"""

"""


