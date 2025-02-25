import tkinter as tk
from FieldFrame import FieldFrame
from tkinter import ttk, messagebox
import json
# Importaciones corregidas
from Main import inicializar_agendador, agendar_servicio, obtener_empleados_disponibles, obtener_sedes, obtener_servicios, verificar_disponibilidad, CentroAdopcion, Mascota, Cliente, Dieta, EstadoSalud, Memorial, Fallecido, Producto, Tienda, Empleado, cargar_datos_productos,cargar_datos_productos2

# ===========================
# FUNCIONES GENERALES
# ===========================

def mostrar_info_aplicacion():
    messagebox.showinfo("Aplicación", "Está es la aplicación de UNmascota, un sistema de servicios de peluqueria, tienda, entrenamiento, peluqueria, gestion de osarios y nutricionista.")

def mostrar_info_autores():
    messagebox.showinfo("Acerca de", "Autores: Alejandro López González, Emmanuel Betancur Uribe, Santiago Martínez Ríos, Melanie Bula Fuente,  Tomas Ospina Gaviria")

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
        inicio_tienda()
    elif "Proceso 2" in proceso:
        mostrar_formulario_sedes()
    elif "Proceso 3" in proceso:
        emergencia()
    elif "Proceso 4" in proceso:
        gestionar_memorial()
    elif "Proceso 5" in proceso:
        mostrar_formulario_dietas()
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
            ingresarDatosCliente(sede, servicio, empleado, cupo, frame_confirmar_cupo, raza_var, precio_var)
        else:
            messagebox.showwarning("Selección Incorrecta", "Debe seleccionar un cupo válido.")

    ttk.Button(frame_confirmar_cupo, text="Confirmar Cupo", command=confirmar_cupo_action).pack(pady=10)
    ttk.Button(frame_confirmar_cupo, text="Cancelar", command=lambda: seleccionar_cupo_dia(sede, servicio, empleado, frame_cupo, raza_var, precio_var)).pack(pady=10)

# ===========================
# INGRESAR DATOS DEL CLIENTE
# ===========================

def ingresarDatosCliente(sede, servicio, empleado, cupo, frame_confirmar_cupo, raza_var, precio_var):
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
    mostrar_interfaz_inicial(content_frame)

# ===========================
# CLASE TIENDAAPP (PROCESO 1)
# ===========================

