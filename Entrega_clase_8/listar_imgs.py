# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 00:38:24 2021

@author: Marcos Martilotta
"""
import os

def archivos_png(directorio):
    lista_archivos = os.listdir(directorio)
    lista_png = []
    for archivo in lista_archivos:
        if archivo[-3:] == 'png':
            lista_png.append(archivo)
            print(lista_png)

    return lista_png

if __name__ == '__main__':
    print(archivos_png('../Data/ordenar/imgs'))
    