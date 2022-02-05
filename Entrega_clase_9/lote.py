# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 19:33:57 2021

@author: Marcos
"""
import fileparse

class Lote:
    '''
    Esta clase permite crear un objeto con 3 atributos, nombre, cajones y precio
        ademas devuelve el costo del objeto y los cajones que te quedan si le restas
        una cierta cantidad.
    '''
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        '''
            Devuelve el costo del cajon
        '''
        return float(self.cajones*self.precio)
        
    
    def vender(self, cantidad):
        '''
            Devuelve cuantos cajones quedan despues de eliminar cierta cantidad
        '''
        self.cajones - cantidad

    def __repr__(self):
        '''
            Imprime claramente el contenido del cajon e informa a que clase corresponde
        '''
        return f'Lote({self.nombre} , {self.cajones}, {self.precio})'
    