# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 18:09:24 2021

@author: user
"""

def medidas_hoja_A(N):
    """
    Devuelve el ancho y el largo de la hoja A(N), por recursión.
    Pre: N debe ser mayor o igual a 0.
    Pos: devuelve un tupla con el ancho y el largo de la hoja.
    """
    if N == 0:
        res = (841,1189)
    #elif N == 1:
     #   res = (1189 // 2, 841)
    else:
        res = medidas_hoja_A(N-1)
        res =  (res[1] // 2, res[0])
       
    return res