def fibonacci(n):
    secuencia = []
    a, b = 0, 1  # Inicializamos los dos primeros términos de la secuencia

    for _ in range(n):
        secuencia.append(a)  # Agregamos el término actual a la secuencia
        a, b = b, a + b  # Calculamos el siguiente término

    return secuencia

# Solicitar al usuario que ingrese el número de términos
num_terminos = int(input("Ingresa el número de términos de la secuencia de Fibonacci: "))

# Generar y mostrar la secuencia
if num_terminos <= 0:
    print("Por favor, ingresa un número mayor que 0.")
else:
    print(f"Secuencia de Fibonacci con {num_terminos} términos: {fibonacci(num_terminos)}")