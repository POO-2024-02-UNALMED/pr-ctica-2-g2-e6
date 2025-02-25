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
    
    ttk.Label(content_frame, text="Bienvenido a la Aplicación", font=("Arial", 24, "bold"), foreground="#004080").grid(row=0, column=0, pady=20, columnspan=3)

    ttk.Label(
        content_frame, 
        text="Seleccione una de las opciones del menú para acceder a diferentes procesos y servicios.",
        font=("Arial", 14), 
        justify=tk.CENTER,
        wraplength=600
    ).grid(row=1, column=0, pady=20, columnspan=3)

# ===========================
# SELECCIÓN DE PROCESO
# ===========================
def manejar_seleccion_proceso(proceso):
    limpiar_frame(content_frame)
    
    field_frame_proceso = FieldFrame(content_frame, "Proceso Seleccionado", [proceso], "")
    field_frame_proceso.pack(pady=10)

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

    opciones_sedes = obtener_sedes()
    field_frame_sede = FieldFrame(content_frame, "Seleccione una sede", ["Sede"], "Valor")
    field_frame_sede.pack(pady=10)
    field_frame_sede.agregar_combobox("Sede", opciones_sedes)

    field_frame_sede.crearBotones(lambda: seleccionar_servicio(field_frame_sede.getValue("Sede"), field_frame_sede), "Seleccionar Sede", pady=10, column=1, padx=5)

def seleccionar_servicio(sede, field_frame_sede):
    limpiar_frame(content_frame)
    if sede not in obtener_sedes():
        messagebox.showwarning("Error", "Seleccione una sede válida.")
        return
    
    opciones_servicios = obtener_servicios(sede)
    field_frame_servicio = FieldFrame(content_frame, "Seleccione un servicio", ["Servicio"], "Valor")
    field_frame_servicio.pack(pady=10)
    field_frame_servicio.agregar_combobox("Servicio", opciones_servicios)

    def verificar_disponibilidad_action():
        servicio = field_frame_servicio.getValue("Servicio")
        if servicio:
            disponibilidad = verificar_disponibilidad(agendador, sede, servicio)
            if disponibilidad:
                confirmar_raza(sede, servicio, field_frame_servicio)
            else:
                messagebox.showwarning("Sin disponibilidad", "No hay disponibilidad para el servicio seleccionado.")
        else:
            messagebox.showwarning("Selección Incorrecta", "Debe seleccionar un servicio válido.")

    field_frame_servicio.crearBotones(verificar_disponibilidad_action, "Seleccionar Servicio", pady=10, column=1, padx=5)
    field_frame_servicio.crearBotones(mostrar_formulario_sedes, "Cancelar", pady=10, column=2, padx=5)

# ===========================
# CONFIRMAR RAZA
# ===========================
def confirmar_raza(sede, servicio, field_frame_servicio):
    limpiar_frame(content_frame)

    razas_disponibles = []
    precio = 0

    if servicio == "Entrenamiento":
        razas_disponibles = ["Perro", "Gato"]
        precio = 100
    elif servicio == "Peluquería":
        razas_disponibles = ["Perro", "Gato"]
        precio = 50
    elif servicio == "Veterinaria":
        razas_disponibles = ["Perro", "Gato", "Ave", "Conejo"]
        precio = 70

    field_frame_raza = FieldFrame(content_frame, "Su mascota pertenece a:", ["Raza"], "Valor")
    field_frame_raza.pack(pady=10)
    field_frame_raza.agregar_combobox("Raza", razas_disponibles)

    def confirmar_raza_action():
        raza = field_frame_raza.getValue("Raza")
        if raza in razas_disponibles:
            seleccionar_empleado(sede, servicio, field_frame_raza)
        else:
            messagebox.showwarning("Selección Incorrecta", "Debe seleccionar una raza válida.")

    field_frame_raza.crearBotones(confirmar_raza_action, "Confirmar Raza", pady=10, column=1, padx=5)
    field_frame_raza.crearBotones(lambda: seleccionar_servicio(sede, field_frame_servicio), "Cancelar", pady=10, column=2, padx=5)

