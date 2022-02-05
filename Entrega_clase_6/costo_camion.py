import informe_funciones
def costo_camion(nombre_archivo):
    '''
        calcula el costo total del camion y lo devuelve como punto flotante
    '''
    costo = 0.0
    camion = informe_funciones.leer_camion(nombre_archivo)
    for row in camion:
        costo += int(row['cajones'])*float(row['precio'])
    return costo