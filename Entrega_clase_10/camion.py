# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 07:11:45 2021

@author: Marcos Martilotta
"""
import informe_final


class Camion:

    def __init__(self, lotes):
        self.lotes = lotes
        
    def __iter__(self):
        return self.lotes.__iter__()

    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes)
    
    def __len__(self):
        return self.lotes.__len__()    
    
    def __getitem__(self,item):
        return self.lotes[item]
    
    def __repr__(self):
        return f'Camion({repr(self.lotes)})'
    
    def __str__(self):
        print(f'Camion con {len(self.lotes)} lotes ')
        t = []
        for lote in self.lotes:
            s = f'Lote de {lote.cajones} cajones de {lote.nombre}, pagados a ${lote.precio}'
            t.append(s)
        return '\n'.join(t)
        
    def precio_total(self):
        return sum(l.costo() for l in self.lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
    
if __name__ == '__main__':
    
    camion = informe_final.leer_camion('../Data/camion.csv')
    print(camion)