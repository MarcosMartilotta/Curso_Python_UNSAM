# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 17:48:02 2021

@author: Marcos Martilotta
"""
import random
import matplotlib.pyplot as plt
import numpy as np


#6.14
def donde_insertar (lista, x, verbose = False):

    '''Utiliza el mismo algoritmo que busqueda_binaria,
        pero entrega el valor de donde se podria insertar el nuevo elemento
        para que la función permanezca odenada.
        Precondición: la lista está ordenada
        Devuelve posición si x no está en lista;
        Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if pos == -1:
        pos = medio
    return pos

#6.15
def insertar (lista, x, verbose = False):

    '''Utiliza el mismo algoritmo que busqueda_binaria,
        pero entrega el valor de donde se podria insertar el nuevo elemento
        para que la función permanezca odenada.
        Precondición: la lista está ordenada
        Devuelve posición si x no está en lista;
        Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if pos == -1:
        if lista[medio] < x:
            pos = medio
            lista.insert(medio+1,x)
        else: 
            pos = medio
            lista.insert(medio,x)
    if verbose:
        print(lista)
    return pos

'''
def busqueda_binaria(lista, x, verbose = False):
    Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos
'''
