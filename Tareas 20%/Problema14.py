#Metodo de ordenamiento por burbuja
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]  # Intercambio
    return lista

# Ejemplo
print(selection_sort([5, 3, 8, 4, 2]))

#Metodo de ordenamiento por isercion
def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

# Ejemplo
print(insertion_sort([5, 3, 8, 4, 2]))

