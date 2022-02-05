# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 00:27:37 2021

@author: user
"""

def propagar(lista):
    
    vector = lista.copy()
    
    if vector == []:
        return 'La lista es vacía'
    for i, fosforo in enumerate(vector[1:]):
       if fosforo == 0 and vector[i] == 1:
           vector[i + 1] = 1
    
    
    while(i >= 0):
        if vector[i] == 0 and vector[i+1] == 1:
            vector[i] = 1
        i -= 1
        

    return vector
    
'''
if __name__ == '__main__':
    vector = [0,0,-1,1,0,0,1,0,0,-1,0,0,0,-1,1,0,0,-1,0,0,1,-1,0,0,1,0,-1]
    propagado = propagar(vector)
'''