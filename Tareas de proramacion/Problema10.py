def manejar_archivo(nombre_archivo, modo, contenido=None):
    """
    Función para manejar operaciones de lectura y escritura en archivos.
    :param nombre_archivo: Nombre del archivo a manejar.
    :param modo: Modo en el que se abrirá el archivo ('r' para leer, 'w' para escribir, 'a' para agregar contenido).
    :param contenido: Contenido a escribir o agregar en el archivo (opcional).
    :return: Contenido del archivo si se lee, mensaje de éxito si se escribe o agrega, o mensaje de error si el modo no es válido.
    """
    with open(nombre_archivo, modo) as archivo:
        if modo == 'r':  # Si el modo es lectura, devolver el contenido del archivo
            return archivo.read()
        elif modo in ['w', 'a']:  # Si el modo es escritura o agregado, escribir el contenido
            archivo.write(contenido)
            return f"Operación '{modo}' completada."
        else:
            return "Modo no válido."  # Retornar mensaje de error si el modo no es válido

def menu():
    """
    Función que despliega un menú interactivo para manejar archivos.
    """
    nombre_archivo = input("Ingresa el nombre del archivo: ")  # Solicita el nombre del archivo al usuario

    while True:
        # Mostrar opciones del menú
        print("\n--- Menú ---")
        print("1. Leer archivo")
        print("2. Escribir en archivo")
        print("3. Modificar archivo (agregar contenido)")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':  # Opción para leer el archivo
            print(manejar_archivo(nombre_archivo, 'r'))
        elif opcion == '2':  # Opción para escribir en el archivo (sobreescribe el contenido)
            contenido = input("Ingresa el contenido a escribir: ")
            print(manejar_archivo(nombre_archivo, 'w', contenido))
        elif opcion == '3':  # Opción para agregar contenido al archivo
            contenido = input("Ingresa el contenido a agregar: ")
            print(manejar_archivo(nombre_archivo, 'a', contenido))
        elif opcion == '4':  # Opción para salir del programa
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")  # Mensaje de error si la opción es inválida
