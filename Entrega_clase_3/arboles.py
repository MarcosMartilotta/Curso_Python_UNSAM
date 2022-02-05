# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 21:21:16 2021

@author: user
"""
import csv
from pprint import pprint
import collections 
import math

def leer_parque(nombre_archivo, parque):
    
    f = open(nombre_archivo, 'r', encoding = 'utf-8')
    rows = csv.reader(f) 
    headers = next(rows)
    data = []
    data_parque = []
    for row in rows:   
        fila = dict(zip(headers,row))
        data.append(fila)
        if fila['espacio_ve'] == parque:
            #float(fila['altura_tot'])
            data_parque.append(fila)
    return(data_parque)
    f.close()

def especies(lista_arboles):
    i=0    
    lista = []
    for row in lista_arboles:
        lista.append(row['nombre_com'])
        i += 1
    conjunto = set(lista)
    return conjunto
    #print(i,set(lista),'\n')
    
def contar_ejemplares(data_parque):
    lista = []
    for row in data_parque:
        lista.append(row['nombre_com'])
    cuenta = collections.Counter(lista)
    #pprint(cuenta)
    pprint(cuenta.most_common(5))
    return(cuenta)

def obtener_alturas(data_parque,especie):
    alturas = []
    for row in data_parque:
        if row['nombre_com'] == especie:
            alturas.append(float(row['altura_tot']))
    '''
    pprint(alturas)
    
    promedio = sum(alturas)/len(alturas)
    print(round(promedio,2))
    print(max(alturas))
    '''

def obtener_inclinaciones(data_parque,especie):
    inclinaciones = []
    for row in data_parque:
        if row['nombre_com'] == especie:
            inclinaciones.append(float(row['inclinacio']))
    #pprint(inclinaciones)
    return inclinaciones
'''   
def especimen_mas_inclinado(data_parque):
    ejemplares = list(especies(data_parque))
    lista_maximos = []
    inclinacion_max = []
    for row in ejemplares:
        inclinacion = obtener_inclinaciones(data_parque,row) #aca tengo la inlinacion de todas las especies de tal parque
        
        inclinacion_max[row] = max(inclinacion) 
        lista_maximos.append(inclinacion_max)
    for n in lista_maximos:
  '''      

parque = ('CENTENARIO')
especie = 'Jacarandá'
data_parque = leer_parque('../Data/arbolado-en-espacios-verdes.csv',parque)
ejemplares = especies(data_parque)
cantidad_ejemplares = contar_ejemplares(data_parque)
alturas = obtener_alturas(data_parque,especie)
inclinaciones = obtener_inclinaciones(data_parque,especie)
#mas_inclinado = especimen_mas_inclinado(data_parque)