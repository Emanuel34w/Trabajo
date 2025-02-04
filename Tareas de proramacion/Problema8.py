import math

def calcular_area_circunferencia(radio):
    area = math.pi * radio**2
    circunferencia = 2 * math.pi * radio
    return area, circunferencia

# Solicitar al usuario que ingrese el radio
radio = float(input("Ingresa el radio del círculo: "))

# Calcular el área y la circunferencia
area, circunferencia = calcular_area_circunferencia(radio)

# Mostrar los resultados
print(f"El área del círculo es: {area:.2f}")
print(f"La circunferencia del círculo es: {circunferencia:.2f}")