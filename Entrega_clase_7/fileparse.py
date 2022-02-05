# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 06:59:50 2021

@author: Marcos Martilotta

"""
#Ejercicio 6.6

import csv

def parse_csv(lista_recibida, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    filas = csv.reader(lista_recibida)
    if not has_headers and select:
        raise RuntimeError('Para seleccionar primero necesito encabezados')
    # Lee los encabezados del archivo
    if has_headers:
        encabezados = next(filas)
        

    # Si se indicó un selector de columnas,
    #    buscar los índices de las columnas especificadas.
    # Y en ese caso achicar el conjunto de encabezados para diccionarios
    if select:
        indices = [encabezados.index(nombre_columna) for nombre_columna in select]
        encabezados = select
            
    else:
        indices = []
           
    registros = []
    for n,fila in enumerate(filas):
        if types:
            try:
                fila = [func(val) for func, val in zip(types, fila)]
            except ValueError:
                if not silence_errors:
                    print(f'Fila {n}: No pude convertir {fila}')
                    print(f'Fila {n}: Motivo: invalid literal for int() with base 10: ''')
        if not fila:    # Saltear filas vacías
            continue
        # Filtrar la fila si se especificaron columnas
        if indices:
            fila = [fila[index] for index in indices]
            
        # Armar el diccionario
        if has_headers:
            registro = dict(zip(encabezados, fila))
            registros.append(registro)
        else:
            registro = tuple(fila)
            registros.append(registro)
    return registros


