def generar_pares_impares(limite):
    pares = []
    impares = []

    for numero in range(1, limite + 1):
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return pares, impares

# Solicitar al usuario que ingrese el límite
limite = int(input("Ingresa el límite: "))

# Generar las listas de números pares e impares
pares, impares = generar_pares_impares(limite)

# Mostrar los resultados
print(f"Números pares hasta {limite}: {pares}")
print(f"Números impares hasta {limite}: {impares}")