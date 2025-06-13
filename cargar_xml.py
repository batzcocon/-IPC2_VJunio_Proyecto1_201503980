from carta import Carta
from jugador import Jugador
from estructuras import ListaCircular

def cargar_configuracion(ruta_xml):
    import xml.etree.ElementTree as ET
    tree = ET.parse(ruta_xml)
    root = tree.getroot()

    # Leer cartas del mazo
    lista_cartas = ListaCircular()
    for carta_elem in root.find('mazo_disponible/cartas').findall('carta'):
        color = carta_elem.attrib.get('color')
        numero = int(carta_elem.text.strip())
        if 1 <= numero <= 9:
            lista_cartas.insertar(Carta(color, numero))

    # Leer jugadores
    jugadores = []
    for jugador_elem in root.find('jugadores').findall('jugador')[:4]:
        jugadores.append(Jugador(jugador_elem.text.strip()))

    # Leer partidas y shuffles
    partidas = {}
    for partida_elem in root.find('partidas').findall('partida'):
        nombre = partida_elem.attrib.get('nombre')
        shuffles = []
        for shuffle_elem in partida_elem.find('shuffles').findall('shuffle'):
            tipo = shuffle_elem.text.strip().upper()
            x = shuffle_elem.attrib.get('x')
            shuffles.append((tipo, int(x) if x else None))
        partidas[nombre] = shuffles

    return lista_cartas, jugadores, partidas