# ===========================
# SELECCIONAR EMPLEADO
# ===========================
def seleccionar_empleado(sede, servicio, field_frame_raza):
    limpiar_frame(content_frame)

    empleados_disponibles = obtener_empleados_disponibles(agendador, sede)
    nombres_empleados = [empleado.nombre for empleado in empleados_disponibles]

    field_frame_empleado = FieldFrame(content_frame, "Seleccione un empleado", ["Empleado"], "Valor")
    field_frame_empleado.pack(pady=10)
    field_frame_empleado.agregar_combobox("Empleado", nombres_empleados)

    def seleccionar_cupo():
        nombre_empleado = field_frame_empleado.getValue("Empleado")
        empleado = next((emp for emp in empleados_disponibles if emp.nombre == nombre_empleado), None)
        if empleado:
            seleccionar_cupo_dia(sede, servicio, empleado, field_frame_raza, field_frame_empleado)
        else:
            messagebox.showwarning("Selección Incorrecta", "Debe seleccionar un empleado válido.")

    field_frame_empleado.crearBotones(seleccionar_cupo, "Seleccionar Empleado", pady=10, column=1, padx=5)
    field_frame_empleado.crearBotones(lambda: confirmar_raza(sede, servicio, field_frame_raza), "Cancelar", pady=10, column=2, padx=5)

# ===========================
# SELECCIONAR CUPO POR DÍA
# ===========================
def seleccionar_cupo_dia(sede, servicio, empleado, field_frame_raza, field_frame_empleado):
    limpiar_frame(content_frame)

    opciones_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    field_frame_cupo = FieldFrame(content_frame, "Seleccione un día", ["Día"], "Valor")
    field_frame_cupo.pack(pady=10)
    field_frame_cupo.agregar_combobox("Día", opciones_dias)

    def seleccionar_dia():
        dia = field_frame_cupo.getValue("Día")
        dias_semana = {"Lunes": 0, "Martes": 1, "Miércoles": 2, "Jueves": 3, "Viernes": 4, "Sábado": 5}
        dia_numero = dias_semana.get(dia)
        if dia_numero is not None:
            cupos_disponibles = empleado.cupos_disponibles(dia_numero)
            if cupos_disponibles:
                confirmar_cupo(sede, servicio, empleado, cupos_disponibles, field_frame_cupo,field_frame_empleado)
            else:
                messagebox.showwarning("Sin disponibilidad", "No hay cupos disponibles para el día seleccionado.")
        else:
            messagebox.showwarning("Selección Incorrecta", "Debe seleccionar un día válido.")

    field_frame_cupo.crearBotones(seleccionar_dia, "Seleccionar Día", pady=10, column=1, padx=5)
    field_frame_cupo.crearBotones(lambda: seleccionar_empleado(sede, servicio, field_frame_raza), "Cancelar", pady=10, column=2, padx=5)

# ===========================
# CONFIRMAR CUPO
# ===========================
def confirmar_cupo(sede, servicio, empleado, cupos_disponibles, field_frame_cupo,field_frame_empleado):
    limpiar_frame(content_frame)

    field_frame_confirmar_cupo = FieldFrame(content_frame, "Seleccione un cupo", ["Cupo"], "Valor")
    field_frame_confirmar_cupo.pack(pady=10)
    field_frame_confirmar_cupo.agregar_combobox("Cupo", [f"{c.get_dia()} {c.hora_inicio} - {c.hora_fin}" for c in cupos_disponibles])

    def confirmar_cupo_action():
        cupo_texto = field_frame_confirmar_cupo.getValue("Cupo")
        cupo = next((c for c in cupos_disponibles if f"{c.get_dia()} {c.hora_inicio} - {c.hora_fin}" == cupo_texto), None)
        if cupo:
            ingresarDatosCliente(sede, servicio, empleado, cupo, field_frame_confirmar_cupo, field_frame_empleado)
        else:
            messagebox.showwarning("Selección Incorrecta", "Debe seleccionar un cupo válido.")

    field_frame_confirmar_cupo.crearBotones(confirmar_cupo_action, "Confirmar Cupo", pady=10, column=1, padx=5)
    field_frame_confirmar_cupo.crearBotones(lambda: seleccionar_cupo_dia(sede, servicio, empleado, field_frame_cupo,field_frame_empleado), "Cancelar", pady=10, column=2, padx=5)

