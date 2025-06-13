import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from cargar_xml import cargar_configuracion
from partida import Partida
from reporte import generar_reporte
from reporte_final import guardar_log

partida = None
log_partida = []

def cargar_xml():
    global partida, jugadores, mazo, partidas_config
    archivo = filedialog.askopenfilename(filetypes=[("Archivos XML", "*.xml")])
    if archivo:
        mazo, jugadores, partidas_config = cargar_configuracion(archivo)
        combo_partidas['values'] = list(partidas_config.keys())
        text_area.insert(tk.END, f"✔️ Archivo cargado: {archivo}\n")

def iniciar_partida():
    global partida, log_partida
    nombre = combo_partidas.get()
    if not nombre:
        messagebox.showwarning("Partida no seleccionada", "Debes seleccionar una partida")
        return

    log_partida = []  # Reiniciar log para nueva partida

    shuffles = partidas_config[nombre]
    partida = Partida(nombre, mazo, jugadores, shuffles)
    partida.aplicar_shuffles()
    partida.repartir_cartas()
    partida.iniciar_juego()
    text_area.insert(tk.END, f"\n🟢 Partida '{nombre}' iniciada.\n")
    text_area.insert(tk.END, f"Carta inicial en mesa: {partida.carta_en_mesa}\n\n")

def continuar_turno():
    global partida
    if partida is None:
        messagebox.showerror("Error", "No se ha iniciado ninguna partida")
        return

    jugador = partida.jugadores[partida.turno_actual]
    log_partida.append(f"{jugador.nombre} jugó o robó una carta.")

    resultado = partida.simular_turno()
    text_area.insert(tk.END, f"➡️ Turno de {jugador.nombre}\n")
    text_area.see(tk.END)

    if resultado == "ganador":
        ganador = jugador.nombre
        guardar_log(partida, log_partida, ganador)
        messagebox.showinfo("Fin del juego", f"🏆 ¡{ganador} ha ganado la partida!")
    elif resultado == "mazo_agotado":
        guardar_log(partida, log_partida, None)
        messagebox.showwarning("Fin del juego", "❌ Mazo agotado. No hay ganador.")

def generar_grafico():
    if partida is None:
        messagebox.showerror("Error", "No se ha iniciado ninguna partida")
        return
    generar_reporte(partida)
    messagebox.showinfo("Gráfico generado", "📊 El reporte gráfico fue guardado como 'reporte_juego.png'")

# =======================
# INTERFAZ CON TKINTER
# =======================
root = tk.Tk()
root.title("Card Clash: IPC2 Edition")
root.geometry("800x500")

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

btn_cargar = tk.Button(frame_top, text="📂 Cargar XML", command=cargar_xml)
btn_cargar.pack(side=tk.LEFT, padx=5)

combo_partidas = ttk.Combobox(frame_top, state="readonly", width=30)
combo_partidas.pack(side=tk.LEFT, padx=5)

btn_iniciar = tk.Button(frame_top, text="▶️ Iniciar Juego", command=iniciar_partida)
btn_iniciar.pack(side=tk.LEFT, padx=5)

btn_continuar = tk.Button(frame_top, text="⏭️ Continuar", command=continuar_turno)
btn_continuar.pack(side=tk.LEFT, padx=5)

btn_graficar = tk.Button(frame_top, text="📊 Generar Gráfico", command=generar_grafico)
btn_graficar.pack(side=tk.LEFT, padx=5)

text_area = tk.Text(root, height=20, width=100)
text_area.pack(pady=10)

root.mainloop()
