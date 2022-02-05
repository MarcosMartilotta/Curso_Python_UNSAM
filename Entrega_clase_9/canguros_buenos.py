# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 00:32:45 2021

@author: Marcos
"""


class Canguro:
    
    def __init__(self, nombre, lista = None): #Recibí ayuda de Luciano Gorgol para entender el error
        self.nombre = nombre
        self.contenido_marsupio = lista if lista else []
    
    def meter_en_marsupio(self, objeto):
        self.contenido_marsupio.append(objeto)
    
    def __str__(self):
        
        return   self.nombre +' ' + ', '.join([str(i) for i in self.contenido_marsupio])

#%%
'''
# canguro_malo.py
"""Este código continene un 
bug importante y dificil de ver
"""

class Canguro:
    """Un Canguro es un marsupial."""

    def __init__(self, nombre, contenido=[]): aca el error es que la lista por omision está asignada a la clase,y no al objeto. entonces a todos por omision les va a asignar la misma lista vacia, o sea la misma direccion de memoria
        Creo que el error está aca, al tener una lista como parámetro opcional
        al meter cangurito en madre, cangurito entra con los atributos que tenía la madra
        
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)
'''
#%%
if __name__ == '__main__':
    
    madre_canguro = Canguro('Madre')
    cangurito = Canguro('gurito')
    madre_canguro.meter_en_marsupio('billetera')
    madre_canguro.meter_en_marsupio('llaves del auto')
    madre_canguro.meter_en_marsupio(cangurito)

    print(madre_canguro)      
    print(cangurito)
#Moraleja, no poner un objeto mutable como valor por omisión
