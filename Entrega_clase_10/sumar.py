# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 00:26:13 2021

@author: user
"""

def sumar(lista):
    if len(lista) == 0:
        res = 0
    if len(lista) != 0:
        res = lista[0] + sumar(lista[1:])
    return res