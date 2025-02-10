def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Ejemplo de uso
anio = int(input("Ingresa un año: "))

if es_bisiesto(anio):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")