def contar_vocales_consonantes(cadena):
    # Definir vocales
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    consonantes = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
    
    # Inicializar contadores
    num_vocales = sum(1 for c in cadena if c in vocales)
    num_consonantes = sum(1 for c in cadena if c in consonantes)

    return num_vocales, num_consonantes

# Ejemplo de uso
texto = input("Ingresa una cadena: ")
vocales, consonantes = contar_vocales_consonantes(texto)

print(f"Número de vocales: {vocales}")
print(f"Número de consonantes: {consonantes}")
