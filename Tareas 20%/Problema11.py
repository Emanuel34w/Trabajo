def es_palindromo(cadena):
    # Convertir a minúsculas y eliminar espacios
    cadena = cadena.lower().replace(" ", "").replace("á", "a").replace("é", "e")\
        .replace("í", "i").replace("ó", "o").replace("ú", "u")
    
    # Comparar la cadena con su reverso
    return cadena == cadena[::-1]

# Ejemplo de uso
texto = input("Ingresa una palabra o frase: ")
if es_palindromo(texto):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
