import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime

def guardar_log(partida, pasos, ganador=None):
    root = ET.Element("partida_jugada")
    resumen = ET.SubElement(root, "resumen")

    if ganador:
        ET.SubElement(resumen, "ganador").text = ganador
    ET.SubElement(resumen, "total_pasos").text = str(len(pasos))

    pasos_elem = ET.SubElement(root, "pasos")
    for i, paso in enumerate(pasos, start=1):
        ET.SubElement(pasos_elem, "paso", n=str(i)).text = paso

    if ganador:
        ET.SubElement(pasos_elem, "paso", n=str(len(pasos)+1)).text = f"Ha ganado {ganador}"
    else:
        ET.SubElement(pasos_elem, "paso", n=str(len(pasos)+1)).text = "No hay ganador. No es posible continuar el juego"

    xml_str = ET.tostring(root, encoding='utf-8')
    pretty = minidom.parseString(xml_str).toprettyxml(indent="  ")

    fecha = datetime.now().strftime("%d_%m_%Y")
    nombre_archivo = f"{partida.nombre}_{fecha}.xml"

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(pretty)

    print(f"✅ Log guardado en: {nombre_archivo}")
