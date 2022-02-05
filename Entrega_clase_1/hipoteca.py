# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
pago_mensual_extra = pago_mensual + pago_extra


while saldo > 0.0:
    mes = mes +1
    while mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - pago_mensual_extra
        total_pagado = total_pagado + pago_mensual_extra
        #print(mes, round(total_pagado, 3), saldo, 'pago extra')
        print(f'Mes {mes} Total a la Fecha: ${total_pagado:0.2f} Saldo actual: ${saldo:0.2f} Tiene extra')
        mes = mes + 1
    if saldo < pago_mensual:
        total_pagado = total_pagado + saldo
        saldo = 0.0
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    print(f'Mes {mes} Total a la Fecha: ${total_pagado:0.2f} Saldo actual: ${saldo:0.2f}')
    #print(mes, round(total_pagado, 3), round(saldo,3))
    

print('Total pagado', round(total_pagado, 2))
print('La cantidad de meses requeridos fue:', mes)