def inicio_tienda():
    limpiar_frame(content_frame)

    # Cargar productos desde el archivo serializado
    productos = cargar_datos_productos()

    if not productos:
        messagebox.showwarning("Error", "No se encontraron productos disponibles.")
        return

    # Mostrar opciones al usuario
    ttk.Label(content_frame, text="Bienvenido a la Tienda", font=("Arial", 18)).pack(pady=20)
    ttk.Label(content_frame, text="Seleccione una opción:", font=("Arial", 14)).pack(pady=10)

    def comprar():
        limpiar_frame(content_frame)
        ttk.Label(content_frame, text="¿Cómo le gustaría mostrar los productos?", font=("Arial", 14)).pack(pady=10)

        def mostrar_todo():
            limpiar_frame(content_frame)
            ttk.Label(content_frame, text="Seleccione un producto:", font=("Arial", 14)).pack(pady=10)

            # Mostrar todos los productos en un Combobox
            producto_var = tk.StringVar()
            productos_combobox = ttk.Combobox(
                content_frame,
                textvariable=producto_var,
                values=[f"{p.nombre} - ${p.precio} ({p.tipo_animal})" for p in productos],
                state="readonly"
            )
            productos_combobox.pack(pady=10)

            ttk.Label(content_frame, text="Cantidad de unidades:", font=("Arial", 14)).pack(pady=10)
            cantidad_var = tk.IntVar()
            cantidad_entry = ttk.Entry(content_frame, textvariable=cantidad_var)
            cantidad_entry.pack(pady=10)

            def confirmar_compra():
                producto_seleccionado = producto_var.get()
                cantidad = cantidad_var.get()

                if not producto_seleccionado or cantidad <= 0:
                    messagebox.showwarning("Error", "Seleccione un producto y una cantidad válida.")
                    return

                # Extraer el nombre del producto seleccionado
                nombre_producto = producto_seleccionado.split(" - ")[0]
                producto = next((p for p in productos if p.nombre == nombre_producto), None)

                if producto:
                    ingresar_datos_cliente(producto, cantidad)
                else:
                    messagebox.showwarning("Error", "Producto no encontrado.")

            ttk.Button(content_frame, text="Confirmar Compra", command=confirmar_compra).pack(pady=10)
            ttk.Button(content_frame, text="Cancelar", command=inicio_tienda).pack(pady=10)

        def filtrar_por_tipo():
            limpiar_frame(content_frame)
            ttk.Label(content_frame, text="Seleccione el tipo de animal:", font=("Arial", 14)).pack(pady=10)

            tipo_animal_var = tk.StringVar()
            tipos_animal = ["Perro", "Gato", "Conejo", "Ave"]
            tipo_combobox = ttk.Combobox(content_frame, textvariable=tipo_animal_var, values=tipos_animal, state="readonly")
            tipo_combobox.pack(pady=10)

            def mostrar_productos_filtrados():
                tipo_animal = tipo_animal_var.get()
                if not tipo_animal:
                    messagebox.showwarning("Error", "Seleccione un tipo de animal válido.")
                    return

                productos_filtrados = [p for p in productos if p.tipo_animal == tipo_animal]

                if not productos_filtrados:
                    messagebox.showinfo("Info", f"No hay productos disponibles para {tipo_animal}.")
                    return

                limpiar_frame(content_frame)
                ttk.Label(content_frame, text="Seleccione un producto:", font=("Arial", 14)).pack(pady=10)

                producto_var = tk.StringVar()
                productos_combobox = ttk.Combobox(
                    content_frame,
                    textvariable=producto_var,
                    values=[f"{p.nombre} - ${p.precio}" for p in productos_filtrados],
                    state="readonly"
                )
                productos_combobox.pack(pady=10)

                ttk.Label(content_frame, text="Cantidad de unidades:", font=("Arial", 14)).pack(pady=10)
                cantidad_var = tk.IntVar()
                cantidad_entry = ttk.Entry(content_frame, textvariable=cantidad_var)
                cantidad_entry.pack(pady=10)

                def confirmar_compra():
                    producto_seleccionado = producto_var.get()
                    cantidad = cantidad_var.get()

                    if not producto_seleccionado or cantidad <= 0:
                        messagebox.showwarning("Error", "Seleccione un producto y una cantidad válida.")
                        return

                    nombre_producto = producto_seleccionado.split(" - ")[0]
                    producto = next((p for p in productos_filtrados if p.nombre == nombre_producto), None)

                    if producto:
                        ingresar_datos_cliente(producto, cantidad)
                    else:
                        messagebox.showwarning("Error", "Producto no encontrado.")

                ttk.Button(content_frame, text="Confirmar Compra", command=confirmar_compra).pack(pady=10)
                ttk.Button(content_frame, text="Cancelar", command=filtrar_por_tipo).pack(pady=10)

            ttk.Button(content_frame, text="Mostrar Productos", command=mostrar_productos_filtrados).pack(pady=10)
            ttk.Button(content_frame, text="Cancelar", command=inicio_tienda).pack(pady=10)

        ttk.Button(content_frame, text="Mostrar Todo", command=mostrar_todo).pack(pady=10)
        ttk.Button(content_frame, text="Filtrar por Tipo", command=filtrar_por_tipo).pack(pady=10)
        ttk.Button(content_frame, text="Cancelar", command=inicio_tienda).pack(pady=10)

    ttk.Button(content_frame, text="Comprar", command=comprar).pack(pady=10)
    ttk.Button(content_frame, text="Salir", command=root.quit).pack(pady=10)

def ingresar_datos_cliente(producto, cantidad):
    limpiar_frame(content_frame)

    ttk.Label(content_frame, text="Ingrese sus datos:", font=("Arial", 14)).pack(pady=10)

    ttk.Label(content_frame, text="Nombre:", font=("Arial", 12)).pack(pady=5)
    nombre_entry = ttk.Entry(content_frame)
    nombre_entry.pack(pady=5)

    ttk.Label(content_frame, text="Cédula:", font=("Arial", 12)).pack(pady=5)
    cedula_entry = ttk.Entry(content_frame)
    cedula_entry.pack(pady=5)

    def finalizar_compra():
        nombre = nombre_entry.get()
        cedula = cedula_entry.get()

        if not nombre or not cedula:
            messagebox.showwarning("Error", "Por favor complete todos los campos.")
            return

        total = producto.precio * cantidad
        recibo = f"""
        Recibo de Compra:
        Producto: {producto.nombre}
        Cantidad: {cantidad}
        Precio Unitario: ${producto.precio}
        Total: ${total}

        Datos del Cliente:
        Nombre: {nombre}
        Cédula: {cedula}
        """

        # Limpiar el frame y mostrar el recibo en el mismo frame
        limpiar_frame(content_frame)
        ttk.Label(content_frame, text="Recibo de Compra", font=("Arial", 18)).pack(pady=20)
        ttk.Label(content_frame, text=recibo, font=("Arial", 12)).pack(pady=10)

        # Botón para volver al inicio
        ttk.Button(content_frame, text="Volver al Inicio", command=inicio_tienda).pack(pady=10)
    
    # Botón para finalizar la compra
    ttk.Button(content_frame, text="Finalizar Compra", command=finalizar_compra).pack(pady=10)
    ttk.Button(content_frame, text="Cancelar", command=inicio_tienda).pack(pady=10)

#Emergencia Veterinaria
#--------------------------------------------------------------------------

def efectivo(cliente, mascota):
    messagebox.showinfo("Factura", f"*|* Cliente     *|* {cliente} \n\n*|* Animal      *|* {mascota} \n\n*|* Monto total *|* 32000$")
    limpiar_frame(content_frame)
    frame_ef = ttk.Frame(content_frame)
    frame_ef.pack(pady=10)
    ttk.Label(frame_ef, text="Pago efectuado", font=("Arial", 14)).pack(anchor="center")
    ttk.Button(frame_ef, text="Volver a Emergencia Veterinaria", command=emergencia).pack(pady=10)

