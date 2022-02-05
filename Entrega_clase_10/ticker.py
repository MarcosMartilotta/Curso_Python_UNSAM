# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:51:24 2021

@author: user
"""
from formato_tabla import crear_formateador
from vigilante import vigilar
import csv
from informe_final import leer_camion

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
       
def filtrar_datos(rows, nombres):
    for row in rows:
        if row['nombre'] in nombres:
            yield row
            
def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def ticker(camion_file, log_file, fmt):
    
    camion = leer_camion(camion_file)
    log = parsear_datos(vigilar(log_file))
    filas = filtrar_datos(log,camion)
    formateador = crear_formateador(fmt)
    formateador.encabezado(['nombre','precio','volumen'])
    
    for linea in filas:
        linea = [linea['nombre'],str(linea['precio']),str(linea['volumen'])]
        formateador.fila(linea)

        
if __name__ == '__main__':
    ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'csv')