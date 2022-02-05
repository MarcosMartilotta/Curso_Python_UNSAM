# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 23:26:37 2021

@author: user
"""
4.3
def buscar_u_elemento(lista, elemento):
    indice = -1
    
    for i, n in enumerate(lista): #reversed(list(enumerate(x))): con esto se podría recorrer alrevez
        
        if n == elemento:
            indice = i
    
    return indice

def buscar_n_elemento(lista, elemento):
    cantidad = 0
    
    for n in lista: 
        if n == elemento:
            cantidad += 1
    
    return cantidad
#4.4
def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = 0 # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor 
        if e >= m:
            m = e
    
    return m

def minimo(lista):
    m = lista[0]
    
    for e in lista:
        if e <= m:
            m = e
    
    return m



if __name__ == '__main__':
    
    lista = [1,2,3,4,2,4,6,-4,7,3,45,4,2,1]
    elemento = 2
    #print(buscar_u_elemento(lista, elemento))
    
    #print(buscar_n_elemento(lista, elemento))
    
    #print(maximo(lista))
    
    print(minimo(lista))