import tkinter as tk
import sys
import os
# Añade el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.gestorAplicacion.elementos.Dieta import Dieta
from src.gestorAplicacion.gestion.Empleado import Empleado
from src.gestorAplicacion.elementos.Mascota import Mascota, EstadoSalud
from src.gestorAplicacion.gestion.Tienda import Tienda
from src.gestorAplicacion.elementos.Cliente import Cliente
from src.gestorAplicacion.elementos.CentroAdopcion import CentroAdopcion, Sedes
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
        elif proceso_seleccionado.startswith("Proceso 3"):
            emergencia()
        elif proceso_seleccionado.startswith("Proceso 4"):
            mostrar_formulario_registro()
        elif proceso.startswith("Proceso 5"):
            mostrar_formulario_dietas()
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

#Emergencia Veterinaria
#--------------------------------------------------------------------------
def emergencia():

    cemtro = CentroAdopcion("POO")

    for widget in content_frame.winfo_children():
        widget.destroy()

    bienvenida = tk.Label(content_frame, text="Bienvenido a Emergencia Veterinaria", font=("Arial", 14), background="white")
    bienvenida.pack(pady=5)

    etiqueta_info = tk.Label(content_frame, text="Ingrese sus datos", font=("Arial", 14), background="white")
    etiqueta_info.pack(pady=5)

    etiqueta_nombre = tk.Label(content_frame, text="Nombre:", font=("Arial", 14), background="white")
    etiqueta_nombre.pack(pady=5)
    entry_nombre = tk.Entry(content_frame)
    entry_nombre.pack(pady=5)

    etiqueta_edad = tk.Label(content_frame, text="Edad:", font=("Arial", 14), background="white")
    etiqueta_edad.pack(pady=5)
    entry_edad = tk.Entry(content_frame)
    entry_edad.pack(pady=5)

    etiqueta_cedula = tk.Label(content_frame, text="Cédula:", font=("Arial", 14), background="white")
    etiqueta_cedula.pack(pady=5)
    entry_cedula = tk.Entry(content_frame)
    entry_cedula.pack(pady=5)

    def registrar():

        def continuar():
            #print(cliente)
            for widget in content_frame.winfo_children():
                widget.destroy()

            etiqueta_info_2 = tk.Label(content_frame, text="Ingrese los datos de su mascota:", font=("Arial", 14), background="white")
            etiqueta_info_2.pack(pady=5)

            etiqueta_nombre_mascota = tk.Label(content_frame, text="Nombre:", font=("Arial", 14), background="white")
            etiqueta_nombre_mascota.pack()
            entry_nombre_mascota = tk.Entry(content_frame)
            entry_nombre_mascota.pack(pady=5)

            etiqueta_especie = tk.Label(content_frame, text="Especie", font=("Arial", 14), background="white")
            etiqueta_especie.pack(pady=5)
            especie_var = tk.StringVar()
            opciones_especie = ["Perro", "Gato"]
            menu_especie = tk.OptionMenu(content_frame, especie_var, *opciones_especie)
            menu_especie.pack(pady=5)

            etiqueta_edad_mascota = tk.Label(content_frame, text="Edad (Años):", font=("Arial", 14), background="white")
            etiqueta_edad_mascota.pack()
            entry_edad_mascota = tk.Entry(content_frame)
            entry_edad_mascota.pack(pady=5)

            etiqueta_sexo = tk.Label(content_frame, text="Sexo", font=("Arial", 14), background="white")
            etiqueta_sexo.pack(pady=5)
            sexo_var = tk.StringVar()
            opciones_sexo = ["Macho", "Hembra"]
            menu_sexo = tk.OptionMenu(content_frame, sexo_var, *opciones_sexo)
            menu_sexo.pack(pady=5)

            etiqueta_tamaño = tk.Label(content_frame, text="Tamaño", font=("Arial", 14), background="white")
            etiqueta_tamaño.pack(pady=5)
            tamaño_var = tk.StringVar()
            opciones_tamaño = ["Miniatura", "Pequeño", "Mediano", "Grande"]
            menu_tamaño = tk.OptionMenu(content_frame, tamaño_var, *opciones_tamaño)
            menu_tamaño.pack(pady=5)

            etiqueta_peso = tk.Label(content_frame, text="Peso en kg:", font=("Arial", 14), background="white")
            etiqueta_peso.pack()
            entry_peso = tk.Entry(content_frame)
            entry_peso.pack(pady=5)

            etiqueta_sintomas = tk.Label(content_frame, text="Síntomas:", font=("Arial", 14), background="white")
            etiqueta_sintomas.pack()
            entry_sintomas = tk.Entry(content_frame)
            entry_sintomas.pack(pady=5)

            def registrar_mascota():
                
                def continuar_2():
                    #print(mascota)
                    #print(lista_sintomas)
                    for widget in content_frame.winfo_children():
                        widget.destroy()

                    centro = CentroAdopcion("Poo")
                    #centro.agregarVeterinario(Empleado("Juana", 27, 10975685, 1765476, "allá", "VETERINARIO"))
                    
                    etiqueta_sedes = tk.Label(content_frame, text="¿En dónde desea que su masconta sea atendida?", font=("Arial", 14), background="white")
                    etiqueta_sedes.pack(pady=5)
                    sedes_var = tk.StringVar()
                    sedes = centro.mostrarSedes()
                    menu_sedes = tk.OptionMenu(content_frame, sedes_var, *sedes)
                    menu_sedes.pack(pady=5)

                    

                    def continuar_3():
                        #nombre_sede = sedes_var.get()
                        #print(nombre_sede)
                        for widget in content_frame.winfo_children():
                            widget.destroy()

                        centro.setSede(sedes_var.get())
                        #print(centro.getSede())

                        '''if centro.verificarHospitalizacion(mascota, lista_sintomas, centro):
                            etiqueta_hosp = tk.Label(content_frame, "Su mascota puede ser hospitalizada.", font=("Arial", 14), background="white")
                            etiqueta_hosp.pack(pady=5)
                        else:
                            etiqueta_hosp = tk.Label(content_frame, text="No", font=("Arial", 14), background="white")
                            etiqueta_hosp.pack(pady=5)'''

                        

                    boton_continuar_2 = tk.Button(content_frame, text="Continuar", command=continuar_3)
                    boton_continuar_2.pack(pady=5)


                try:
                    lista_sintomas = entry_sintomas.get().split(" ")
                    nombre_mascota = entry_nombre_mascota.get()
                    especie = especie_var.get()
                    sexo = sexo_var.get()
                    if tamaño_var.get() == "Miniatura":
                        tamaño = 1
                    elif tamaño_var.get() == "Pequeño":
                        tamaño = 2
                    elif tamaño_var.get() == "Mediano":
                        tamaño = 3
                    else:
                        tamaño = 4
                    edad_mascota = int(entry_edad_mascota.get())
                    peso = float(entry_peso.get())

                    if not nombre_mascota or not especie or not sexo or not tamaño or not edad_mascota or not peso or not lista_sintomas:
                        messagebox.showwarning("Error", "Por favor ingrese valores válidos.")
                        return

                    mascota = Mascota(nombre_mascota, especie, edad_mascota, sexo, EstadoSalud.ENFERMO, tamaño, peso)

                    boton_continuar = tk.Button(content_frame, text="Continuar", command=continuar_2)
                    boton_continuar.pack(pady=5)
                    print(mascota)
            

                except ValueError:
                    messagebox.showwarning("Error", "Ingrese valores numéricos válidos.")

            boton_registrar_mascota = tk.Button(content_frame, text="Registrar", command=registrar_mascota)
            boton_registrar_mascota.pack(pady=5)



        try:
            nombre_cliente = entry_nombre.get()
            edad_cliente = entry_edad.get()
            cedula_cliente = entry_cedula.get()

            if not nombre_cliente or not edad_cliente or not cedula_cliente:
                messagebox.showwarning("Error", "Por favor ingrese valores válidos.")
                return

            cliente = Cliente(nombre_cliente, edad_cliente, cedula_cliente)

            boton_continuar = tk.Button(content_frame, text="Continuar", command=continuar)
            boton_continuar.pack(pady=5)
            print(cliente)
            

        except ValueError:
            messagebox.showwarning("Error", "Ingrese valores numéricos válidos.")


    #cliente = registrar()

    

        #print(cliente)

    boton_registrar = tk.Button(content_frame, text="Registrar", command=registrar)
    boton_registrar.pack(pady=5)


