from estructuras import Pila

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mazo = Pila()  # El mazo es una pila LIFO 

    def recibir_carta(self, carta):
        self.mazo.push(carta)

    def jugar_carta(self, carta_en_mesa):
        # LIFO
        if not self.mazo.esta_vacia():
            carta_top = self.mazo.peek()
            if carta_top.coincide(carta_en_mesa):
                return self.mazo.pop()

            # Si no, buscar en el resto de la pila 
            anterior = None
            actual = self.mazo.cima

            while actual:
                if actual.dato.coincide(carta_en_mesa):
                    carta_valida = actual.dato
                    # Remover nodo manualmente de la pila
                    if anterior:
                        anterior.siguiente = actual.siguiente
                    else:
                        self.mazo.cima = actual.siguiente  # era la cima
                    return carta_valida
                anterior = actual
                actual = actual.siguiente

        return None  # No encontró ninguna carta que coincida


    def robar_carta(self, carta):
        self.mazo.push(carta)

    def tiene_cartas(self):
        return not self.mazo.esta_vacia()

    def mostrar_cartas(self):
        return self.mazo.obtener_cartas()

    def __str__(self):
        return f"{self.nombre}: {', '.join(self.mostrar_cartas())}"
