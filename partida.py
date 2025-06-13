from estructuras import ListaCircular
from copy import deepcopy

class Partida:
    def __init__(self, nombre, mazo_original, jugadores, shuffles):
        self.nombre = nombre
        self.jugadores = jugadores
        self.shuffles = shuffles
        self.mazo_original = mazo_original
        self.mazo_actual = deepcopy(mazo_original)
        self.mazo_reserva = ListaCircular()
        self.turno_actual = 0
        self.carta_en_mesa = None

    def aplicar_shuffles(self):
        for tipo, x in self.shuffles:
            if tipo == "RIGHT" and x is not None:
                self.mazo_actual.right_shuffle(x)
            elif tipo == "HALF_SHUFFLE":
                self.mazo_actual.half_shuffle()
            elif tipo == "FARO_SHUFFLE":
                self.mazo_actual.faro_shuffle()

    def repartir_cartas(self):
        nodos = self.mazo_actual.obtener_nodos()
        total = len(nodos)
        indice = total - 1  # repartir desde la cola

        for i in range(7):
            for jugador in self.jugadores:
                if indice < 0:
                    return
                jugador.recibir_carta(nodos[indice].dato)
                indice -= 1

        self.mazo_reserva.reconstruir_desde_lista(nodos[:indice+1])

    def iniciar_juego(self):
        self.turno_actual = 0
        self.carta_en_mesa = self.jugadores[0].mazo.pop()

    def simular_turno(self):
        jugador = self.jugadores[self.turno_actual]
        carta_jugada = jugador.jugar_carta(self.carta_en_mesa)

        if carta_jugada:
            self.carta_en_mesa = carta_jugada
        else:
            nodos_reserva = self.mazo_reserva.obtener_nodos()
            if nodos_reserva:
                carta_robada = nodos_reserva.pop(-1).dato
                if carta_robada.coincide(self.carta_en_mesa):
                    self.carta_en_mesa = carta_robada
                else:
                    jugador.robar_carta(carta_robada)
                self.mazo_reserva.reconstruir_desde_lista(nodos_reserva)
            else:
                return "mazo_agotado"

        if not jugador.tiene_cartas():
            return "ganador"

        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)
        return "continuar"
