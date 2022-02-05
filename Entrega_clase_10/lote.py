# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 19:33:57 2021

@author: Marcos
"""
import fileparse

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        return float(self.cajones*self.precio)
    
    def vender(self, cantidad):
        self.cajones - cantidad

    def __repr__(self):
        return f'Lote({self.nombre} , {self.cajones}, {self.precio})'
    
    def __str__(self):
        return f'Lote de {self.cajones} de {self.nombre}, pagados a ${self.precio} cada uno'
        
        
            