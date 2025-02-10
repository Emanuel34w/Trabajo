#Pilas
class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # Agregar elemento a la pila

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()  # Sacar el último elemento
        return None

    def cima(self):
        return self.items[-1] if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.items) == 0

    def tamaño(self):
        return len(self.items)

# Ejemplo de uso
pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)
print(pila.pop())  # 3
print(pila.cima())  # 2

#Cola
class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.append(item)  # Agregar al final

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)  # Quitar el primero
        return None

    def frente(self):
        return self.items[0] if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.items) == 0

    def tamaño(self):
        return len(self.items)

# Ejemplo de uso
cola = Cola()
cola.encolar("A")
cola.encolar("B")
cola.encolar("C")
print(cola.desencolar())  # "A"
print(cola.frente())  # "B"

#Lista enlazada
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None
        while actual and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            return False  # No encontrado

        if anterior is None:
            self.cabeza = actual.siguiente  # Eliminar cabeza
        else:
            anterior.siguiente = actual.siguiente  # Saltar nodo

        return True

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
lista.mostrar()  # 30 -> 20 -> 10 -> None
lista.eliminar(20)
lista.mostrar()  # 30 -> 10 -> None
