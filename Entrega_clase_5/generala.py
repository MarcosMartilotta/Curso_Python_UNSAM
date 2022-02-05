# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 00:37:40 2021

@author: user
"""
import collections
import random

def tirar():
    lista =[]
    for i in range(5):
        lista.append(random.randint(1,6))
    
    return lista

def es_generala(tirada):
    n = 0
    for i in tirada:
        if i == tirada[0]:
            n +=1
    if n == 5:
        var = True
    else:
        var = 0
    return var
            
def prob_generala(N):
    
    def tirar_3_veces():
        
        def repeticiones(tirada):
            mas_repetido = collections.Counter(tirada) #Cuento cuantos hay de cada número
            numero_cantidad = mas_repetido.most_common()  #creo una lista de tuplas con los pares numero_cantidad
            numero = int(numero_cantidad[0][0]) #elijo el primer número, o sea el más repetido
            cantidad = int(numero_cantidad[0][1])    # guardo la cantidad de veces que se repitió
            return (numero,cantidad)
        
        primer_numero, primera_cantidad = repeticiones(tirar()) #tiro por primera vez 
        
        tirada_1 = []
        for n in range(primera_cantidad):
            tirada_1.append(primer_numero) #creo una lista con los mas repetidos
        
        if len(tirada_1) != 5: #Si es 5 significa que es generala
            for n in range(5 - len(tirada_1)):
                dado = random.randint(1, 6)
                if dado == primer_numero:
                    tirada_1.append(dado) #Hago una segunda tirada con los que me quedan y agrego a tirada_1 los que son iguales al más repetido
                    
        if len(tirada_1) != 5: # si es 5 significa que es generala
            for n in range(5 - len(tirada_1)):   
                dado = random.randint(1,6)
                tirada_1.append(dado) #Hago una tercera tirada con los que me quedan y los agrego todos a tirada_1 para llegar a 5
        
        return tirada_1
    
    G = sum([es_generala(tirar_3_veces()) for i in range(N)])
    prob = G/N
    
    print(f'Tiré {N} veces, de las cuales {G} saqué generala al finalizar los 3 intentos.')
    print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')
    
    
    return prob
    
    
    
if __name__ =='__main__':
    
    probabilidad = prob_generala(1000000)
    '''
    tirada = tirar()
    generala = es_generala(tirada)
    N = 1000000
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

'''