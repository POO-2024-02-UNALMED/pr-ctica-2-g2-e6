import tkinter as tk
from FieldFrame import FieldFrame
from tkinter import ttk, messagebox
import json
# Importaciones corregidas
from Main import inicializar_agendador, agendar_servicio, obtener_empleados_disponibles, obtener_sedes, obtener_servicios, verificar_disponibilidad
import tkinter as tk
from FieldFrame import FieldFrame
from tkinter import ttk, messagebox
import json
# Importaciones corregidas
from Main import inicializar_agendador, agendar_servicio, obtener_empleados_disponibles, obtener_sedes, obtener_servicios, verificar_disponibilidad

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

    sede_var = tk.StringVar()
    servicio_var = tk.StringVar()
    raza_var = tk.StringVar()
    precio_var = tk.StringVar()

    frame_sede = ttk.Frame(content_frame)
    frame_sede.pack(pady=10)
    ttk.Label(frame_sede, text="Seleccione una sede:", font=("Arial", 18)).pack(pady=10)
    
    opciones_sedes = obtener_sedes()
    print(f"Opciones de sedes: {opciones_sedes}")
    menu_sedes = ttk.Combobox(frame_sede, textvariable=sede_var, values=opciones_sedes, state="readonly")
    menu_sedes.pack(pady=10)
    
    ttk.Button(frame_sede, text="Seleccionar Sede", command=lambda: seleccionar_servicio(sede_var.get(), frame_sede, servicio_var, raza_var, precio_var)).pack(pady=10)

def seleccionar_servicio(sede, frame_sede, servicio_var, raza_var, precio_var):
    if sede not in obtener_sedes():
        messagebox.showwarning("Error", "Seleccione una sede válida.")
        return
    
    frame_servicio = ttk.Frame(content_frame)
    frame_servicio.pack(pady=10)
    ttk.Label(frame_servicio, text="Seleccione un servicio:", font=("Arial", 18)).pack(pady=10)

    opciones_servicios = obtener_servicios(sede)
    print(f"Opciones de servicios para {sede}: {opciones_servicios}")
    menu_servicios = ttk.Combobox(frame_servicio, textvariable=servicio_var, values=opciones_servicios, state="readonly")
    menu_servicios.pack(pady=10)
    
    def verificar_disponibilidad_action():
        servicio = servicio_var.get()
        print(f"Servicio seleccionado: {servicio}")
        if servicio:
            disponibilidad = verificar_disponibilidad(agendador, sede, servicio)
            print(f"Disponibilidad para {servicio} en {sede}: {disponibilidad}")
            if disponibilidad:
                confirmar_raza(sede, servicio, frame_servicio, frame_sede, raza_var,servicio_var,precio_var)
            else:
                messagebox.showwarning("Sin disponibilidad", "No hay disponibilidad para el servicio seleccionado.")
        else:
            messagebox.showwarning("Selección Incorrecta", "Debe seleccionar un servicio válido.")

    ttk.Button(frame_servicio, text="Seleccionar Servicio", command=verificar_disponibilidad_action).pack(pady=10)
    ttk.Button(frame_servicio, text="Cancelar", command=mostrar_formulario_sedes).pack(pady=10)

# ===========================
# CONFIRMAR RAZA
# ===========================

def confirmar_raza(sede, servicio, frame_servicio, frame_sede, servicio_var, raza_var, precio_var):
    limpiar_frame(content_frame)

    frame_raza = ttk.Frame(content_frame)
    frame_raza.pack(expand=True, fill=tk.BOTH)
    ttk.Label(frame_raza, text="Su mascota pertenece a:", font=("Arial", 18)).pack(pady=10)

    if servicio == "Entrenamiento":
        razas_disponibles = ["Perro", "Gato"]
        precio = 100
    elif servicio == "Peluquería":
        razas_disponibles = ["Perro", "Gato"]
        precio = 50
    elif servicio == "Veterinaria":
        razas_disponibles = ["Perro", "Gato", "Ave", "Conejo"]
        precio = 70
    else:
        razas_disponibles = []
        precio = 0

    print(f"Razas disponibles para {servicio}: {razas_disponibles} con precio ${precio}")
    menu_razas = ttk.Combobox(frame_raza, textvariable=raza_var, values=razas_disponibles, state="readonly")
    menu_razas.pack(pady=10)

    def confirmar_raza_action():
        raza = raza_var.get()
        print(f"Raza seleccionada: {raza}")
        if raza in razas_disponibles:
            precio_var.set(f"El precio del servicio de {servicio} es ${precio}.")
            seleccionar_empleado(sede, servicio, frame_raza, raza_var, precio_var)
        else:
            messagebox.showwarning("Selección Incorrecta", "Debe seleccionar una raza válida.")

    ttk.Button(frame_raza, text="Confirmar Raza", command=confirmar_raza_action).pack(pady=10)
    ttk.Button(frame_raza, text="Cancelar", command=lambda: seleccionar_servicio(sede, frame_servicio, servicio_var, raza_var, precio_var)).pack(pady=10)

    ttk.Label(frame_raza, textvariable=precio_var, font=("Arial", 14)).pack(pady=10)