#----------------------------------------------------------------------------------------------

#Planeacion Dieta
#-----------------------------------------------------------------------------------------------

def mostrar_formulario_dietas():
    for widget in content_frame.winfo_children():
        widget.destroy()
    
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
    
    def calcular_dieta():
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
            mascota = Mascota(nombre, especie, edad, sexo, "SANO", tamano, peso)

            # Crear y calcular dieta
            dieta = Dieta(mascota)
            dieta.calcularPesoIdeal()
            dieta.planDieta()
            dieta.menu()
            messagebox.showinfo(f"Plan de dieta", f"{dieta}")
        except ValueError:
            messagebox.showwarning("Error", "Ingrese valores numéricos válidos.")
    
    tk.Button(content_frame, text="Calcular Dieta", command=calcular_dieta).pack(pady=10)

    # Mini tienda de productos dietéticos
    #tipoDietaBarf = f"Dieta Barf para {especie}s"

    #tienda = Tienda(Empleado("Albert", 22, 555, 1323, "West Elm", "Vendedor"))
    #productosBarf = [
    #    Producto(f"Dieta Barf Alta en Proteínas para {especie} (Gramo)", 45.0, "Dieta", f"Alimento para {especie}", 1000),
     #   Producto(f"Dieta Barf Alta en Grasas para {especie} (Gramo)", 45.0, "Dieta", f"Alimento para {especie}", 1000),
      #  Producto(f"Dieta Barf Alta en Carbohidratos para {especie} (Gramo)", 45.0, "Dieta", f"Alimento para {especie}", 1000)
    #]

#    for producto in productosBarf:
 #       tienda.agregarProducto(producto)

  #  # Compra de Dieta Barf
   # print("\n¿Desea adquirir Dieta Barf para su mascota? [si/no]: ")
    #while True:    
     #   respuesta = input().lower()
      #  if respuesta == "si":
      #      print(f"\nSabores disponibles de {tipoDietaBarf}:")
       #     print(tienda.filtrar("Dieta"))
        #    opcionSabor = int(input("Ingrese el número del sabor que desea: "))
         #  resultadoCompra = tienda.compra(opcionSabor, cantidadGramos, cliente)
          #  print(resultadoCompra)
        #    print("¿Desea seguir comprando? [Si/No]: ")
        #    return
       # elif respuesta == "no":
        #    print("\nGracias por ingresar a la interfaz de planificación de dieta!\nRedirigiéndote al menú principal...\n")
         #   break
        #else:
        #    print("ingresa un valor valido (si/no)")
         #   return

#-----------------------------------------------------------------------------------------------

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
    "Proceso 3: Emergencia Veterinaria",
    "Proceso 4: Descripción del proceso 4",
    "Proceso 5: Planificacion de Dietas"
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
