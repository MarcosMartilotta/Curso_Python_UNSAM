# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 00:02:01 2021

@author: user
"""

def invertir_lista(lista):
    invertida = []
    ultima_pos = len(lista) - 1
    
    for e in lista:             # si la copio quedan linqueadas, de esta manera me creo otra lista igual
        invertida.append(e) 
                             
    for e in lista:
        invertida[ultima_pos] = e
        ultima_pos -= 1
    return invertida
        
        
        

if __name__ == '__main__':
    
    lista = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
    
    invertida = invertir_lista(lista)