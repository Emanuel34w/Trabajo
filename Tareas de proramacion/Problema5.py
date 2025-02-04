def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número para verificar si es primo: "))

# Verificar y mostrar el resultado
print(f"{numero} es primo." if es_primo(numero) else f"{numero} no es primo.")