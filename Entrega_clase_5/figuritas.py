# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 14:29:55 2021

@author: user
"""

import numpy as np
import random
import matplotlib.pyplot as plt

def crear_album(figus_total):
    espacios_vacios = np.zeros(figus_total+1)    
    return espacios_vacios

def album_incompleto(A):
    completitud = 0. in A
    return completitud    #devuelve True si hay un cero

def comprar_figu(figus_total):
    figurita = random.randint(0, figus_total)
    return figurita

def cuantas_figus(figus_total):
    album = crear_album(figus_total)    
    cantidad = 0
    while album_incompleto(album):
        figurita = comprar_figu(figus_total)
        album[figurita] += 1.
        cantidad += 1
    return cantidad

def experimetno_figus(n_repeticiones,figus_total):
    
    lista_cant = []
    while n_repeticiones >= 0:
        cantidad = cuantas_figus(figus_total)
        lista_cant.append(cantidad)
        n_repeticiones -= 1
                                                #tratar de hacerlo por comprension de listas
    lista_figus = np.array(lista_cant)
    return np.mean(lista_figus)

def comprar_paquete(figus_total, figus_paquete):
    paquete = []
    for i in range(figus_paquete):
        paquete.append(random.randint(0,figus_total))        
    figus_paquete = np.array(paquete)
    return paquete

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    cantidad = 0
    while album_incompleto(album):
        for figu in range(figus_paquete):
            album[random.randint(0,figus_total)] = 1
        cantidad += 1
    return cantidad

def paquetes_promedio(n_repeticiones, figus_total, figus_paquete):
    lista_cant = []
    while n_repeticiones >= 0:
        cantidad = cuantos_paquetes(figus_total, figus_paquete)
        lista_cant.append(cantidad)
        n_repeticiones -= 1
                                                #tratar de hacerlo por comprension de listas
    lista_figus = np.array(lista_cant)
    return np.mean(lista_figus)

def n_paquetes_hasta_llenar(n_repeticiones, figus_total, figus_paquete):
    lista_cant = []
    while n_repeticiones >= 0:
        cantidad = cuantos_paquetes(figus_total, figus_paquete)
        lista_cant.append(cantidad)
        n_repeticiones -= 1
                                                #tratar de hacerlo por comprension de listas
    lista_figus = np.array(lista_cant)
    return lista_figus

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

def proba_especifica(n_paquetes):
    cantidad_especifica = (n_paquetes <= 850).sum()
    return cantidad_especifica
    
if __name__ == '__main__':
    figus_total = 670
    figus_paquete = 5
    n_repeticiones = 100
    '''
    espacios_vacios = crear_album(figus_total)
    completitud = album_incompleto(espacios_vacios)
    figurita = comprar_figu(figus_total)
    cantidad = cuantas_figus(figus_total)
    promedio = figus_promedio(100, figus_total)
    '''
    #paquete = comprar_paquete(figus_total, figus_paquete)
    #cantidad_paquetes = cuantos_paquetes(figus_total, figus_paquete)
    #promedio = paquetes_promedio(n_repeticiones, figus_total, figus_paquete)
    plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de figuritas pegadas.")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()
    n_paquetes = n_paquetes_hasta_llenar(n_repeticiones, figus_total, figus_paquete)
    proba = proba_especifica(n_paquetes)/n_repeticiones
    
    plt.hist(n_paquetes, bins = 30)
    
  