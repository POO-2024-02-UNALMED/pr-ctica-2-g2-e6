import tkinter as tk
from tkinter import messagebox, simpledialog

# Función para mostrar información de la aplicación
def mostrar_info_aplicacion():
    messagebox.showinfo("Aplicación", "Esta aplicación realiza varias operaciones y consultas.")

# Función para mostrar información de los autores
def mostrar_info_autores():
    messagebox.showinfo("Acerca de", "Autores: Mel Bulaf")

# Función para salir de la aplicación
def salir_aplicacion():
    root.quit()

# Función para manejar la selección de procesos
def manejar_seleccion_proceso(proceso):
    mostrar_interfaz_principal(proceso)

# Función para mostrar la interfaz inicial
def mostrar_interfaz_inicial():
    for widget in content_frame.winfo_children():
        widget.destroy()
    label = tk.Label(content_frame, text="Bienvenido a la Aplicación", font=("Arial", 24, "bold"), fg="blue")
    label.pack(pady=20)
    texto_instrucciones = (
        "Esta aplicación permite realizar varias operaciones y consultas.\n"
        "Utilice el menú 'Archivo' para ver la información de la aplicación o salir.\n"
        "Utilice el menú 'Procesos y Consultas' para listar todas las funcionalidades disponibles.\n"
        "Utilice el menú 'Ayuda' para información sobre los autores."
    )
    instrucciones = tk.Label(content_frame, text=texto_instrucciones, font=("Arial", 14), justify=tk.LEFT, wraplength=600, fg="green")
    instrucciones.pack(pady=20, expand=True, fill="both")

# Función para mostrar la interfaz principal
def mostrar_interfaz_principal(proceso_seleccionado=None):
    for widget in content_frame.winfo_children():
        widget.destroy()
    etiqueta_principal = tk.Label(content_frame, text="Procesos y Consultas", font=("Arial", 24, "bold"), fg="blue")
    etiqueta_principal.pack(pady=20)
    
    if proceso_seleccionado:
        etiqueta_proceso = tk.Label(content_frame, text=f"Has seleccionado: {proceso_seleccionado}", font=("Arial", 18), fg="black")
        etiqueta_proceso.pack(pady=10)
        
        if proceso_seleccionado.startswith("Proceso 2"):
            mostrar_formulario_sedes()
        elif proceso_seleccionado.startswith("Proceso 3") or proceso_seleccionado.startswith("Proceso 4") or proceso_seleccionado.startswith("Proceso 5"):
            mostrar_formulario_registro()
    else:
        etiqueta_proceso = tk.Label(content_frame, text="Seleccione un proceso del menú", font=("Arial", 18), fg="black")
        etiqueta_proceso.pack(pady=10)

# Función para mostrar el formulario de selección de sede
def mostrar_formulario_sedes():
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    def seleccionar_sede():
        sede = sede_var.get()
        if sede in ["Sede Medellin", "Sede Bogota", "Sede Cali", "Sede Cartagena"]:
            mostrar_formulario_servicios(sede)
        else:
            messagebox.showwarning("Selección Incorrecta", "Debe seleccionar una sede válida.")
    
    sede_var = tk.StringVar()
    etiqueta_sede = tk.Label(content_frame, text="Seleccione una sede:", font=("Arial", 18), fg="black")
    etiqueta_sede.pack(pady=10)
    
    opciones_sedes = ["Sede Medellin", "Sede Bogota", "Sede Cali", "Sede Cartagena"]
    menu_sedes = tk.OptionMenu(content_frame, sede_var, *opciones_sedes)
    menu_sedes.pack(pady=10)
    
    boton_seleccionar_sede = tk.Button(content_frame, text="Seleccionar Sede", command=seleccionar_sede)
    boton_seleccionar_sede.pack(pady=10)



# Función para mostrar el formulario de selección de servicios
def mostrar_formulario_servicios(sede):
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    def seleccionar_servicio():
        servicio = servicio_var.get()
        if servicio in ["Servicio 1", "Servicio 2"]:
            mostrar_formulario_registro()
        else:
            messagebox.showwarning("Selección Incorrecta", "Debe seleccionar un servicio válido.")
    
    servicio_var = tk.StringVar()
    etiqueta_servicio = tk.Label(content_frame, text=f"Servicios disponibles en {sede}:", font=("Arial", 18), fg="black")
    etiqueta_servicio.pack(pady=10)
    
    if sede == "Sede Medellin":
        opciones_servicios = ["Servicio 1: Entrenamiento", "Servicio 2: Veterinaria"]
    elif sede == "Sede Bogota":
        opciones_servicios = ["Servicio 1: Peluquería"]
    elif sede == "Sede Cali":
        opciones_servicios = ["Servicio 1: Veterinaria", "Servicio 2: Entrenamiento"]
    elif sede == "Sede Cartagena":
        opciones_servicios = ["Servicio 1: Entrenamiento"]
    
    menu_servicios = tk.OptionMenu(content_frame, servicio_var, *opciones_servicios)
    menu_servicios.pack(pady=10)
    
    boton_seleccionar_servicio = tk.Button(content_frame, text="Seleccionar Servicio", command=seleccionar_servicio)
    boton_seleccionar_servicio.pack(pady=10)

# Función para mostrar el formulario de registro
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
            mostrar_interfaz_principal("Proceso Completado")
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

# Ventana principal
root = tk.Tk()
root.title("Interfaz de Aplicación")
root.geometry("800x600")
root.configure(bg="lightblue")

# Marco principal (zona 0)
main_frame = tk.Frame(root, bg="lightblue")
main_frame.pack(fill=tk.BOTH, expand=True)

# Barra de menú (zona 1)
menu_bar = tk.Menu(main_frame)

# Menú Archivo
archivo_menu = tk.Menu(menu_bar, tearoff=0)
archivo_menu.add_command(label="Aplicación", command=mostrar_info_aplicacion)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=salir_aplicacion)
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

# Menú Procesos y Consultas
procesos_menu = tk.Menu(menu_bar, tearoff=0)

# Agregar procesos al menú Procesos y Consultas
procesos = [
    "Proceso 1: Descripción del proceso 1",
    "Proceso 2: Descripción del proceso 2",
    "Proceso 3: Descripción del proceso 3",
    "Proceso 4: Descripción del proceso 4",
    "Proceso 5: Descripción del proceso 5"
]

for proceso in procesos:
    procesos_menu.add_command(label=proceso, command=lambda p=proceso: manejar_seleccion_proceso(p))
    procesos_menu.add_separator()

menu_bar.add_cascade(label="Procesos y Consultas", menu=procesos_menu)

# Menú Ayuda
ayuda_menu = tk.Menu(menu_bar, tearoff=0)
ayuda_menu.add_command(label="Acerca de", command=mostrar_info_autores)
menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)

# Configuración de la barra de menú
root.config(menu=menu_bar)

# Marco de contenido (zona 2)
content_frame = tk.Frame(main_frame, bg="white")
content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Mostrar interfaz inicial
mostrar_interfaz_inicial()

# Ejecutar el bucle principal
root.mainloop()
