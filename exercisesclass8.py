
# city = input()

# def Welcome(param):
#         print(f"Hola bienvenido a {param}")
        
# Welcome(city)

###################################################################################################



def convertir_unidades(valor, unidad_inicial, unidad_final):
    if unidad_inicial == 'mm' and unidad_final == 'cm':
        return valor / 10
    elif unidad_inicial == 'mm' and unidad_final == 'm':
        return valor / 1000
    elif unidad_inicial == 'cm' and unidad_final == 'mm':
     return valor * 10
    elif unidad_inicial == 'cm' and unidad_final == 'm':
        return valor / 100
    elif unidad_inicial == 'm' and unidad_final == 'cm':
        return valor * 100
    elif unidad_inicial == 'm' and unidad_final == 'mm':
        return valor * 1000
    else:
        return "Conversión no válida. Unidades no soportadas."


resultado1 = convertir_unidades(1500, 'mm', 'm')
print(resultado1)  

resultado2 = convertir_unidades(2.5, 'm', 'cm')
print(resultado2)

resultado3 = convertir_unidades(2, "n", 2)
print(resultado3)