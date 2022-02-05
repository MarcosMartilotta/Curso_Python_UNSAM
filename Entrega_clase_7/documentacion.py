# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 22:59:38 2021

@author: Marcos Martilotta

"""

def valor_absoluto(n):
   '''
       Devuelve el valor absoluto de un número, sea entero o no
   '''
   if n >= 0:
       return n
   else:
       return -n

def suma_pares(lista):
    '''
        Recibe una lista con números y suma todos aquellos que son pares
    '''
    res = 0
    for e in lista:
        if e % 2 ==0:
            res += e
        else:
            res += 0
    #En este caso, res es un invariante
    return res

def veces(a, b):
    '''
        Indica el resultado de sumar a veces b
        Pre: Deben ser numeros reales
        Pos: Retorna el valor, y cero si indicamos 0 veces
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    #Tiene dos invariantes, tanto res como nb
    
    return res
def collatz(n):
    '''
    Dado un numero indica cuantos pasos debo realizar para 
    llegar a 1 segun la conjetura collatz. Más información en 
    https://es.wikipedia.org/wiki/Conjetura_de_Collatz 
    Pre: Debe ingresar un número entero y positivo
    Pos: El resultado es la cantidad de veces que se debió aplicar el algoritmo
        sea n//2 o 3*n + 1
    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1
    #Res es la invariante de esta función
    
    return res