def verificar_numero(numero, multiplo_de=None):
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")

    if multiplo_de is not None:
        if numero % multiplo_de == 0:
            print(f"{numero} es múltiplo de {multiplo_de}.")
        else:
            print(f"{numero} no es múltiplo de {multiplo_de}.")

# Solicitar datos al usuario
numero = int(input("Ingresa un número: "))
multiplo_de = input("Ingresa un número para verificar si es múltiplo (opcional, deja vacío si no deseas): ")

# Convertir a entero si se ingresó un valor
multiplo_de = int(multiplo_de) if multiplo_de.strip() else None

# Verificar y mostrar resultados
verificar_numero(numero, multiplo_de)