def tarjeta(cliente, mascota):
    messagebox.showinfo("Factura", f"*|* Cliente     *|* {cliente} \n\n*|* Animal      *|* {mascota} \n\n*|* Monto total *|* 30000$")
    limpiar_frame(content_frame)
    frame_tar = ttk.Frame(content_frame)
    frame_tar.pack(pady=10)
    ttk.Label(frame_tar, text="Pago efectuado", font=("Arial", 14)).pack(anchor="center")
    ttk.Button(frame_tar, text="Volver a Emergencia Veterinaria", command=emergencia).pack(pady=10)

def puntos(cliente, mascota):
    messagebox.showinfo("Factura", f"*|* Cliente     *|* {cliente} \n\n*|* Animal      *|* {mascota} \n\n*|* Monto total *|* 28000$")
    limpiar_frame(content_frame)
    frame_pun = ttk.Frame(content_frame)
    frame_pun.pack(pady=10)
    ttk.Label(frame_pun, text="Pago efectuado", font=("Arial", 14)).pack(anchor="center")
    ttk.Button(frame_pun, text="Volver a Emergencia Veterinaria", command=emergencia).pack(pady=10)


def pagar(cliente, mascota):
    limpiar_frame(content_frame)

    frame_pagar = ttk.Frame(content_frame)
    frame_pagar.pack(pady=10)

    ttk.Button(frame_pagar, text="Pago con efectivo", command=lambda: efectivo(cliente, mascota)).pack(pady=5)
    ttk.Button(frame_pagar, text="Pago con tarjeta", command=lambda: tarjeta(cliente, mascota)).pack(pady=5)
    ttk.Button(frame_pagar, text="Descuento de puntos", command=lambda: puntos(cliente, mascota)).pack(pady=5)

def continuar_proceso(cliente, centro, mascota, sintomas):
    limpiar_frame(content_frame)

    frame_cont_pro = ttk.Frame(content_frame)
    frame_cont_pro.pack(pady=10)

    sintomas_m = sintomas.split(" ") 
    lista_sintomas = []
    for sintoma in sintomas_m:
        if sintoma != "y":
            lista_sintomas.append(sintoma)
            
    ttk.Label(frame_cont_pro, text=f"Su mascota {mascota.getNombre()} con síntomas {lista_sintomas}", font=("Arial", 14)).pack(pady=5)
    ttk.Label(frame_cont_pro, text=f"ha sido hospitalizada en {centro.getNombre()}", font=("Arial", 14)).pack(pady=5)
    ttk.Button(frame_cont_pro, text="Continuar al pago", command=lambda: pagar(cliente, mascota)).pack(pady=5)

def registrar_mascota(cliente, centro, nombre, especie, edad, sexo, tamaño, peso, sintomas):
    
    if not nombre or not especie or not edad or not sexo or not tamaño or not peso or not sintomas:
            messagebox.showerror("Error", "Todos los campos deben ser completados")
    else:
        if tamaño == "Miniatura":
            tamaño_mascota = 1
        elif tamaño == "Pequeño":
            tamaño_mascota = 2
        elif tamaño == "Mediano":
            tamaño_mascota = 3
        else:
            tamaño_mascota = 4

        mascota = Mascota(nombre, especie, int(edad), sexo, EstadoSalud.ENFERMO, tamaño_mascota, float(peso))

        boton_continuar = ttk.Button(content_frame, text="Continuar", command=lambda: continuar_proceso(cliente, centro, mascota, sintomas))
        boton_continuar.pack(pady=2)


