# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:43:34 2021

@author: Marcos Martilotta
"""

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0

class TorreDeControl():
    '''
        Permite simular el comportamiento de una torre de control de aviones
        donde la prioridad en la pista la tienen los vuelos que aterrizan
    '''
    def __init__(self):
        '''
            Al iniciar creo dos objetos del tipo cola, para poder encolar
            o desencolar nuevos aviones en cada uno.
        '''
        self.cola_arribo = Cola()
        self.cola_partida = Cola()
        
    def nuevo_arribo(self, avion):
        '''
            Encolo un avion a la lista de aviones para aterrizar
        '''
        self.cola_arribo.encolar(avion)
        
    def nueva_partida(self, avion):
        '''
            Encolo un avion a la lista de aviones para despegar
        '''
        self.cola_partida.encolar(avion)
        
    def ver_estado(self):
        '''
            Imprime de manera clara que aviones hay en ambas listas de espera
        '''
        arribo = ','.join(self.cola_arribo.items)
        print('Vuelos esperando para aterrizar: ', arribo)
        despegue = ','.join(self.cola_partida.items)
        print('Vuelos esperando para despegar: ', despegue )
        
    def asignar_pista(self):
        '''
            Asigna una pista con prioridad para los que tienen que aterrizar 
            imprime cual fue y lo quita de la lista.
        '''
        if self.cola_arribo.esta_vacia() == False:
            print(f'El vuelo {self.cola_arribo.items[0]} aterrizó')
            self.cola_arribo.desencolar()
        elif self.cola_partida.esta_vacia() == False:
            print(f'El vuelo {self.cola_partida.items[0]} despegó')
            self.cola_partida.desencolar() 
        else:
            print('No hay vuelos en espera')
            
if __name__ == '__main__':
    import torre_control
    torre = torre_control.TorreDeControl()
    torre.nuevo_arribo('AR156')
    torre.nueva_partida('KLM1267')
    torre.nuevo_arribo('AR32')
    torre.nueva_partida('AR123')
    torre.ver_estado()
    torre.asignar_pista()
    
    