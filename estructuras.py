# ============================
# Nodo Genérico
# ============================
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# ============================
# Lista Circular Simplemente Enlazada
# ============================
class ListaCircular:
    def __init__(self):
        self.primero = None

    def insertar(self, carta):
        nuevo = Nodo(carta)
        if not self.primero:
            self.primero = nuevo
            nuevo.siguiente = nuevo
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.primero

    def recorrer(self):
        cartas = []
        if self.primero:
            actual = self.primero
            while True:
                cartas.append(str(actual.dato))
                actual = actual.siguiente
                if actual == self.primero:
                    break
        return cartas

    def obtener_nodos(self):
        nodos = []
        if self.primero:
            actual = self.primero
            while True:
                nodos.append(actual)
                actual = actual.siguiente
                if actual == self.primero:
                    break
        return nodos

    def reconstruir_desde_lista(self, lista_nodos):
        if not lista_nodos:
            return
        self.primero = lista_nodos[0]
        actual = self.primero
        for nodo in lista_nodos[1:]:
            actual.siguiente = nodo
            actual = nodo
        actual.siguiente = self.primero

    def right_shuffle(self, n):
        nodos = self.obtener_nodos()
        if not nodos:
            return
        carta_movida = nodos.pop(-1)
        posicion = len(nodos) - n
        if posicion < 0:
            posicion = 0
        nodos.insert(posicion, carta_movida)
        self.reconstruir_desde_lista(nodos)

    def half_shuffle(self):
        nodos = self.obtener_nodos()
        if len(nodos) < 2:
            return
        mitad = 26
        mitad_1 = nodos[:mitad]
        mitad_2 = nodos[mitad:]
        nuevos = mitad_2 + mitad_1
        self.reconstruir_desde_lista(nuevos)

    def faro_shuffle(self):
        nodos = self.obtener_nodos()
        if len(nodos) < 2:
            return
        mitad = 26
        mitad_1 = nodos[:mitad]
        mitad_2 = nodos[mitad:]
        resultado = []
        for i in range(len(mitad_1)):
            resultado.append(mitad_1[i])
            if i < len(mitad_2):
                resultado.append(mitad_2[i])
        self.reconstruir_desde_lista(resultado)

# ============================
# Pila Personalizada (para mazo de jugador)
# ============================
class Pila:
    def __init__(self):
        self.cima = None

    def push(self, carta):
        nuevo = Nodo(carta)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def pop(self):
        if self.cima:
            carta = self.cima.dato
            self.cima = self.cima.siguiente
            return carta
        return None

    def peek(self):
        return self.cima.dato if self.cima else None

    def esta_vacia(self):
        return self.cima is None

    def obtener_cartas(self):
        cartas = []
        actual = self.cima
        while actual:
            cartas.append(str(actual.dato))
            actual = actual.siguiente
        return cartas