def registro_mascota(cliente, centro):
    limpiar_frame(content_frame)

    frame_reg_mas = ttk.Frame(content_frame)
    frame_reg_mas.pack(pady=10)

    etiqueta_info_2 = ttk.Label(frame_reg_mas, text="Ingrese los datos de su mascota:", font=("Arial", 14))
    etiqueta_info_2.pack(pady=1)

    etiqueta_nombre_mascota = ttk.Label(frame_reg_mas, text="Nombre:", font=("Arial", 14))
    etiqueta_nombre_mascota.pack()
    entry_nombre_mascota = ttk.Entry(frame_reg_mas)
    entry_nombre_mascota.pack(pady=1)

    etiqueta_especie = ttk.Label(frame_reg_mas, text="Especie", font=("Arial", 14))
    etiqueta_especie.pack(pady=1)
    especie_var = tk.StringVar()
    opciones_especie = ["Perro", "Gato"]
    menu_especie = tk.OptionMenu(frame_reg_mas, especie_var, *opciones_especie)
    menu_especie.pack(pady=1)

    etiqueta_edad_mascota = ttk.Label(frame_reg_mas, text="Edad (Años):", font=("Arial", 14))
    etiqueta_edad_mascota.pack()
    entry_edad_mascota = ttk.Entry(frame_reg_mas)
    entry_edad_mascota.pack(pady=1)

    etiqueta_sexo = ttk.Label(frame_reg_mas, text="Sexo", font=("Arial", 14))
    etiqueta_sexo.pack(pady=1)
    sexo_var = tk.StringVar()
    opciones_sexo = ["Macho", "Hembra"]
    menu_sexo = tk.OptionMenu(frame_reg_mas, sexo_var, *opciones_sexo)
    menu_sexo.pack(pady=1)

    etiqueta_tamaño = ttk.Label(frame_reg_mas, text="Tamaño", font=("Arial", 14))
    etiqueta_tamaño.pack(pady=1)
    tamaño_var = tk.StringVar()
    opciones_tamaño = ["Miniatura", "Pequeño", "Mediano", "Grande"]
    menu_tamaño = tk.OptionMenu(frame_reg_mas, tamaño_var, *opciones_tamaño)
    menu_tamaño.pack(pady=1)

    etiqueta_peso = ttk.Label(frame_reg_mas, text="Peso en kg:", font=("Arial", 14))
    etiqueta_peso.pack()
    entry_peso = ttk.Entry(frame_reg_mas)
    entry_peso.pack(pady=1)

    etiqueta_sintomas = ttk.Label(frame_reg_mas, text="Síntomas:", font=("Arial", 14))
    etiqueta_sintomas.pack()
    entry_sintomas = tk.Entry(frame_reg_mas)
    entry_sintomas.pack(pady=1)

    boton_registrar_mascota = ttk.Button(frame_reg_mas, text="Registrar", command=lambda: registrar_mascota(cliente, centro, entry_nombre_mascota.get(), especie_var.get(), entry_edad_mascota.get(), sexo_var.get(), tamaño_var.get(), entry_peso.get(), entry_sintomas.get()))
    boton_registrar_mascota.pack(pady=2)



def seleccion_sede(cliente, sede):
    if not sede:
            messagebox.showerror("Error", "Seleccione una sede")
    else:
        centro1 = CentroAdopcion(sede)

        if sede != "":
            boton_2 = ttk.Button(content_frame, text="Continuar", command=lambda: registro_mascota(cliente, centro1))
            boton_2.pack(pady=10)


def mostrar_formulario_sedes_emer(cliente):
    limpiar_frame(content_frame)

    sede_var = tk.StringVar()

    frame_sede = ttk.Frame(content_frame)
    frame_sede.pack(pady=10)
    ttk.Label(frame_sede, text="Seleccione una sede:", font=("Arial", 18)).pack(pady=10)
    opciones_sedes = obtener_sedes()
    menu_sedes = tk.OptionMenu(content_frame, sede_var, *opciones_sedes)
    menu_sedes.pack(pady=5)
    
    ttk.Button(frame_sede, text="Seleccionar Sede", command=lambda: seleccion_sede(cliente,sede_var.get())).pack(pady=10)

def registrar(nombre, edad, cedula):
    if not nombre or not edad or not cedula:
            messagebox.showerror("Error", "Todos los campos deben ser completados.")
    else:
        cliente1 = Cliente(nombre, edad, cedula)

        boton_registro_cliente = ttk.Button(content_frame, text="Continuar", command=lambda: mostrar_formulario_sedes_emer(cliente1))
        boton_registro_cliente.pack(pady=10)


def registro_cliente():

    limpiar_frame(content_frame)

    frame_reg = ttk.Frame(content_frame)
    frame_reg.pack(pady=10)

    etiqueta_info = ttk.Label(frame_reg, text="Ingrese sus datos", font=("Arial", 14))
    etiqueta_info.pack(pady=5)

    etiqueta_nombre = ttk.Label(frame_reg, text="Nombre:", font=("Arial", 14))
    etiqueta_nombre.pack(pady=5)
    entry_nombre = ttk.Entry(frame_reg)
    entry_nombre.pack(pady=5)

    etiqueta_edad = ttk.Label(frame_reg, text="Edad:", font=("Arial", 14))
    etiqueta_edad.pack(pady=5)
    entry_edad = ttk.Entry(frame_reg)
    entry_edad.pack(pady=5)

    etiqueta_cedula = ttk.Label(frame_reg, text="Cédula:", font=("Arial", 14))
    etiqueta_cedula.pack(pady=5)
    entry_cedula = ttk.Entry(frame_reg)
    entry_cedula.pack(pady=5)

        
    boton_registrar = ttk.Button(frame_reg, text="Registrar", command=lambda: registrar(entry_nombre.get(), entry_edad.get(), entry_cedula.get()))
    boton_registrar.pack(pady=5)


def emergencia():

    limpiar_frame(content_frame)
    frame_emer = ttk.Frame(content_frame)
    frame_emer.pack(pady=10)

    bienvenida = ttk.Label(frame_emer, text="Bienvenido a Emergencia Veterinaria", font=("Arial", 14))
    bienvenida.pack(pady=5)

    boton = ttk.Button(frame_emer, text="Continuar", command=registro_cliente)
    boton.pack(pady=30)

#----------------------------------------------------------------------------------------------
memorial = Memorial(CentroAdopcion("Centro de Ejemplo"))

