
cadena = 'geringoso'
geringoso = ''
i = 0

for c in cadena:
    
    if c == 'a':
        geringoso = geringoso + c + 'pa'
    elif c == 'e':
        geringoso = geringoso + c + 'pe'
    elif c == 'i': 
        geringoso = geringoso + c + 'pi'
    elif c == 'o': 
        geringoso = geringoso + c + 'po'
    elif c == 'u':
        geringoso = geringoso + c + 'pu'
    else: 
        geringoso = geringoso + c
print(geringoso)   