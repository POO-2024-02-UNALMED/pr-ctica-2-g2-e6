import tkinter as tk
from tkinter import ttk, messagebox
import json

# ===========================
# FUNCIONES GENERALES
# ===========================

def mostrar_info_aplicacion():
    messagebox.showinfo("Aplicación", "Esta aplicación realiza varias operaciones y consultas.")

def mostrar_info_autores():
    messagebox.showinfo("Acerca de", "Autores: Mel Bulaf")

def salir_aplicacion():
    root.quit()

# ===========================
# INTERFAZ INICIAL
# ===========================

def mostrar_interfaz_inicial():
    limpiar_frame(content_frame)
    
    ttk.Label(content_frame, text="Bienvenido a la Aplicación", font=("Arial", 24, "bold"), foreground="#004080").pack(pady=20)

    ttk.Label(
        content_frame, 
        text="Seleccione una de las opciones del menú para acceder a diferentes procesos y servicios.",
        font=("Arial", 14), 
        justify=tk.CENTER,
        wraplength=600
    ).pack(pady=20)

# ===========================
# SELECCIÓN DE PROCESO
# ===========================

def manejar_seleccion_proceso(proceso):
    limpiar_frame(content_frame)
    
    etiqueta_proceso = ttk.Label(content_frame, text=f"Has seleccionado: {proceso}", font=("Arial", 18))
    etiqueta_proceso.pack(pady=10)

    if "Proceso 1" in proceso:
        TiendaApp(root)
    elif "Proceso 2" in proceso:
        mostrar_formulario_sedes()
    else:
        messagebox.showinfo("Info", "Esta funcionalidad está en desarrollo.")

# ===========================
# FORMULARIO DE SELECCIÓN DE SEDE Y SERVICIOS
# ===========================

def mostrar_formulario_sedes():
    limpiar_frame(content_frame)

    def seleccionar_sede():
        sede = sede_var.get()
        if sede in opciones_sedes:
            mostrar_servicios_por_sede(sede)
        else:
            messagebox.showwarning("Error", "Seleccione una sede válida.")

    sede_var = tk.StringVar()
    ttk.Label(content_frame, text="Seleccione una sede:", font=("Arial", 18)).pack(pady=10)

    opciones_sedes = ["Sede Medellin", "Sede Bogota", "Sede Cali", "Sede Cartagena"]
    menu_sedes = ttk.Combobox(content_frame, textvariable=sede_var, values=opciones_sedes, state="readonly")
    menu_sedes.pack(pady=10)

    ttk.Button(content_frame, text="Seleccionar Sede", command=seleccionar_sede).pack(pady=10)

# ===========================
# MOSTRAR SERVICIOS POR SEDE
# ===========================

def mostrar_servicios_por_sede(sede):
    limpiar_frame(content_frame)

    servicios_sedes = {
        "Sede Medellin": ["Veterinaria", "Peluquería", "Guardería"],
        "Sede Bogota": ["Veterinaria", "Hotel para mascotas"],
        "Sede Cali": ["Tienda de mascotas", "Peluquería"],
        "Sede Cartagena": ["Guardería", "Tienda de accesorios"]
    }

    ttk.Label(content_frame, text=f"Servicios disponibles en {sede}:", font=("Arial", 18, "bold")).pack(pady=10)

    servicios = servicios_sedes.get(sede, ["No hay servicios disponibles"])
    for servicio in servicios:
        ttk.Label(content_frame, text=f"• {servicio}", font=("Arial", 14)).pack()

    ttk.Button(content_frame, text="Volver", command=mostrar_formulario_sedes).pack(pady=10)

# ===========================
# CLASE TIENDAAPP (PROCESO 1)
# ===========================

class TiendaApp:
    def __init__(self, root):
        self.root = root
        self.mostrar_formulario_registro()

    def mostrar_formulario_registro(self):
        limpiar_frame(content_frame)

        ttk.Label(content_frame, text="Ingrese su nombre:", font=("Arial", 14)).pack(pady=5)
        self.nombre_entry = ttk.Entry(content_frame, font=("Arial", 12))
        self.nombre_entry.pack(pady=5)
        
        ttk.Button(content_frame, text="Continuar", command=self.mostrar_seleccion_productos).pack(pady=10)
    
    def mostrar_seleccion_productos(self):
        self.nombre_cliente = self.nombre_entry.get()
        if not self.nombre_cliente:
            messagebox.showwarning("Advertencia", "Por favor, ingrese su nombre.")
            return
        
        limpiar_frame(content_frame)

        ttk.Label(content_frame, text="Seleccione un producto:", font=("Arial", 14)).pack(pady=10)
        self.producto_var = tk.StringVar()

        for prod in cargar_productos():
            ttk.Radiobutton(content_frame, text=f"{prod['nombre']} - ${prod['precio']}", variable=self.producto_var, value=prod['nombre']).pack()

        ttk.Label(content_frame, text="Cantidad:", font=("Arial", 14)).pack(pady=5)
        self.cantidad_entry = ttk.Entry(content_frame, font=("Arial", 12))
        self.cantidad_entry.pack(pady=5)

        ttk.Button(content_frame, text="Comprar", command=self.realizar_compra).pack(pady=10)

    def realizar_compra(self):
        producto_seleccionado = self.producto_var.get()
        cantidad = self.cantidad_entry.get()

        if not producto_seleccionado or not cantidad.isdigit() or int(cantidad) <= 0:
            messagebox.showwarning("Advertencia", "Seleccione un producto y una cantidad válida.")
            return
        
        cantidad = int(cantidad)
        producto = next((p for p in cargar_productos() if p['nombre'] == producto_seleccionado), None)

        if producto:
            total = cantidad * producto['precio']
            recibo = f"Cliente: {self.nombre_cliente}\nProducto: {producto['nombre']}\nCantidad: {cantidad}\nTotal: ${total}"
            messagebox.showinfo("Recibo de compra", recibo)

# ===========================
# CARGA DE PRODUCTOS
# ===========================

def cargar_productos():
    try:
        with open("productos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# ===========================
# UTILIDADES
# ===========================

def limpiar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# ===========================
# CONFIGURACIÓN DE INTERFAZ
# ===========================

root = tk.Tk()
root.title("Interfaz de Aplicación Mejorada")
root.geometry("800x600")
root.configure(bg="#E3F2FD")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=6)
style.configure("TLabel", font=("Arial", 12))
style.configure("TCombobox", padding=5)

main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill=tk.BOTH, expand=True)

menu_bar = tk.Menu(main_frame)

archivo_menu = tk.Menu(menu_bar, tearoff=0)
archivo_menu.add_command(label="Aplicación", command=mostrar_info_aplicacion)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=salir_aplicacion)
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

procesos_menu = tk.Menu(menu_bar, tearoff=0)
procesos_menu.add_command(label="Tienda UNamascota", command=lambda: manejar_seleccion_proceso("Proceso 1"))
procesos_menu.add_command(label="Selección de Sede", command=lambda: manejar_seleccion_proceso("Proceso 2"))
menu_bar.add_cascade(label="Procesos", menu=procesos_menu)

ayuda_menu = tk.Menu(menu_bar, tearoff=0)
ayuda_menu.add_command(label="Acerca de", command=mostrar_info_autores)
menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)

root.config(menu=menu_bar)

content_frame = ttk.Frame(main_frame, padding=20, relief="ridge", borderwidth=2)
content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

mostrar_interfaz_inicial()

root.mainloop()