# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 06:53:07 2021

@author: Marcos Martilotta
"""

import csv 
from pprint import pprint
import fileparse

def leer_precios(nombre_archivo):
    '''Crea un diccionario con los precios de las frutas/verduras
       por cajon, donde la clave es la fruta y el valor el precio
        ej: {naranja: 123, pera: 34}
    '''
    precios = dict(fileparse.parse_csv(nombre_archivo,types = [str,float], has_headers = False))
    return precios

def leer_camion(nombre_archivo):
    '''Lee el archivo y devuelve una lista con diccionarios 
        donde cada diccionario será por ejemplo
        {nombre: pera, cajones: 23, precio: 123}        
    '''
    camion = fileparse.parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])

    return camion

def recaudo(camion, precios):
    '''
        toma los datos del camion y se fija en el archivo de precios de venta
        cuanto se recauda con la venta
    '''
    recaudado = 0.0
    for k in camion: #busco las frutas que hay en el camion en k voy a tener un diccionario
        try:
            fruta_verdura = k['nombre']
            print(fruta_verdura)
            print(precios[fruta_verdura])

            recaudado += float(precios[fruta_verdura])*int(k['cajones'])
        except KeyError:
            pass
    return recaudado

def diferencia(costo, recaudado):
    '''
    toma lo que costó el camion y lo que se recaudó y devuelve la ganancia
    '''
    dif = recaudado - costo
    return dif

def imprimir_informe(informe):
    '''
        imprime el informe realizado por hacer informe
    '''
    print('%10s %10d %10s %10.2f' % informe)

def hacer_informe(camion,precios):
    '''
    realiza un informe prolijo de lo comprado, y lo recaudado
    '''
    for k in camion:
        dif = precios[k['nombre']]-k['precio']
        informe = (k['nombre'],int(k['cajones']),'$'+str(round(float(k['precio']),2)),dif)
        imprimir_informe(informe)

def cabecera():
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')

    guiones = ('----------', '----------', '----------', '----------')
    print(f'{guiones[0]:>10s} {guiones[1]:>10s} {guiones[2]:>10s} {guiones[3]:>10s}')

'''
def informe_camion(nombre_archivo_camion,nombre_archivo_precios):

    cabecera()
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    hacer_informe(camion,precios)    
'''


