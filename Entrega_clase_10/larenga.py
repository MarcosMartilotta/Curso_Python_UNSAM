# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 18:02:52 2021

@author: Marcos Martilotta
"""


'''
def pascal(n,k):    
    if k == 0:
        res = 1
        return res
    else:
        res = ((n-k + 1)/k)*pascal(n,k-1)
        return res

'''
'''
def pascal(n,k):
    def pascal_aux(n):
        if n == 0:
            return []
        elif n == 1:
            return [1]
        else:
            new_row = [1]
            last_row = pascal_aux(n-1)
            for i in range(len(last_row)-1):
                new_row.append(last_row[i] + last_row[i+1])
            new_row += 1
        return new_row        
    return pascal_aux(n+1)[k]
'''

'''
def pascal(n,k):
    def pascal_aux(n):
        if n == 0:
            return[1]
        elif n == 1:
            return [1]
        else:
            nueva_fila = [1]
            
            
            
            
            
#larenga.py
#MASCIA, JULIAN FEDERICO

#Funcion triangle inspirada en https://stackoverflow.com/questions/10628788/python-recursive-pascal-triangle
'''
def triangle(n):
          
    if n == 0:
        return []

    elif n == 1:
        return [[1]] #Caso base

    else:
        new_row = [1]
        result = triangle(n-1)  #Caso recursivo
        last_row = result[-1] #ultima fila
        
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    
    return result


def pascal(fila,col):
    
    triangulo=triangle(fila+1) #busco la fila n+1 del triangulo (arranca en 0)
    return triangulo[fila][col]
            
#a=pascal(5,2)              
