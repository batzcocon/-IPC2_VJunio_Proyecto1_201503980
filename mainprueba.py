from cargar_xml import cargar_configuracion
from partida import Partida

# Cargar XML
ruta = "entrada_ejemplo.xml"  # Asegurate de que esté en el mismo directorio
mazo_original, jugadores, partidas_dict = cargar_configuracion(ruta)

# Seleccionar partida
nombre_partida = "Partida1"
shuffles = partidas_dict.get(nombre_partida)

if not shuffles:
    print(f"❌ La partida '{nombre_partida}' no fue encontrada en el XML.")
    exit()

# Crear partida
partida = Partida(nombre_partida, mazo_original, jugadores, shuffles)

# Aplicar shuffles y repartir
partida.aplicar_shuffles()
partida.repartir_cartas()
partida.iniciar_juego()

print(f"\n🃏 Partida '{nombre_partida}' iniciada.")
print(f"➡️ Jugadores: {[j.nombre for j in jugadores]}")
print(f"🎴 Carta inicial en mesa: {partida.carta_en_mesa}")

# Simular juego
turno = 1
while True:
    estado = partida.simular_turno()
    jugador = partida.jugadores[partida.turno_actual - 1]

    print(f"\n🔁 Turno {turno} - Jugador: {jugador.nombre}")
    print(f"   Carta en mesa: {partida.carta_en_mesa}")

    if estado == "ganador":
        print(f"\n🏆 {jugador.nombre} ganó la partida en el turno {turno} con la carta {partida.carta_en_mesa}")
        break
    elif estado == "mazo_agotado":
        print(f"\n🛑 Mazo agotado. No se puede continuar. Última carta: {partida.carta_en_mesa}")
        break

    turno += 1
