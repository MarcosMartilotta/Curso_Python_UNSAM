# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 06:53:07 2021

@author: user
"""

import csv 
from pprint import pprint

def leer_precios(nombre_archivo):
    '''Crea un diccionario con los precios de las frutas/verduras'''
    precios = {}

    f = open(nombre_archivo, 'r')
    rows = csv.reader(f)
    for row in rows:
        try:
            fruta_verdura = row[0]
            precio = float(row[1])
            precios[fruta_verdura] = precio
        except IndexError:
            print('Falta una linea')
    f.close()
    return precios

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
       # headers = headers.split(',')
        for row in rows:
            record = dict(zip(headers, row)) # aca hago lo de abajo mas inteligentemente
            #lote = {'nombre':'row[0]', 'cajones':int(row[1]), 'precio':float(row[2])}
            camion.append(record)
    pprint(camion)
    return camion

def costo_camion(data_camion):
    costo = 0.0
    camion = leer_camion(data_camion)
    for row in camion:
        costo += int(row['cajones'])*float(row['precio'])
    return costo

def recaudo(camion, precios):
    recaudado = 0.0
    #claves_precios = precios.keys() #armo una lista con los nombres de las frutas de la lista de precios
    
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
    dif = recaudado - costo
    return dif

def hacer_informe(camion,precios):
    for k in camion:
        dif = precios[k['nombre']]-float(k['precio'])
        r = (k['nombre'],int(k['cajones']),'$'+str(round(float(k['precio']),2)),dif)
        print('%10s %10d %10s %10.2f' % r)



data_camion = '../Data/camion.csv'
data_precios = '../Data/precios.csv'

costo = costo_camion(data_camion)
camion = leer_camion(data_camion)
precios = leer_precios(data_precios)

'''
recaudado = recaudo(camion, precios)
ganancias = diferencia(costo, recaudado)

print('El costo del camion fue:',costo)
print('Se logró recaudar: ',recaudado)

if ganancias >= 0:
    print(f'Este mes se ganaron {round(ganancias, 2)}$')
else:
    print(f'Este mes se perdieron {round(-ganancias)}$ ')
'''    
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')

guiones = ('----------', '----------', '----------', '----------')
print(f'{guiones[0]:>10s} {guiones[1]:>10s} {guiones[2]:>10s} {guiones[3]:>10s}')

informe = hacer_informe(camion,precios)


#print(precios)
