# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 20:25:10 2021

@author: Marcos Martilotta
"""

import matplotlib.pyplot as plt
import numpy as np 
import random

    
    
    
def randomwalk(largo):
    '''
        Realiza 3 gráficos con las random_walk de 0 a largo,
        en el primer gráfico muestra 12 caminatas y en los de abajo 
        la que más y la que menos se alejan.
        Pre: Debe ingresar unicamente un número entero
        Pos: no retorna ningun valor, sólo grafica
    '''
    n = 0 
    
    plt.figure(figsize = (12, 8), dpi = 80)
    
    #Configuraciones para el primer subplot, ax1
    ax1 = plt.subplot(2,1,1)
    ax1.title.set_text('12 Caminatas al azar')
    plt.xlabel('Tiempo')
    plt.ylabel('Distancia al origen')
    plt.xlim(0, largo)
    plt.ylim(-500, 500)
    
    todas_caminatas = []
    while n < 12:
        pasos=np.random.randint(-1,2,largo)
        caminata = (pasos.cumsum())
        todas_caminatas.append(caminata)
        r = random.random() 
        b = random.random() #asigno 3 valores al azar para hacer los colores
        g = random.random() 
        color = (r, g, b)
        plt.plot(caminata, c = color, linewidth = 0.5)
        n += 1
    #Puedo inicializar en valores extremos de manera que siempre alguno de los que elijo sea el mayor
    mas_lejos = todas_caminatas[0] #Asigno la primer caminata como la mas lejana
    menos_lejos = todas_caminatas[0] #Asigno la primer caminata como la más cercana
    
    for camino in todas_caminatas:
        if max(abs(camino)) > max(abs(mas_lejos)):
            mas_lejos = camino #si el camino que mira el for es mas grande que el 
                                 #primero, lo guardo como el que mas se aleja
                                 
        if max(abs(camino)) < max(abs(menos_lejos)):
            menos_lejos = camino #aca guardo el que menos se aleja
    
    #Configuraciones para el segundo subplot
    ax2 = plt.subplot(2,2,3)
    ax2.title.set_text('La caminata que más se aleja')
    plt.plot(mas_lejos, color = 'Blue')
    plt.xlabel('Tiempo')
    plt.ylabel('Distancia al origen')
    plt.xlim(0, largo)
    plt.ylim(-500, 500)
    
    #Configuraciones para el tercer sublot
    ax3 = plt.subplot(2,2,4)
    ax3.title.set_text('La caminata que menos se aleja')
    plt.plot(menos_lejos, color = 'Red')
    plt.xlabel('Tiempo')
    plt.ylabel('Distancia al origen')
    plt.xlim(0, largo)
    plt.ylim(-500, 500)
    
    plt.show()

if __name__ == '__main__':

    N = 100000
    randomwalk(N)

