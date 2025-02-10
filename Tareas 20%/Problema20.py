def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Retorna la posición donde se encontró
    return -1  # No encontrado

# Ejemplo de uso
lista = [10, 23, 45, 70, 11, 15]
objetivo = 70
resultado = busqueda_lineal(lista, objetivo)

print(f"Elemento encontrado en la posición: {resultado}" if resultado != -1 else "Elemento no encontrado")