# ===========================
# INGRESAR DATOS DEL CLIENTE
# ===========================
def ingresarDatosCliente(sede, servicio, empleado, cupo, field_frame_confirmar_cupo,field_frame_empleado):
    limpiar_frame(content_frame)

    field_frame_cliente = FieldFrame(content_frame, "Datos del Cliente", ["Nombre", "Edad", "Cédula"], "Valor")
    field_frame_cliente.pack(pady=10)

    def confirmar_datos_cliente():
        cliente_data = (
            field_frame_cliente.getValue("Nombre"),
            field_frame_cliente.getValue("Edad"),
            field_frame_cliente.getValue("Cédula")
        )
        ingresar_datos_mascota(sede, servicio, empleado, cupo, cliente_data, field_frame_cliente,field_frame_empleado)

    field_frame_cliente.crearBotones(confirmar_datos_cliente, "Confirmar Datos", pady=10, column=1, padx=5)
    field_frame_cliente.crearBotones(lambda: confirmar_cupo(sede, servicio, empleado, [cupo], field_frame_confirmar_cupo,field_frame_empleado), "Cancelar", pady=10, column=2, padx=5)
# ===========================
# INGRESAR DATOS DE LA MASCOTA
# ===========================
def ingresar_datos_mascota(sede, servicio, empleado, cupo, cliente_data, field_frame_confirmar_cupo, field_frame_empleado):
    limpiar_frame(content_frame)

    field_frame_mascota = FieldFrame(content_frame, "Datos de la Mascota", ["Nombre de la Mascota", "Especie de la Mascota", "Edad de la Mascota (meses)", "Género de la Mascota"], "Valor")
    field_frame_mascota.pack(pady=10)
    field_frame_mascota.setValue("Especie de la Mascota", "Perro")
    field_frame_mascota.disableEntry("Especie de la Mascota")

    def confirmar_datos_mascota():
        mascota_data = (
            field_frame_mascota.getValue("Nombre de la Mascota"),
            field_frame_mascota.getValue("Especie de la Mascota"),
            field_frame_mascota.getValue("Edad de la Mascota (meses)"),
            field_frame_mascota.getValue("Género de la Mascota")
        )
        confirmar_agendamiento(sede, servicio, empleado, cupo, cliente_data, mascota_data, field_frame_mascota)

    field_frame_mascota.crearBotones(confirmar_datos_mascota, "Confirmar Datos", pady=10, column=1, padx=10)
    field_frame_mascota.crearBotones(lambda: ingresarDatosCliente(sede, servicio, empleado, cupo, field_frame_confirmar_cupo, field_frame_empleado), "Cancelar", pady=10, column=2, padx=10)

