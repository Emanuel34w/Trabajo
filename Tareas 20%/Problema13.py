def convertir_temperatura(valor, origen, destino):
    origen = origen.lower()
    destino = destino.lower()

    # Convertir origen a Celsius
    if origen == "c":
        celsius = valor
    elif origen == "f":
        celsius = (valor - 32) * 5 / 9
    elif origen == "k":
        celsius = valor - 273.15
    else:
        return "Unidad de origen no válida"

    # Convertir Celsius a destino
    if destino == "c":
        return celsius
    elif destino == "f":
        return celsius * 9 / 5 + 32
    elif destino == "k":
        return celsius + 273.15
    else:
        return "Unidad de destino no válida"

# Ejemplo de uso
valor = float(input("Ingresa la temperatura: "))
origen = input("Unidad de origen (C, F, K): ")
destino = input("Unidad de destino (C, F, K): ")

resultado = convertir_temperatura(valor, origen, destino)
print(f"Temperatura convertida: {resultado} {destino.upper()}")