# ===========================
# SELECCIONAR EMPLEADO
# ===========================

def seleccionar_empleado(sede, servicio, frame_raza, raza_var, precio_var):
    limpiar_frame(content_frame)

    empleados_disponibles = obtener_empleados_disponibles(agendador, sede)
    print(f"Empleados disponibles en {sede}: {empleados_disponibles}")
    empleados_var = tk.StringVar(value=[empleado.nombre for empleado in empleados_disponibles])

    frame_empleado = ttk.Frame(content_frame)
    frame_empleado.pack(pady=10)
    ttk.Label(frame_empleado, text="Seleccione un empleado:", font=("Arial", 18)).pack(pady=10)
    
    empleados_listbox = tk.Listbox(frame_empleado, listvariable=empleados_var, height=6, selectmode='single')
    empleados_listbox.pack(pady=10)

    def seleccionar_cupo():
        seleccion = empleados_listbox.curselection()
        if seleccion:
            empleado = empleados_disponibles[seleccion[0]]
            print(f"Empleado seleccionado: {empleado.nombre}")
            seleccionar_cupo_dia(sede, servicio, empleado,frame_raza, frame_empleado, raza_var, precio_var)
        else:
            messagebox.showwarning("Selección Incorrecta", "Debe seleccionar un empleado válido.")

    ttk.Button(frame_empleado, text="Seleccionar Empleado", command=seleccionar_cupo).pack(pady=10)
    ttk.Button(frame_empleado, text="Cancelar", command=lambda: confirmar_raza(sede, servicio, frame_raza, raza_var, precio_var)).pack(pady=10)

# ===========================
# SELECCIONAR CUPO POR DÍA
# ===========================

def seleccionar_cupo_dia(sede, servicio, empleado, frame_raza, frame_empleado, raza_var, precio_var):
    limpiar_frame(content_frame)

    dia_var = tk.StringVar()
    frame_cupo = ttk.Frame(content_frame)
    frame_cupo.pack(pady=10)
    ttk.Label(frame_cupo, text="Seleccione un día:", font=("Arial", 18)).pack(pady=10)
    
    opciones_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    menu_dias = ttk.Combobox(frame_cupo, textvariable=dia_var, values=opciones_dias, state="readonly")
    menu_dias.pack(pady=10)

    def seleccionar_dia():
        dia = dia_var.get()
        print(f"Día seleccionado: {dia}")
        dias_semana = {"Lunes": 0, "Martes": 1, "Miércoles": 2, "Jueves": 3, "Viernes": 4, "Sábado": 5}
        dia_numero = dias_semana.get(dia)
        if dia_numero is not None:
            cupos_disponibles = empleado.cupos_disponibles(dia_numero)
            print(f"Cupos disponibles para {dia}: {cupos_disponibles}")
            if cupos_disponibles:
                confirmar_cupo(sede, servicio, empleado, cupos_disponibles, frame_cupo, raza_var, precio_var)
            else:
                messagebox.showwarning("Sin disponibilidad", "No hay cupos disponibles para el día seleccionado.")
        else:
            messagebox.showwarning("Selección Incorrecta", "Debe seleccionar un día válido.")

    ttk.Button(frame_cupo, text="Seleccionar Día", command=seleccionar_dia).pack(pady=10)
    ttk.Button(frame_cupo, text="Cancelar", command=lambda: seleccionar_empleado(sede, servicio, frame_raza, raza_var, precio_var)).pack(pady=10)

# ===========================
# CONFIRMAR CUPO
# ===========================

def confirmar_cupo(sede, servicio, empleado, cupos_disponibles, frame_cupo, raza_var, precio_var):
    limpiar_frame(content_frame)

    cupos_var = tk.StringVar(value=[f"{cupo.get_dia()} {cupo.hora_inicio} - {cupo.hora_fin}" for cupo in cupos_disponibles])
    frame_confirmar_cupo = ttk.Frame(content_frame)
    frame_confirmar_cupo.pack(pady=10)
    ttk.Label(frame_confirmar_cupo, text="Seleccione un cupo:", font=("Arial", 18)).pack(pady=10)

    cupos_listbox = tk.Listbox(frame_confirmar_cupo, listvariable=cupos_var, height=6, selectmode='single')
    cupos_listbox.pack(pady=10)

    def confirmar_cupo_action():
        seleccion = cupos_listbox.curselection()
        if seleccion:
            cupo = cupos_disponibles[seleccion[0]]
            print(f"Cupo seleccionado: {cupo.get_dia()} {cupo.hora_inicio} - {cupo.hora_fin}")
            ingresar_datos_cliente(sede, servicio, empleado, cupo, frame_confirmar_cupo, raza_var, precio_var)
        else:
            messagebox.showwarning("Selección Incorrecta", "Debe seleccionar un cupo válido.")

    ttk.Button(frame_confirmar_cupo, text="Confirmar Cupo", command=confirmar_cupo_action).pack(pady=10)
    ttk.Button(frame_confirmar_cupo, text="Cancelar", command=lambda: seleccionar_cupo_dia(sede, servicio, empleado, frame_cupo, raza_var, precio_var)).pack(pady=10)

