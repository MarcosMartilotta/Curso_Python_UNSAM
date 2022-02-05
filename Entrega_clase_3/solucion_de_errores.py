#solucion_de_errores.py
#Ejercicios de errores en el código

#%%
#Ejercicio 3.1. Funcion tiene_a()
#Comentario: El error era del tipo semántico y se encontraba en la expresion de los if, el cual hacia que no recorra toda la frase
# Lo corregí agregando un contador que si termina teniendo un valor mayor a cero imprimirá true, sino false. 
#Aclaración, la funcion solo sirve para detectar a minuscula, por ello en el primer caso devolverá False.
# A continuación, el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    contador = 0
    while i < n:
        #print(expresion[i])
        if expresion[i] == 'a':
            contador += 1
        i += 1
    if contador > 0:
        return True
    else:
        return False
    

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
print(tiene_a('La novela 1984 de George Orwell'))
print(tiene_a('Apor'))


#Ejercicio 3.2
#La a la funcion le faltaban los : luego del while, el if y def. Ademas retornaba Falso la cual no es una palabra reservada del lenguaje
#Se agregaron los : donde correspondía y se cambió la palabra Falso por False.

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#Ejercicio 3.3
#La funcion sólo detectara cuando el 1 sea un string. En caso de pasarle un entero habrá que convertirlo antes
#asigne a la variable expresion, ella misma pero convertida a string. 

def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

#Ejercicio 3.4
#Esta funcion no devolvía nada, agregue el return al final para que devuelva el valor de la operación

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")


import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    #registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        print(encabezado)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)