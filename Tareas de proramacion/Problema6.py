def interes_compuesto(P, r, n, t):
    A = P * (1 + r / n) ** (n * t)
    return A

# Solicitar datos al usuario
capital = float(input("Ingresa el capital inicial (P): "))
tasa_anual = float(input("Ingresa la tasa de interés anual (r) en %: ")) / 100
veces_capitalizacion = int(input("Ingresa el número de veces que se capitaliza el interés por año (n): "))
tiempo = float(input("Ingresa el tiempo en años (t): "))

# Calcular el monto final
monto_final = interes_compuesto(capital, tasa_anual, veces_capitalizacion, tiempo)

# Mostrar el resultado
print(f"El monto final después de {tiempo} años es: {monto_final:.2f}")