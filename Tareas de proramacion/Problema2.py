'''Ejercicio 2:'''
def calculadora():
    print("Calculadora Simple")
    print("Operaciones: +, -, *, /")
    
    operacion = input("Selecciona una operación: ")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        if num2 == 0:
            resultado = "Error: No se puede dividir por cero."
        else:
            resultado = num1 / num2
    else:
        resultado = "Operación no válida."

    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    calculadora()