# ===========================
# CONFIRMAR AGENDAMIENTO
# ===========================
def confirmar_agendamiento(sede, servicio, empleado, cupo, cliente_data, mascota_data, field_frame_mascota):
    limpiar_frame(content_frame)
    
    resultado = agendar_servicio(agendador, sede, servicio, cliente_data, mascota_data, cupo.get_dia().weekday(), cupo.hora_inicio, empleado.nombre)
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
    field_frame_tienda = FieldFrame(content_frame, "Bienvenido a la Tienda", [], "")
    field_frame_tienda.pack(pady=20)

    def comprar():
        limpiar_frame(content_frame)
        field_frame_comprar = FieldFrame(content_frame, "¿Cómo le gustaría mostrar los productos?", [], "")
        field_frame_comprar.pack(pady=10)

        def mostrar_todo():
            limpiar_frame(content_frame)
            field_frame_todo = FieldFrame(content_frame, "Seleccione un producto", ["Producto", "Cantidad"], "Valor")
            field_frame_todo.pack(pady=10)

            productos_valores = [f"{p.nombre} - ${p.precio} ({p.tipo_animal})" for p in productos]
            field_frame_todo.agregar_combobox("Producto", productos_valores)
            field_frame_todo.setValue("Cantidad", 1)

            def confirmar_compra():
                producto_seleccionado = field_frame_todo.getValue("Producto")
                cantidad = int(field_frame_todo.getValue("Cantidad"))

                if not producto_seleccionado or cantidad <= 0:
                    messagebox.showwarning("Error", "Seleccione un producto y una cantidad válida.")
                    return

                nombre_producto = producto_seleccionado.split(" - ")[0]
                producto = next((p for p in productos if p.nombre == nombre_producto), None)

                if producto:
                    ingresar_datos_cliente(producto, cantidad)
                else:
                    messagebox.showwarning("Error", "Producto no encontrado.")

            field_frame_todo.crearBotones(confirmar_compra, "Confirmar Compra", pady=10, column=1, padx=10)
            field_frame_todo.crearBotones(comprar, "Cancelar", pady=10, column=2, padx=10)

        def filtrar_por_tipo():
            limpiar_frame(content_frame)
            field_frame_tipo = FieldFrame(content_frame, "Seleccione el tipo de animal", ["Tipo"], "Valor")
            field_frame_tipo.pack(pady=10)
            field_frame_tipo.agregar_combobox("Tipo", ["Perro", "Gato", "Conejo", "Ave"])

            def mostrar_productos_filtrados():
                tipo_animal = field_frame_tipo.getValue("Tipo")
                if not tipo_animal:
                    messagebox.showwarning("Error", "Seleccione un tipo de animal válido.")
                    return

                productos_filtrados = [p for p in productos if p.tipo_animal == tipo_animal]

                if not productos_filtrados:
                    messagebox.showinfo("Info", f"No hay productos disponibles para {tipo_animal}.")
                    return

                limpiar_frame(content_frame)
                field_frame_filtrado = FieldFrame(content_frame, "Seleccione un producto", ["Producto", "Cantidad"], "Valor")
                field_frame_filtrado.pack(pady=10)

                productos_filtrados_valores = [f"{p.nombre} - ${p.precio}" for p in productos_filtrados]
                field_frame_filtrado.agregar_combobox("Producto", productos_filtrados_valores)
                field_frame_filtrado.setValue("Cantidad", 1)

                def confirmar_compra():
                    producto_seleccionado = field_frame_filtrado.getValue("Producto")
                    cantidad = int(field_frame_filtrado.getValue("Cantidad"))

                    if not producto_seleccionado or cantidad <= 0:
                        messagebox.showwarning("Error", "Seleccione un producto y una cantidad válida.")
                        return

                    nombre_producto = producto_seleccionado.split(" - ")[0]
                    producto = next((p for p in productos_filtrados if p.nombre == nombre_producto), None)

                    if producto:
                        ingresar_datos_cliente(producto, cantidad)
                    else:
                        messagebox.showwarning("Error", "Producto no encontrado.")

                field_frame_filtrado.crearBotones(confirmar_compra, "Confirmar Compra", pady=10, column=1, padx=10)
                field_frame_filtrado.crearBotones(filtrar_por_tipo, "Cancelar", pady=10, column=2, padx=10)

            field_frame_tipo.crearBotones(mostrar_productos_filtrados, "Mostrar Productos", pady=10, column=1, padx=10)
            field_frame_tipo.crearBotones(comprar, "Cancelar", pady=10, column=2, padx=10)

        field_frame_comprar.crearBotones(mostrar_todo, "Mostrar Todo", pady=10, column=1, padx=10)
        field_frame_comprar.crearBotones(filtrar_por_tipo, "Filtrar por Tipo", pady=10, column=2, padx=10)
        field_frame_comprar.crearBotones(inicio_tienda, "Cancelar", pady=10, column=3, padx=10)

    field_frame_tienda.crearBotones(comprar, "Comprar", pady=10, column=1, padx=10)
    field_frame_tienda.crearBotones(root.quit, "Salir", pady=10, column=2, padx=10)

def ingresar_datos_cliente(producto, cantidad):
    limpiar_frame(content_frame)

    field_frame_cliente = FieldFrame(content_frame, "Ingrese sus datos", ["Nombre", "Cédula"], "Valor")
    field_frame_cliente.pack(pady=10)

    def finalizar_compra():
        nombre = field_frame_cliente.getValue("Nombre")
        cedula = field_frame_cliente.getValue("Cédula")

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
        limpiar_frame(content_frame)
        ttk.Label(content_frame, text="Compra Exitosa", font=("Arial", 18)).pack(pady=20)
        ttk.Label(content_frame, text=recibo, font=("Arial", 14)).pack(pady=10)
        
         # Botón para volver al inicio
        ttk.Button(content_frame, text="Volver al Inicio", command=inicio_tienda).pack(pady=10)
    
        field_frame_recibo = FieldFrame(content_frame, "", [], "")
        field_frame_recibo.pack(pady=10)
        field_frame_recibo.crearBotones(lambda: mostrar_interfaz_inicial(content_frame), "Volver al Inicio", pady=10, column=1, padx=10)

    field_frame_cliente.crearBotones(finalizar_compra, "Finalizar Compra", pady=10, column=1, padx=10)
    field_frame_cliente.crearBotones(inicio_tienda, "Cancelar", pady=10, column=2, padx=10)

