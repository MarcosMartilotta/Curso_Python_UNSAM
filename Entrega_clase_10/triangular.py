# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 20:23:54 2021

@author: user
"""
import math
#%%

def triangular(n):
    
    if n == 1:
        res = 1
        return res
    else:
        
        res = n*(n+1)/2 - triangular(n-1)
        return res
#%%
def cant_digitos(n):
    '''
    Pre: El número tiene más de un dígito
    '''

    if n < 10:
        res = 1
        return res
    else: 
        res = 1 + cant_digitos(n//10) 
        return res
#%%

def es_potencia(n, b):
    res = False
    potencia = b*b
    if potencia == n:
        res = True
        return res
    if potencia != n:
    else:
        return res
   
    
#%%
def posiciones(a,b):
    


#%%

def par(n):

def impar(n):

#%%
def maximo(lista):

#%%

def replicar(lista,n):

    
#%%

def pascal(n,k):    
    if k == 0:
        res = 1
        return res
    else:
        res = ((n-k + 1)/k)*pascal(n,k-1)
        return res
#%%
def combinaciones(lista, k):

#%%
def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if e < lista[medio]:
            res = bbinaria_rec(lista[:medio], e)
        else:
            res = bbinaria_rec(lista[medio:],e)
    return res
    
#%%
def medidas_hoja_A(N):
    if N == 0:
        hoja = (841, 1189) #ancho y largo
        return hoja 
    else:
        ancho = medidas_hoja_A(N-1)[1] // 2
        largo = medidas_hoja_A(N-1)[0]
        hoja = (ancho, largo)
        return hoja
        


    
    


    

    
        