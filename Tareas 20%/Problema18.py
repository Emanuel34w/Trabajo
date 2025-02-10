import math

def resolver_ecuacion_cuadratica(a, b, c):
    # Calcular el discriminante
    discriminante = b**2 - 4*a*c
    
    # Verificar el valor del discriminante
    if discriminante > 0:
        # Dos soluciones reales distintas
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Las soluciones son: x1 = {x1}, x2 = {x2}"
    elif discriminante == 0:
        # Una solución real (raíz doble)
        x = -b / (2*a)
        return f"La solución doble es: x = {x}"
    else:
        # Soluciones complejas
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(abs(discriminante)) / (2*a)
        return f"Las soluciones son complejas: x1 = {parte_real} + {parte_imaginaria}i, x2 = {parte_real} - {parte_imaginaria}i"

# Ejemplos de uso
print(resolver_ecuacion_cuadratica(2, 5, -3))  # 2x² + 5x - 3 = 0
print(resolver_ecuacion_cuadratica(1, -4, 4))  # x² - 4x + 4 = 0
print(resolver_ecuacion_cuadratica(1, 2, 5))   # x² + 2x + 5 = 0