# ===========================
# INGRESAR DATOS DEL CLIENTE
# ===========================

def ingresar_datos_cliente(sede, servicio, empleado, cupo, frame_confirmar_cupo, raza_var, precio_var):
    limpiar_frame(content_frame)

    global field_frame_cliente
    
    frame_cliente = ttk.Frame(content_frame)
    frame_cliente.pack(pady=10)
    ttk.Label(frame_cliente, text="Datos del Cliente", font=("Arial", 16)).pack(pady=10)
    field_frame_cliente = FieldFrame(frame_cliente, "Criterio", ["Nombre", "Edad", "Cédula"], "Valor")
    field_frame_cliente.pack(pady=10)

    def confirmar_datos_cliente():
        cliente_data = (
            field_frame_cliente.getValue("Nombre"),
            field_frame_cliente.getValue("Edad"),
            field_frame_cliente.getValue("Cédula")
        )
        ingresar_datos_mascota(sede, servicio, empleado, cupo, cliente_data, frame_cliente, raza_var, precio_var)

    ttk.Button(frame_cliente, text="Confirmar Datos", command=confirmar_datos_cliente).pack(pady=10)
    ttk.Button(frame_cliente, text="Cancelar", command=lambda: confirmar_cupo(sede, servicio, empleado, [cupo], frame_confirmar_cupo, raza_var, precio_var)).pack(pady=10)

# ===========================
# INGRESAR DATOS DE LA MASCOTA
# ===========================

def ingresar_datos_mascota(sede, servicio, empleado, cupo, cliente_data, frame_cliente, raza_var, precio_var):
    limpiar_frame(content_frame)

    global field_frame_mascota
    
    frame_mascota = ttk.Frame(content_frame)
    frame_mascota.pack(pady=10)
    ttk.Label(frame_mascota, text="Datos de la Mascota", font=("Arial", 16)).pack(pady=10)
    field_frame_mascota = FieldFrame(frame_mascota, "Criterio", ["Nombre de la Mascota", "Especie de la Mascota", "Edad de la Mascota (meses)", "Género de la Mascota"], "Valor")
    field_frame_mascota.pack(pady=10)
    field_frame_mascota.setValue("Especie de la Mascota", raza_var.get())
    field_frame_mascota.disableEntry("Especie de la Mascota")

    def confirmar_datos_mascota():
        mascota_data = (
            field_frame_mascota.getValue("Nombre de la Mascota"),
            field_frame_mascota.getValue("Especie de la Mascota"),
            field_frame_mascota.getValue("Edad de la Mascota (meses)"),
            field_frame_mascota.getValue("Género de la Mascota")
        )
        confirmar_agendamiento(sede, servicio, empleado, cupo, cliente_data, mascota_data, frame_mascota)

    ttk.Button(frame_mascota, text="Confirmar Datos", command=confirmar_datos_mascota).pack(pady=10)
    ttk.Button(frame_mascota, text="Cancelar", command=lambda: ingresar_datos_cliente(sede, servicio, empleado, cupo, frame_cliente, raza_var, precio_var)).pack(pady=10)

# ===========================
# CONFIRMAR AGENDAMIENTO
# ===========================

def confirmar_agendamiento(sede, servicio, empleado, cupo, cliente_data, mascota_data, frame_mascota):
    limpiar_frame(content_frame)
    
    resultado = agendar_servicio(agendador, sede, servicio, cliente_data, mascota_data, cupo.get_dia().weekday(), cupo.hora_inicio, empleado.nombre)
    print(f"Resultado del agendamiento: {resultado}")
    messagebox.showinfo("Resultado", resultado)
    mostrar_interfaz_inicial()

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
procesos_menu.add_command(label="Agendar UNservicio", command=lambda: manejar_seleccion_proceso("Proceso 2"))
menu_bar.add_cascade(label="Procesos", menu=procesos_menu)

ayuda_menu = tk.Menu(menu_bar, tearoff=0)
ayuda_menu.add_command(label="Acerca de", command=mostrar_info_autores)
menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)

root.config(menu=menu_bar)

content_frame = ttk.Frame(main_frame, padding=20, relief="ridge", borderwidth=2)
content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Inicializar agendador globalmente
global agendador
agendador = inicializar_agendador()

mostrar_interfaz_inicial()

root.mainloop()