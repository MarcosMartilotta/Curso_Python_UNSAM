# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 18:10:14 2021

@author: Marcos Martilotta
"""
from datetime import datetime, timedelta, date

def vida_en_segundos(fecha_nac):
    ''' Toma un str en formato dd/mm/AAAA y devuelve
        los segundos que viviste'''
        
    inicio_vida = datetime.strptime(fecha_nac, '%d/%m/%Y')
    
    tiempo_vivido = datetime.now() - inicio_vida 
    
    return tiempo_vivido.total_seconds()

def primavera():
    
    hoy = date.today()
    fecha_actual = datetime(year = hoy.year, month = hoy.month, day = hoy.day)
    año_proximo = hoy.year + 1
    proxima_primavera = datetime(año_proximo, 9, 21)
    dias_hasta_primavera = proxima_primavera - fecha_actual
    print('Para la proxima primavera faltan:', dias_hasta_primavera)
    
#Pendiente 8.3
def licencia_paternidad():
    comienzo = datetime(year = 2020, month = 9, day = 26)
    dias_de_licencia = 200
    reincorporacion = comienzo + dias_de_licencia
    print(reincorporacion)
    
#pendiente 8.4

