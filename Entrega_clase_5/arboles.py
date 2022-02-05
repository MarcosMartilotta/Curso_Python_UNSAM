# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 21:21:16 2021

@author: user
"""
import csv
from pprint import pprint
import collections
import math
import matplotlib.pyplot as plt
import numpy as np
import os

def leer_parque(nombre_archivo, parque):
    
    f = open(nombre_archivo, 'r', encoding = 'utf-8') #uso encoding para que lea bien los datos
    rows = csv.reader(f) 
    headers = next(rows)
    data = []
    data_parque = []
    for row in rows:                                  #en cada row tengo un arbol
        fila = dict(zip(headers,row))                 #agrupo el deader con su contenido
        if fila['espacio_ve'] == parque:
            data_parque.append(fila)                  #en data parque voy a ir guardando diccionarios que son los arboles, pero de un parque especifico
    f.close()
    return(data_parque)
    
def leer_arboles(nombre_archivo):
    
    f = open(nombre_archivo, 'r', encoding= 'utf-8')
    rows = csv.reader(f)
    headers = next(rows)
    arboleda = []
    for row in rows:
        fila = dict(zip(headers,row))
        arboleda.append(fila)
    f.close()
    return arboleda
    
def medidas_de_especies(variedades, arboleda):
    
    medidas_especies = {especie :[(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in variedades}
    return medidas_especies
    
def especies(lista_arboles): 
    
    lista = []
    for row in lista_arboles:
        lista.append(row['nombre_com'])
    conjunto = set(lista)                           #aca transformo a la lista en un conjunto, donde solamente va a aparecer una vez cada arbol
    return conjunto
    
def contar_ejemplares(data_parque):
    
    lista = []
    for row in data_parque:
        lista.append(row['nombre_com'])             #aca agrego todos los arboles de un parque a una lista
    cuenta = collections.Counter(lista)             #con esta instruccion cuento cuantas veces se repiten
    return(cuenta)  

def obtener_alturas(data_parque,especie):
    
    alturas = []
    for row in data_parque:
        if row['nombre_com'] == especie: 
            alturas.append(float(row['altura_tot'])) #agrego a la lista alturas, las alturas de todos los arboles de tal especie
    return alturas
    '''
    pprint(alturas)
    
    promedio = sum(alturas)/len(alturas)
    print(round(promedio,2))
    print(max(alturas))
    '''
#ejercicio 3.22
def obtener_inclinaciones(data_parque,especie):
    
    inclinaciones = []
    for row in data_parque:
        if row['nombre_com'] == especie:
            inclinaciones.append(float(row['inclinacio'])) #agrego a la lista inclinaciones, las inclinaciones del arbol especificado en especie
    return inclinaciones

#ejercicios clase 5
def histograma_altos (nombre_archivo,especie):
    arboleda = leer_arboles(nombre_archivo)
    altos = obtener_alturas(arboleda,especie)
    plt.hist(altos, bins = 50)

def scatter_hd(lista_de_pares, color,especie):
    arr = np.array(lista_de_pares)
    h = arr[0:,0]
    d = arr[0:,1]
    area = 2**2
    plt.scatter(d,h,s = area,c = color, alpha = 0.3)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title(f'relación diámetro-alto para {especie}')
    plt.xlim(0,150)
    plt.ylim(0,50)
    plt.figure()
    
def tres_graficos(nombre_archivo):
    os.path.join('..','Data','arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    especies = ['Eucalipto', 'Palo borracho rosado','Jacarandá']
    medidas = medidas_de_especies(especies,arboleda)
    colores = ['red','blue','green']
    
    for n,especie in enumerate(especies):
        scatter_hd(medidas[especie],colores[n],especies[n])
    
    
    

if __name__ == '__main__':
    
    '''variables_hardcodeadas'''
     
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'    
    parque = ('CENTENARIO')
    especie = 'Jacarandá'
    variedades = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    
    '''devolucion_de_funciones'''
    
    #data_parque = leer_parque(nombre_archivo,parque)

    arboleda = leer_arboles(nombre_archivo)    
    '''
    medidas_especies = medidas_de_especies(variedades,arboleda)
    
    todas_las_especies = especies(data_parque)

    cantidad_ejemplares = contar_ejemplares(data_parque)
    
    alturas = obtener_alturas(data_parque,especie)
    
    inclinaciones = obtener_inclinaciones(data_parque,especie)
    '''
    #plotear = histograma_altos(nombre_archivo, especie)
    lista_de_pares = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]
    #sactter = scatter_hd(lista_de_pares)
    graficos = tres_graficos(nombre_archivo)