#=========================
#Emergencia Veterinaria
#=========================

def efectivo(cliente, mascota):
    messagebox.showinfo("Factura", f"*|* Cliente     *|* {cliente} \n\n*|* Animal      *|* {mascota} \n\n*|* Monto total *|* 32000$")
    limpiar_frame(content_frame)
    ttk.Label(content_frame, text="Pago efectuado", font=("Arial", 14)).pack(anchor="center")
    ttk.Button(content_frame, text="Volver a Emergencia Veterinaria", command=emergencia).pack(pady=10)

def tarjeta(cliente, mascota):
    messagebox.showinfo("Factura", f"*|* Cliente     *|* {cliente} \n\n*|* Animal      *|* {mascota} \n\n*|* Monto total *|* 30000$")
    limpiar_frame(content_frame)
    ttk.Label(content_frame, text="Pago efectuado", font=("Arial", 14)).pack(anchor="center")
    ttk.Button(content_frame, text="Volver a Emergencia Veterinaria", command=emergencia).pack(pady=10)

def puntos(cliente, mascota):
    messagebox.showinfo("Factura", f"*|* Cliente     *|* {cliente} \n\n*|* Animal      *|* {mascota} \n\n*|* Monto total *|* 28000$")
    limpiar_frame(content_frame)
    ttk.Label(content_frame, text="Pago efectuado", font=("Arial", 14)).pack(anchor="center")
    ttk.Button(content_frame, text="Volver a Emergencia Veterinaria", command=emergencia).pack(pady=10)


def pagar(cliente, mascota):
    limpiar_frame(content_frame)
    ttk.Button(content_frame, text="Pago con efectivo", command=lambda: efectivo(cliente, mascota)).pack(pady=5)
    ttk.Button(content_frame, text="Pago con tarjeta", command=lambda: tarjeta(cliente, mascota)).pack(pady=5)
    ttk.Button(content_frame, text="Descuento de puntos", command=lambda: puntos(cliente, mascota)).pack(pady=5)

def continuar_proceso(cliente, centro, mascota, sintomas):
    limpiar_frame(content_frame)
    sintomas_m = sintomas.split(" ") 
    lista_sintomas = []
    for sintoma in sintomas_m:
        if sintoma != "y":
            lista_sintomas.append(sintoma)
    ttk.Label(content_frame, text=f"Su mascota {mascota.getNombre()} con síntomas {lista_sintomas} \nha sido hospitalizada en {centro.getNombre()}", font=("Arial", 14)).pack(pady=5)
    ttk.Button(content_frame, text="Continuar al pago", command=lambda: pagar(cliente, mascota)).pack(pady=5)

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

    etiqueta_info_2 = ttk.Label(content_frame, text="Ingrese los datos de su mascota:", font=("Arial", 14))
    etiqueta_info_2.pack(pady=1)

    etiqueta_nombre_mascota = ttk.Label(content_frame, text="Nombre:", font=("Arial", 14))
    etiqueta_nombre_mascota.pack()
    entry_nombre_mascota = ttk.Entry(content_frame)
    entry_nombre_mascota.pack(pady=1)

    etiqueta_especie = ttk.Label(content_frame, text="Especie", font=("Arial", 14))
    etiqueta_especie.pack(pady=1)
    especie_var = tk.StringVar()
    opciones_especie = ["Perro", "Gato"]
    menu_especie = tk.OptionMenu(content_frame, especie_var, *opciones_especie)
    menu_especie.pack(pady=1)

    etiqueta_edad_mascota = ttk.Label(content_frame, text="Edad (Años):", font=("Arial", 14))
    etiqueta_edad_mascota.pack()
    entry_edad_mascota = ttk.Entry(content_frame)
    entry_edad_mascota.pack(pady=1)

    etiqueta_sexo = ttk.Label(content_frame, text="Sexo", font=("Arial", 14))
    etiqueta_sexo.pack(pady=1)
    sexo_var = tk.StringVar()
    opciones_sexo = ["Macho", "Hembra"]
    menu_sexo = tk.OptionMenu(content_frame, sexo_var, *opciones_sexo)
    menu_sexo.pack(pady=1)

    etiqueta_tamaño = ttk.Label(content_frame, text="Tamaño", font=("Arial", 14))
    etiqueta_tamaño.pack(pady=1)
    tamaño_var = tk.StringVar()
    opciones_tamaño = ["Miniatura", "Pequeño", "Mediano", "Grande"]
    menu_tamaño = tk.OptionMenu(content_frame, tamaño_var, *opciones_tamaño)
    menu_tamaño.pack(pady=1)

    etiqueta_peso = ttk.Label(content_frame, text="Peso en kg:", font=("Arial", 14))
    etiqueta_peso.pack()
    entry_peso = ttk.Entry(content_frame)
    entry_peso.pack(pady=1)

    etiqueta_sintomas = ttk.Label(content_frame, text="Síntomas:", font=("Arial", 14))
    etiqueta_sintomas.pack()
    entry_sintomas = tk.Entry(content_frame)
    entry_sintomas.pack(pady=1)

    boton_registrar_mascota = ttk.Button(content_frame, text="Registrar", command=lambda: registrar_mascota(cliente, centro, entry_nombre_mascota.get(), especie_var.get(), entry_edad_mascota.get(), sexo_var.get(), tamaño_var.get(), entry_peso.get(), entry_sintomas.get()))
    boton_registrar_mascota.pack(pady=2)



