# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 18:08:26 2021

@author: user
"""

numeros = list(range(10))
mult = 0

print(f'{str(0):>10s} {str(1):>5s} {str(2):>5s} {str(3):>5s} {str(4):>5s} {str(5):>5s} {str(6):>5s} {str(7):>5s} {str(8):>5s} {str(9):>5s}')
print('-'*65)
for n in numeros:
    fila = []
    for m in numeros:
        mult = (m*n)
        fila.append(mult)
    print(f'{n}: {fila[0]:>7d} {fila[1]:>5d} {fila[2]:>5d} {fila[3]:>5d} {fila[4]:>5d} {fila[5]:>5d} {fila[6]:>5d} {fila[7]:>5d} {fila[8]:>5d} {fila[9]:>5d}')
    
        
        
            