def gestionar_memorial():

    def registro():
        for widget in content_frame.winfo_children():
            widget.destroy()
        
        tk.Label(content_frame, text="Servicio Memorial", font=("Arial", 18)).pack(pady=10)
        tk.Label(content_frame, text="Ingrese sus datos", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(content_frame, text="Nombre Completo:", font=("Arial", 14)).pack()
        entry_nombre = tk.Entry(content_frame)
        entry_nombre.pack()
        
        tk.Label(content_frame, text="Edad:", font=("Arial", 14)).pack()
        entry_edad = tk.Entry(content_frame)
        entry_edad.pack()
        
        tk.Label(content_frame, text="Cédula:", font=("Arial", 14)).pack()
        entry_cedula = tk.Entry(content_frame)
        entry_cedula.pack()
        
        def continuar():
            nombre_cliente = entry_nombre.get()
            edad_cliente = entry_edad.get()
            cedula_cliente = entry_cedula.get()
            if not nombre_cliente or not edad_cliente or not cedula_cliente:
                messagebox.showwarning("Error", "Ingrese valores válidos.")
                return
            gestionar_opciones()
        
        tk.Button(content_frame, text="Continuar", command=continuar).pack(pady=10)

    def gestionar_opciones():
        for widget in content_frame.winfo_children():
            widget.destroy()
        
        tk.Label(content_frame, text="¿Qué desea hacer?", font=("Arial", 18)).pack(pady=10)
        tk.Button(content_frame, text="Añadir Memorial", command=anadir_memorial).pack(pady=5)
        tk.Button(content_frame, text="Ver Memorial", command=ver_memorial).pack(pady=5)
        tk.Button(content_frame, text="Decorar Memorial", command=decorar_memorial).pack(pady=5)
        tk.Button(content_frame, text="Volver al Menú Principal", command=registro).pack(pady=10)

    def anadir_memorial():
        for widget in content_frame.winfo_children():
            widget.destroy()
        
        tk.Label(content_frame, text="Añadir Memorial", font=("Arial", 18)).pack(pady=10)
        tk.Label(content_frame, text="Nombre del Fallecido:", font=("Arial", 14)).pack()
        entry_nombre_fallecido = tk.Entry(content_frame)
        entry_nombre_fallecido.pack()
        
        tk.Label(content_frame, text="Especie:", font=("Arial", 14)).pack()
        entry_especie = tk.Entry(content_frame)
        entry_especie.pack()
        
        tk.Label(content_frame, text="Edad de la mascota:", font=("Arial", 14)).pack()
        entry_edad_mascota = tk.Entry(content_frame)
        entry_edad_mascota.pack()
        
        tk.Label(content_frame, text="Fecha de Fallecimiento (YYYY-MM-DD):", font=("Arial", 14)).pack()
        entry_fecha = tk.Entry(content_frame)
        entry_fecha.pack()
        
        tk.Label(content_frame, text="Seleccione un mensaje:", font=("Arial", 14)).pack()
        mensaje_var = tk.StringVar()
        mensaje_var.set("Descansa en paz")
        mensajes = ["Descansa en paz", "Siempre en nuestros corazones", "Nunca te olvidaremos"]
        tk.OptionMenu(content_frame, mensaje_var, *mensajes).pack()
        
        tk.Label(content_frame, text="Tipo de memorial:", font=("Arial", 14)).pack()
        tipo_var = tk.StringVar()
        tipo_var.set("Tumba")
        tipos = ["Tumba", "Osario", "Cenizas", "Arbol"]
        tk.OptionMenu(content_frame, tipo_var, *tipos).pack()
        
        def guardar_memorial():
            nombre_fallecido = entry_nombre_fallecido.get()
            especie_fallecido = entry_especie.get()
            edad_mascota = entry_edad_mascota.get()
            fecha = entry_fecha.get()
            mensaje = mensaje_var.get()
            tipo = tipo_var.get()
            
            if not nombre_fallecido or not especie_fallecido or not edad_mascota or not fecha:
                messagebox.showwarning("Error", "Por favor complete todos los campos.")
                return
            
            mascota = Mascota(nombre_fallecido, especie_fallecido, int(edad_mascota), None, None, 0, 0) 
            fallecido = Fallecido(mascota, fecha, mensaje, None, "", tipo)
            memorial.anadir_fallecido(fallecido, tipo)
            messagebox.showinfo("Éxito", "Memorial añadido correctamente.")
            gestionar_opciones()
        
        tk.Button(content_frame, text="Guardar Memorial", command=guardar_memorial).pack(pady=10)
        tk.Button(content_frame, text="Volver", command=gestionar_opciones).pack(pady=5)
    
    def ver_memorial():
        for widget in content_frame.winfo_children():
            widget.destroy()
        
        tk.Label(content_frame, text="Ver Memorial", font=("Arial", 18)).pack(pady=10)
        tipo_var = tk.StringVar()
        tipo_var.set("Tumba")
        tipos = ["Tumba", "Osario", "Cenizas", "Arbol"]
        tk.OptionMenu(content_frame, tipo_var, *tipos).pack()
        
        def mostrar_memorial():
            tipo = tipo_var.get()
            registros = memorial.obtener_fallecidos_por_tipo(tipo)
            
            if not registros:
                messagebox.showinfo("Memorial", "No hay registros en esta categoría.")
            else:
                resultado = "\n".join([str(f) for f in registros])
                messagebox.showinfo(f"Registros en {tipo}", resultado)
        
        tk.Button(content_frame, text="Ver", command=mostrar_memorial).pack(pady=10)
        tk.Button(content_frame, text="Volver", command=gestionar_opciones).pack(pady=5)
    
    def decorar_memorial():
        for widget in content_frame.winfo_children():
            widget.destroy()
    
        tk.Label(content_frame, text="Decorar Memorial", font=("Arial", 18)).pack(pady=10)
    
        tk.Label(content_frame, text="Seleccione el tipo de memorial:", font=("Arial", 14)).pack()
        tipo_var = tk.StringVar()
        tipo_var.set("Tumba")
        tipos = ["Tumba", "Osario", "Cenizas", "Árbol"]
        tk.OptionMenu(content_frame, tipo_var, *tipos).pack()
    
        def seleccionar_memorial():
            tipo = tipo_var.get()
            registros = memorial.obtener_fallecidos_por_tipo(tipo)

            if not registros:
                messagebox.showinfo("Memorial", "No hay registros en esta categoría.")
                return
        
            seleccion_index = tk.IntVar()
            seleccion_index.set(0)
        
            opciones_nombres = [f.get_mascota().getNombre() for f in registros]
            tk.OptionMenu(content_frame, seleccion_index, *range(len(opciones_nombres))).pack()

            tk.Label(content_frame, text="Ingrese una flor:", font=("Arial", 14)).pack()
            entry_flor = tk.Entry(content_frame)
            entry_flor.pack()
        
            def agregar_flor():
                flor = entry_flor.get()
                index = seleccion_index.get()

                if not flor:
                    messagebox.showwarning("Error", "Ingrese una flor válida.")
                    return
            
                fallecido = registros[index]
                mensaje = fallecido.poner_flor(flor)
                messagebox.showinfo("Decoración", mensaje)
        
            tk.Button(content_frame, text="Añadir Flor", command=agregar_flor).pack(pady=10)
    
        tk.Button(content_frame, text="Seleccionar Memorial", command=seleccionar_memorial).pack(pady=10)
        tk.Button(content_frame, text="Volver", command=gestionar_opciones).pack(pady=5)
    
    
    registro()

#Planeacion Dieta
#-----------------------------------------------------------------------------------------------

def mostrar_formulario_dietas():
    for widget in content_frame.winfo_children():
        widget.destroy()

    #Formulario para crear el objeto Mascota 

    tk.Label(content_frame, text="Planificación de Dieta", font=("Arial", 18, "bold")).pack(pady=10)

    tk.Label(content_frame, text="Nombre de la mascota:").pack()
    entry_nombre = tk.Entry(content_frame)
    entry_nombre.pack()

    tk.Label(content_frame, text="Especie:").pack()
    especie_var = tk.StringVar()
    opciones_especie = ["Perro", "Gato"]
    tk.OptionMenu(content_frame, especie_var, *opciones_especie).pack()

    tk.Label(content_frame, text="Edad (años):").pack()
    entry_edad = tk.Entry(content_frame)
    entry_edad.pack()

    tk.Label(content_frame, text="Sexo:").pack()
    sexo_var = tk.StringVar()
    opciones_sexo = ["Macho", "Hembra"]
    tk.OptionMenu(content_frame, sexo_var, *opciones_sexo).pack()

    tk.Label(content_frame, text="Tamaño:").pack()
    tamano_var = tk.StringVar()
    opciones_tamano = ["Miniatura", "Pequeño", "Mediano", "Grande"]
    tk.OptionMenu(content_frame, tamano_var, *opciones_tamano).pack()

    tk.Label(content_frame, text="Peso en kg:").pack()
    entry_peso = tk.Entry(content_frame)
    entry_peso.pack()
    especie = especie_var.get()

    def calcular_dieta():
        #Capturar datos del formulario en variables
        try:
            nombre = entry_nombre.get()
            especie = especie_var.get()
            sexo = sexo_var.get()
            if tamano_var.get() == "Miniatura":
                tamano = 1
            elif tamano_var.get() == "Pequeño":
                tamano = 2
            elif tamano_var.get() == "Mediano":
                tamano = 3
            else:
                tamano = 4
            edad = int(entry_edad.get())
            peso = float(entry_peso.get())
            if not nombre or not especie or not edad or not sexo or not tamano or not peso:
                messagebox.showwarning("Error", "Por favor seleccione valores válidos.")
                return
            # Crear objeto Mascota
            mascota = Mascota(nombre, especie, edad, sexo, EstadoSalud.SANO , tamano, peso)

            # Crear y calcular dieta
            dieta = Dieta(mascota)
            dieta.calcularPesoIdeal()
            dieta.planDieta()
            dieta.menu()
            messagebox.showinfo(f"Plan de dieta", f"{dieta}")

            # Preguntar si desea continuar a la tienda
            continuar = messagebox.askyesno("Continuar", "¿Desea continuar a la tienda de dietas BARF?")
            if continuar:
                inicio_tienda_dietas(especie)
            else:
                mostrar_interfaz_inicial(content_frame)

        except ValueError:
            messagebox.showwarning("Error", "Ingrese valores numéricos válidos.")

    tk.Button(content_frame, text="Calcular Dieta", command=calcular_dieta).pack(pady=10)
    
#Mini tienda de productos dieta BARF
    def inicio_tienda_dietas(especie):
        limpiar_frame(content_frame)

        # Cargar productos desde el archivo serializado
        productosBarf = cargar_datos_productos2()

        if not productosBarf:
            messagebox.showwarning("Error", "No se encontraron productos disponibles.")
            mostrar_interfaz_inicial(content_frame)
            return
        
    #Formulario para realizar la compra en gramos de distintos Dieta Barf para perros y gatos
        ttk.Label(content_frame, text=f"Tienda de Dietas BARF para {especie}s", font=("Arial", 18)).pack(pady=20)
        ttk.Label(content_frame, text="Seleccione un producto:", font=("Arial", 14)).pack(pady=10)

        producto_var = tk.StringVar()
        productos_combobox = ttk.Combobox(
            content_frame,
            textvariable=producto_var,
            values=[f"{p.nombre} - ${p.precio} por gramo" for p in productosBarf],
            state="readonly",
            width=60
        )
        productos_combobox.pack(pady=10)

        ttk.Label(content_frame, text="Cantidad en gramos:", font=("Arial", 14)).pack(pady=10)
        cantidad_var = tk.IntVar()
        cantidad_entry = ttk.Entry(content_frame, textvariable=cantidad_var)
        cantidad_entry.pack(pady=10)

        ttk.Label(content_frame, text="Ingrese sus datos:", font=("Arial", 14)).pack(pady=10)
    
        ttk.Label(content_frame, text="Nombre:", font=("Arial", 12)).pack(pady=5)
        nombre_entry = ttk.Entry(content_frame)
        nombre_entry.pack(pady=5)
        
        ttk.Label(content_frame, text="Cédula:", font=("Arial", 12)).pack(pady=5)
        cedula_entry = ttk.Entry(content_frame)
        cedula_entry.pack(pady=5)
        
        #Consumacion de la compra y factura electronica.
        def confirmar_compra():
            producto_seleccionado = producto_var.get()
            cantidad = int(cantidad_var.get())
            nombre = nombre_entry.get()
            cedula = cedula_entry.get()

            if not producto_seleccionado or cantidad <= 0 or not nombre or not cedula:
                messagebox.showwarning("Error", "Por favor complete todos los campos correctamente.")
                return

            nombre_producto = producto_seleccionado.split(" - ")[0]
            producto = next((p for p in productosBarf if p.nombre == nombre_producto), None)

            if producto:
                cliente = Cliente(nombre,18, cedula)
                messagebox.showinfo("Factura Electrónica", 
                                    f"FACTURA ELECTRONICA\n{producto.nombre} x {cantidad}g.\nCliente: {cliente.nombre}\nDocumento: {cliente.cedula}\nMuchas Gracias por comprar en UNmascota! Vuelva pronto")
                mostrar_interfaz_inicial(content_frame)
            else:
                messagebox.showwarning("Error", "Producto no encontrado.")

        frame_botones = ttk.Frame(content_frame)
        frame_botones.pack(pady=10)

        ttk.Button(frame_botones, text="Confirmar Compra", command=confirmar_compra).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Cancelar", command=mostrar_formulario_dietas).pack(side="right", padx=5)

#-----------------------------------------------------------------------------------------------
def mostrar_formulario_registro():
    for widget in content_frame.winfo_children():
        widget.destroy()

    def registrar():
        nombre = entry_nombre.get()
        edad = entry_edad.get()
        cedula = entry_cedula.get()
        if nombre and edad and cedula:
            messagebox.showinfo("Registro Exitoso", f"Nombre: {nombre}, Edad: {edad}, Cédula: {cedula}")
            mostrar_formulario_mascota()
        else:
            messagebox.showwarning("Registro Incompleto", "Debe completar todos los campos.")

    etiqueta_nombre = tk.Label(content_frame, text="Nombre:", font=("Arial", 14))
    etiqueta_nombre.grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(content_frame, font=("Arial", 14))
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    etiqueta_edad = tk.Label(content_frame, text="Edad:", font=("Arial", 14))
    etiqueta_edad.grid(row=1, column=0, padx=5, pady=5)
    entry_edad = tk.Entry(content_frame, font=("Arial", 14))
    entry_edad.grid(row=1, column=1, padx=5, pady=5)

    etiqueta_cedula = tk.Label(content_frame, text="Cédula:", font=("Arial", 14))
    etiqueta_cedula.grid(row=2, column=0, padx=5, pady=5)
    entry_cedula = tk.Entry(content_frame, font=("Arial", 14))
    entry_cedula.grid(row=2, column=1, padx=5, pady=5)

    boton_registrar = tk.Button(content_frame, text="Registrar", command=registrar)
    boton_registrar.grid(row=3, column=0, columnspan=2, pady=10)
# Función para mostrar el formulario de la mascota
def mostrar_formulario_mascota():
    for widget in content_frame.winfo_children():
        widget.destroy()

    def registrar_mascota():
        nombre_mascota = entry_nombre_mascota.get()
        edad_mascota = entry_edad_mascota.get()
        especie_mascota = especie_var.get()
        genero_mascota = genero_var.get()
        if nombre_mascota and edad_mascota and especie_mascota and genero_mascota:
            messagebox.showinfo("Registro Exitoso", f"Nombre: {nombre_mascota}, Edad: {edad_mascota}, Especie: {especie_mascota}, Género: {genero_mascota}")
            messagebox.showinfo("Proceso Completado")
        else:
            messagebox.showwarning("Registro Incompleto", "Debe completar todos los campos.")

    etiqueta_nombre_mascota = tk.Label(content_frame, text="Nombre de la Mascota:", font=("Arial", 14))
    etiqueta_nombre_mascota.grid(row=0, column=0, padx=5, pady=5)
    entry_nombre_mascota = tk.Entry(content_frame, font=("Arial", 14))
    entry_nombre_mascota.grid(row=0, column=1, padx=5, pady=5)

    etiqueta_edad_mascota = tk.Label(content_frame, text="Edad de la Mascota (meses):", font=("Arial", 14))
    etiqueta_edad_mascota.grid(row=1, column=0, padx=5, pady=5)
    entry_edad_mascota = tk.Entry(content_frame, font=("Arial", 14))
    entry_edad_mascota.grid(row=1, column=1, padx=5, pady=5)

    etiqueta_especie_mascota = tk.Label(content_frame, text="Especie de la Mascota:", font=("Arial", 14))
    etiqueta_especie_mascota.grid(row=2, column=0, padx=5, pady=5)
    especie_var = tk.StringVar()
    opciones_especie = ["Perro", "Gato", "Conejo", "Hámster"]
    menu_especie = tk.OptionMenu(content_frame, especie_var, *opciones_especie)
    menu_especie.grid(row=2, column=1, padx=5, pady=5)

    etiqueta_genero_mascota = tk.Label(content_frame, text="Género de la Mascota:", font=("Arial", 14))
    etiqueta_genero_mascota.grid(row=3, column=0, padx=5, pady=5)
    genero_var = tk.StringVar()
    opciones_genero = ["Macho", "Hembra"]
    menu_genero = tk.OptionMenu(content_frame, genero_var, *opciones_genero)
    menu_genero.grid(row=3, column=1, padx=5, pady=5)

    boton_registrar_mascota = tk.Button(content_frame, text="Registrar Mascota", command=registrar_mascota)
    boton_registrar_mascota.grid(row=4, column=0, columnspan=2, pady=10)


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
def return_to_initial(master, main_window):
    master.destroy()
    main_window.deiconify()

def mostrar_interfaz_inicial(content_frame):
    limpiar_frame(content_frame)

    ttk.Label(content_frame, text="Bienvenido a la Aplicación", font=("Arial", 24, "bold"), foreground="#004080").pack(pady=20)

    ttk.Label(
        content_frame, 
        text="Seleccione una de las opciones del menú para acceder a diferentes procesos y servicios.",
        font=("Arial", 14), 
        justify=tk.CENTER,
        wraplength=600
    ).pack(pady=20)

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

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
archivo_menu = tk.Menu(menu_bar, tearoff=0)
archivo_menu.add_command(label="Aplicacion", command=mostrar_info_aplicacion)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=salir_aplicacion)
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)


procesos_menu = tk.Menu(menu_bar, tearoff=0)
procesos_menu.add_command(label="Tienda UNamascota", command=lambda: manejar_seleccion_proceso("Proceso 1"))
procesos_menu.add_command(label="Agendar UNservicio", command=lambda: manejar_seleccion_proceso("Proceso 2"))
procesos_menu.add_command(label="UNaemergencia o.o", command=lambda: manejar_seleccion_proceso("Proceso 3"))
procesos_menu.add_command(label="Adquirir UNmemorial", command=lambda: manejar_seleccion_proceso("Proceso 4"))
procesos_menu.add_command(label="Planificar UNadieta", command=lambda: manejar_seleccion_proceso("Proceso 5"))
menu_bar.add_cascade(label="Procesos y Consultas", menu=procesos_menu)


# Menú Ayuda
ayuda_menu = tk.Menu(menu_bar, tearoff=0)
ayuda_menu.add_command(label="Acerca de", command=mostrar_info_autores)
menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)

root.config(menu=menu_bar)

content_frame = ttk.Frame(main_frame, padding=20, relief="ridge", borderwidth=2)
content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Inicializar agendador globalmente
global agendador
agendador = inicializar_agendador()

mostrar_interfaz_inicial(content_frame)

root.mainloop()