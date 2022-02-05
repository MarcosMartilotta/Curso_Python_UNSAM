# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:36:08 2021

@author: user
"""

import random
import numpy as np

def medir_temp(n):
        
    mu = 0 
    sigma = 0.2
    temp_normal = 37.5
    
    mediciones = []
    for i in range(n):
        mediciones.append(temp_normal + random.normalvariate(mu,sigma))
    
    arr = np.array(mediciones)
    
    np.save('../Data/temperaturas',arr)
    return mediciones

def resumen_temp(n):
    mediciones = medir_temp(n)
    
    valor_maximo = max(mediciones)
    valor_minimo = min(mediciones)
    promedio = sum(mediciones)/n
    
    if n % 2 == 0: #si es par
        var1 = mediciones[int(n/2)]
        var2 = mediciones[int(n/2 + 1)]
        mediana = (var1 + var2) / 2
    if n % 2 == 1: # si es impar
        mediciones.sort()
        ordenadas = mediciones
        mediana = ordenadas[int(n/2 + 0.5)]
        
    return valor_maximo, valor_minimo, promedio, mediana

    

if __name__ == '__main__':
    mediciones = medir_temp(99)
    medidas = resumen_temp(99)