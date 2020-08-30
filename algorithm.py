import numpy as np

class Mesa:
    def __init__(self,numero):
        self.estado = 1
        self.numero_mesa = numero
        print(self.estado)
    
    def trans(self,N):
        if N == 0:
            self.estado = 0
        
class Memoria:
    def __init__(self):
        self.lista_espera = []
        self.lista_activado = []
        self.lista_desactivado =[]
    
    def agregar(self,mesa,lista):
        if lista == 'e':
            (self.lista_espera).append(mesa)
        elif lista == 'a':
            (self.lista_activado).append(mesa)
        elif lista == 'd':
            (self.lista_activado).append(mesa)
    
    def next(self):
        for i in self.lista_espera:
            if (i.estado % 2) == 0 :
                return i



def activacion(mesa):
    mesa.trans(2)
    return mesa

def desactivacion(mesa):
    mesa.trans(3)
    return mesa 

def aumento(matrix):
    rows = (matrix.shape)[0]
    col = (matrix.shape)[1]
    print(rows)
    print(col)
    matrix = np.insert(matrix,0,[[0],[0]],axis=0)
    matrix = np.insert(matrix,rows+1,[[0],[0]],axis=0)
    matrix = np.insert(matrix,0,[[0],[0]],axis=1)
    matrix = np.insert(matrix,col+1,[[0],[0]],axis=1)
    return matrix

m1 = Mesa(1)
m2 = Mesa(2)
m3 = Mesa(3)
m4 = Mesa(4)
m5 = Mesa(5)
m6 = Mesa(6)

mymatrix = np.array([
    [m1,m1,0,0,0,0,m6,m6],
    [m1,m1,0,0,0,0,m6,m6],
    [0,0,0,m3,m3,0,0,0],
    [m2,m2,0,m3,m3,0,0,0],
    [m2,m2,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [m4,m4,0,0,0,0,m5,m5],
    [m4,m4,0,0,0,0,m5,m5]
],dtype = object)

mymatrix=aumento(mymatrix)

M = Memoria()
for i in range(((mymatrix.shape)[1])-2):
    for w in range (((mymatrix.shape)[0])-2):
        print(type((mymatrix[i,w])))
        if type(mymatrix[i,w]).__name__=='Mesa':
            if ((mymatrix[i,w]).estado)==1:
                M.agregar(mymatrix[i,w],'a')
                rectangulo = [
                    (i-2,w+2),(i-1,w+2),(i,w+2),(i+1,w+2),(i+2,w+2),
                    (i+3,w+2),(i+3,w+1),(i+3,w),(i+3,w-1),(i+3,w-2),
                    (i+3,w-3),(i+2,w-3),(i+1,w-3),(i,w-3),(i-1,w-3),
                    (i-2,w+3),(i-2,w-2),(i-2,w-1),(i-2,w),(i-2,w+1)]
                for i2 in rectangulo:
                    print(i2)
                    if type(mymatrix[i2[0],i2[1]]).__name__ == 'Mesa':
                        M.agregar(mymatrix[i2[0],i2[1]],'d')
                        (mymatrix[i2[0],i2[1]]).trans(0)
                        
print(M.lista_desactivado)
print(((M.lista_activado)[1]).estado)