def seleccion_sede(cliente, sede):
    if not sede:
            messagebox.showerror("Error", "Elija una sede")
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

    etiqueta_info = ttk.Label(content_frame, text="Ingrese sus datos", font=("Arial", 14))
    etiqueta_info.pack(pady=5)

    etiqueta_nombre = ttk.Label(content_frame, text="Nombre:", font=("Arial", 14))
    etiqueta_nombre.pack(pady=5)
    entry_nombre = ttk.Entry(content_frame)
    entry_nombre.pack(pady=5)

    etiqueta_edad = ttk.Label(content_frame, text="Edad:", font=("Arial", 14))
    etiqueta_edad.pack(pady=5)
    entry_edad = ttk.Entry(content_frame)
    entry_edad.pack(pady=5)

    etiqueta_cedula = ttk.Label(content_frame, text="Cédula:", font=("Arial", 14))
    etiqueta_cedula.pack(pady=5)
    entry_cedula = ttk.Entry(content_frame)
    entry_cedula.pack(pady=5)

        
    boton_registrar = ttk.Button(content_frame, text="Registrar", command=lambda: registrar(entry_nombre.get(), entry_edad.get(), entry_cedula.get()))
    boton_registrar.pack(pady=5)


def emergencia():

    limpiar_frame(content_frame)

    bienvenida = ttk.Label(content_frame, text="Bienvenido a Emergencia Veterinaria", font=("Arial", 14))
    bienvenida.pack(pady=5)

    boton = ttk.Button(content_frame, text="Continuar", command=registro_cliente)
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

    field_frame_dieta = FieldFrame(content_frame, "Planificación de Dieta", ["Nombre de la mascota", "Especie", "Edad (años)", "Sexo", "Tamaño", "Peso en kg"], "Valor")
    field_frame_dieta.pack(pady=10)
    field_frame_dieta.agregar_combobox("Especie", ["Perro", "Gato"])
    field_frame_dieta.agregar_combobox("Sexo", ["Macho", "Hembra"])
    field_frame_dieta.agregar_combobox("Tamaño", ["Miniatura", "Pequeño", "Mediano", "Grande"])

    def calcular_dieta():
        try:
            nombre = field_frame_dieta.getValue("Nombre de la mascota")
            especie = field_frame_dieta.getValue("Especie")
            sexo = field_frame_dieta.getValue("Sexo")
            tamaño_texto = field_frame_dieta.getValue("Tamaño")
            tamaño = ["Miniatura", "Pequeño", "Mediano", "Grande"].index(tamaño_texto) + 1
            edad = int(field_frame_dieta.getValue("Edad (años)"))
            peso = float(field_frame_dieta.getValue("Peso en kg"))
            if not nombre or not especie or not edad or not sexo or not tamaño or not peso:
                messagebox.showwarning("Error", "Por favor seleccione valores válidos.")
                return
            # Crear objeto Mascota
            mascota = Mascota(nombre, especie, edad, sexo, EstadoSalud.SANO , tamaño, peso)

            # Crear y calcular dieta
            dieta = Dieta(mascota)
            dieta.calcularPesoIdeal()
            dieta.planDieta()
            dieta_resultado = str(dieta)

            # Limpiar el frame general y mostrar el resultado en pantalla
            limpiar_frame(content_frame)
            ttk.Label(content_frame, text="Resultado de la Dieta", font=("Arial", 18, "bold")).pack(pady=10)
            resultado_text = tk.Text(content_frame, wrap=tk.WORD, font=("Arial", 14))
            resultado_text.pack(pady=10)
            resultado_text.insert(tk.END, dieta_resultado)
            resultado_text.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showwarning("Error", "Ingrese valores numéricos válidos.")

    field_frame_dieta.crearBotones(calcular_dieta, "Calcular Dieta", pady=10, column=0, padx=10)

    def inicio_tienda_dietas(especie):
        limpiar_frame(content_frame)

        # Cargar productos desde el archivo serializado
        productosBarf = cargar_datos_productos2()

        if not productosBarf:
            messagebox.showwarning("Error", "No se encontraron productos disponibles.")
            mostrar_interfaz_inicial(content_frame)
            return

        field_frame_tienda = FieldFrame(content_frame, f"Tienda de Dietas BARF para {especie}s", ["Producto", "Cantidad en gramos", "Nombre", "Cédula"], "Valor")
        field_frame_tienda.pack(pady=10)
        field_frame_tienda.agregar_combobox("Producto", [f"{p.nombre} - ${p.precio} por gramo" for p in productosBarf])

        def confirmar_compra():
            producto_seleccionado = field_frame_tienda.getValue("Producto")
            cantidad = int(field_frame_tienda.getValue("Cantidad en gramos"))
            nombre = field_frame_tienda.getValue("Nombre")
            cedula = field_frame_tienda.getValue("Cédula")

            if not producto_seleccionado or cantidad <= 0 or not nombre or not cedula:
                messagebox.showwarning("Error", "Por favor complete todos los campos correctamente.")
                return

            nombre_producto = producto_seleccionado.split(" - ")[0]
            producto = next((p for p in productosBarf if p.nombre == nombre_producto), None)

            if producto:
                cliente = Cliente(nombre, 18, cedula)
                factura = f"FACTURA ELECTRONICA\n{producto.nombre} x {cantidad}g.\nCliente: {cliente.nombre}\nDocumento: {cliente.cedula}\nMuchas Gracias por comprar en UNmascota! Vuelva pronto"
                # Limpiar el frame general y mostrar el resultado en pantalla
                limpiar_frame(content_frame)
                ttk.Label(content_frame, text=factura, font=("Arial", 14)).pack(pady=10)
            else:
                messagebox.showwarning("Error", "Producto no encontrado.")

        field_frame_tienda.crearBotones(confirmar_compra, "Confirmar Compra", pady=10, column=0, padx=10)
        field_frame_tienda.crearBotones(mostrar_formulario_dietas, "Cancelar", pady=10, column=1, padx=10)

    field_frame_dieta.crearBotones(lambda: inicio_tienda_dietas(field_frame_dieta.getValue("Especie")), "Tienda Dieta BARF", pady=10, column=1, padx=10)

#---------------------------------------------------------------------
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

def centrar_ventana(root, ancho, alto):
    pantalla_ancho = root.winfo_screenwidth()
    pantalla_alto = root.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    root.geometry(f"{ancho}x{alto}+{x}+{y}")
# ===========================
# CONFIGURACIÓN DE INTERFAZ
# ===========================

root = tk.Tk()
root.title("Interfaz de Aplicación Mejorada")
centrar_ventana(root, 800, 450)
root.configure(bg="#D5D5D5")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
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
procesos_menu.add_separator()
procesos_menu.add_command(label="Agendar UNservicio", command=lambda: manejar_seleccion_proceso("Proceso 2"))
procesos_menu.add_separator()
procesos_menu.add_command(label="UNaemergencia o.o", command=lambda: manejar_seleccion_proceso("Proceso 3"))
procesos_menu.add_separator()
procesos_menu.add_command(label="Adquirir UNmemorial", command=lambda: manejar_seleccion_proceso("Proceso 4"))
procesos_menu.add_separator()
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