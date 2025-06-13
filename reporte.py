from graphviz import Digraph

def generar_reporte(partida: object, ruta_salida="reporte_juego"):
    dot = Digraph(comment='Estado del Juego')
    dot.attr(rankdir='LR')
    dot.attr('node', shape='box', style='filled', fontname='Helvetica')

    # =====================
    # MAZOS DE LOS JUGADORES
    # =====================
    for jugador in partida.jugadores:
        nombre = jugador.nombre.replace(" ", "_")
        cartas = jugador.mostrar_cartas()

        anterior = None
        for i, carta in enumerate(reversed(cartas)):
            id_nodo = f"{nombre}_carta_{i}"
            label = f"{carta}"
            color = carta_color(carta)
            dot.node(id_nodo, label=label, fillcolor=color)

            if anterior:
                dot.edge(id_nodo, anterior)
            anterior = id_nodo

        # Etiqueta del jugador al inicio
        if cartas:
            dot.node(f"{nombre}_inicio", f"Mazo {jugador.nombre}", fillcolor="white", style="bold")
            dot.edge(f"{nombre}_inicio", f"{nombre}_carta_{len(cartas)-1}")

    # =====================
    # CARTA EN MESA
    # =====================
    if partida.carta_en_mesa:
        label = str(partida.carta_en_mesa)
        dot.node("MESA", f"Área de Juego:\n{label}", fillcolor="lightblue", style="bold")

    # =====================
    # MAZO DE RESERVA (vertical)
    # =====================
    cartas_reserva = partida.mazo_reserva.recorrer()
    anterior = None
    for i, carta in enumerate(reversed(cartas_reserva)):
        id_nodo = f"reserva_{i}"
        label = str(carta)
        color = carta_color(carta)
        dot.node(id_nodo, label=label, fillcolor=color)
        if anterior:
            dot.edge(id_nodo, anterior)
        anterior = id_nodo

    if cartas_reserva:
        dot.node("reserva_inicio", "Mazo de Reserva", fillcolor="white", style="bold")
        dot.edge("reserva_inicio", f"reserva_{len(cartas_reserva)-1}")

    # =====================
    # EXPORTAR REPORTE
    # =====================
    dot.render(ruta_salida, format='png', cleanup=True)
    print(f"✅ Reporte generado: {ruta_salida}.png")

def carta_color(carta):
    color_hex = carta.split("(")[-1].replace(")", "").strip()
    try:
        return color_hex
    except:
        return "white"
