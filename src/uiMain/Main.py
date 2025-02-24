import sys
import os
# Añade el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.gestorAplicacion.elementos.Dieta import Dieta
from src.gestorAplicacion.gestion.empleado import Empleado
from src.gestorAplicacion.elementos.Mascota import Mascota
from src.gestorAplicacion.gestion.Tienda import Tienda
from src.gestorAplicacion.elementos.Cliente import Cliente
from src.gestorAplicacion.elementos.centroAdopcion import CentroAdopcion
from src.gestorAplicacion.elementos.Producto import Producto
from src.gestorAplicacion.gestion.Cupo import Cupo
from src.gestorAplicacion.elementos.estado_Salud import EstadoSalud
from tkinter import messagebox
from src.baseDatos.serializador import cargar_datos

if __name__ == "__main__":
    from src.uiMain import InitialWin

##================================================================================================
##PLANIFICAR UNADIETA
##================================================================================================
def planificacionDieta():
    cliente = Cliente.registro()

    # Ingresar datos de la mascota
    print("\nIngresa los datos de su mascota:")
    
    nombre = str(input("Nombre: "))

    # Validar especie
    especie = ""
    while True:
        especie = input("Especie: ").capitalize()
        if especie in ["Gato", "Perro"]:
            break
        else:
            print("Lo sentimos, la planificación de dieta solo está disponible para gatos y perros.")
            return

    edad = int(input("Edad: "))

    # Validar sexo
    sexo = ""
    while True:
        sexo = input("Sexo (M/F): ").upper()
        if sexo in ["M", "F"]:
            break
        else:
            print("Introduce un valor valido (M/F)")
            return

    # Validar tamaño
    print("Tamaño (1-4): \n1. Miniatura \n2. Pequeño \n3. Mediano \n4. Grande")
    while True:
        tamano = int(input("Seleccione el tamaño: "))
        if 1 <= tamano <= 4:
            break
        else:
            print("Entrada no válida, inténtalo de nuevo.")

    peso = int(input("Peso en kg: "))

    # Crear objeto Mascota
    mascota = Mascota(nombre, especie, edad, sexo, "SANO", tamano, peso)

    # Crear y calcular dieta
    dieta = Dieta(mascota)
    dieta.calcularPesoIdeal()
    dieta.planDieta()
    dieta.menu()

    # Imprimir la dieta planificada
    print("\n--------------------\n")
    print(dieta)
    print("\n--------------------")

    # Mini tienda de productos dietéticos
    tipoDietaBarf = f"Dieta Barf para {especie}s"

    tienda = Tienda(empleado.Empleado("Albert", 22, 555, 1323, "West Elm", "Vendedor"))
    productosBarf = [
        Producto(f"Dieta Barf Alta en Proteínas para {especie} (Gramo)", 45.0, "Dieta", f"Alimento para {especie}", 1000),
        Producto(f"Dieta Barf Alta en Grasas para {especie} (Gramo)", 45.0, "Dieta", f"Alimento para {especie}", 1000),
        Producto(f"Dieta Barf Alta en Carbohidratos para {especie} (Gramo)", 45.0, "Dieta", f"Alimento para {especie}", 1000)
    ]

    for producto in productosBarf:
        tienda.agregarProducto(producto)

    # Compra de Dieta Barf
    print("\n¿Desea adquirir Dieta Barf para su mascota? [si/no]: ")
    while True:    
        respuesta = input().lower()
        if respuesta == "si":
            print(f"\nSabores disponibles de {tipoDietaBarf}:")
            print(tienda.filtrar("Dieta"))
            opcionSabor = int(input("Ingrese el número del sabor que desea: "))
            cantidadGramos = int(input("Ingrese la cantidad en gramos que desea comprar: "))
            resultadoCompra = tienda.compra(opcionSabor, cantidadGramos, cliente)
            print(resultadoCompra)
            print("¿Desea seguir comprando? [Si/No]: ")
            return
        elif respuesta == "no":
            print("\nGracias por ingresar a la interfaz de planificación de dieta!\nRedirigiéndote al menú principal...\n")
            break
        else:
            print("ingresa un valor valido (si/no)")
            return

##================================================================================================
##AGENDAR UNSERVICIO
##================================================================================================
def inicializar_agendador():
    # Cargar datos iniciales desde el archivo
    centros_adopcion = cargar_datos()
    if centros_adopcion is None:
        raise Exception("No se pudieron cargar los datos iniciales.")

    return {
        'cliente': None,
        'mascota': None,
        'citas_agendadas': [],
        'centros_adopcion': centros_adopcion
    }

def agendar_servicio(agendador, sede, servicio, cliente_data, mascota_data, dia, hora, empleado_nombre):
    cliente = Cliente(*cliente_data)
    mascota = Mascota(*mascota_data)
    agendador['cliente'] = cliente
    agendador['mascota'] = mascota

    centro = agendador['centros_adopcion'][sede]

    empleados_disponibles = centro.tieneEmpleados()
    if not empleados_disponibles:
        return "No hay empleados disponibles"

    empleado_seleccionado = next((emp for emp in empleados_disponibles if emp.nombre == empleado_nombre), None)
    if not empleado_seleccionado:
        return "Empleado no disponible"

    cupos_disponibles = empleado_seleccionado.cupos_disponibles(dia)
    cupo_seleccionado = next((cupo for cupo in cupos_disponibles if cupo.hora_inicio == hora), None)
    if not cupo_seleccionado:
        return "Cupo no disponible"

    # Asignar el cupo al cliente y mascota
    cupo_seleccionado.disponible = False
    return "Cita agendada exitosamente"

def verificar_disponibilidad(agendador, sede, servicio):
    centro = agendador['centros_adopcion'][sede]
    empleados_disponibles = centro.tieneEmpleados()
    return bool(empleados_disponibles)

def obtener_sedes():
    return ["Sede Medellin", "Sede Bogota", "Sede Cali", "Sede Cartagena"]

def obtener_servicios(sede):
    servicios = {
        "Sede Medellin": ["Entrenamiento", "Veterinaria"],
        "Sede Bogota": ["Peluquería"],
        "Sede Cali": ["Entrenamiento", "Veterinaria"],
        "Sede Cartagena": ["Entrenamiento"]
    }
    return servicios.get(sede, [])

def obtener_empleados_disponibles(agendador, sede):
    centro = agendador['centros_adopcion'][sede]
    return centro.tieneEmpleados()

##================================================================================================
##UNAEMERGENCIA
##================================================================================================
def emergenciaVeterinaria():

    cliente = Cliente.registro()

    print("Ingrese los datos de su mascota:")
    nombreMascota = input("Nombre: ")
    tipo = input("Especie: ")
    edadMascota = int(input("Edad: "))
    sexo = input("Sexo (M/F): ")
    tamano = int(input("Tamaño (1-4): \n1. Miniatura \n2. Pequeño \n3. Mediano \n4. Grande \nIngrese el número correspondiente: "))
    peso = float(input("Peso en kg: "))

    print("¿Cuáles de los siguientes síntomas presenta su mascota? (Sin comas)\nFiebre - Vómito - Picazón - Enrojecimiento - Inflamación")
    sintomas = input()
    listaSintomas = sintomas.split(" ")

    mascota = Mascota(nombreMascota, tipo, edadMascota, sexo, EstadoSalud.ENFERMO, tamano, peso)

    print("\n¿En dónde desea que su mascota sea atendida? (1-4):")
    centro.mostrarSedes()
    sede = int(input("Ingrese el número correspondiente a la sede: "))

    while sede < 1 or sede > len(Sedes):
        sede = int(input("scanner inválida. Por favor, ingrese un número entre 1 y " + len(Sedes) + ":"))

    centro.setSede(list(Sedes)[sede - 1].name)
    nombreSede = list(Sedes)[sede - 1].name.capitalize()
    print("\nLa sede seleccionada es: " + nombreSede)

    if (centro.verificarHospitalizacion(mascota, listaSintomas, centro)):

        print("\nSu mascota puede ser hospitalizada.")
        print("\nElija uno de los siguientes veterinarios disponibles:\n")

        for i, veterinario in enumerate(centro.gestionarVeterinario()):
            print(f"{i + 1}. {veterinario}")

        opcion = int(input("Ingrese el número correspondiente al veterinario que desea: "))

        while opcion < 1 or opcion > len(centro.getVeterinario()):
            opcion = int(input("\nOpción inválida. Por favor, ingrese un número entre 1 y " + len(centro.gestionarVeterinario())+ ":"))

        
        print("\nSu veterinario asignado es\n" + centro.gestionarVeterinario()[opcion-1])
        centro.asignarVeterinario(mascota, centro.gestionarVeterinario()[opcion-1])
        centro.agregarHospitalizado(mascota)

        print("\nSu mascota ha sido hospitalizada en la sede: " + nombreSede)

        print("\nGestionando pago. Seleccione el método de pago (1-3):\n")
        for i, metodo in enumerate(centro.mostrarOpcionesPago()):
            print(f"{i + 1}. {metodo}")
        pago = int(input())

        while pago < 1 or pago > len(centro.mostrarOpcionesPago()):
            pago = int(input("\nOpción inválida. Por favor, ingrese un número entre 1 y " + len(centro.mostrarOpcionesPago())+ ":"))


        pagoValido = False
        while not pagoValido:

            if pago == 1:
                centro.procesarPago(1, cliente, 20000)
                centro.generarFactura(cliente, mascota, 20000)
                pagoValido = True
                break
            elif pago == 2:
                centro.procesarPago(2, cliente, 32000)
                centro.generarFactura(cliente, mascota, 32000)
                pagoValido = True
                break
            elif pago == 3:
                if cliente.getPuntos() < 20000:
                    pago = int(input("\nPuntos insuficientes, seleccione otro método de pago."))
                else:
                    centro.procesarPago(3, cliente, 20000)
                    centro.generarFactura(cliente, mascota, 20000)
                    pagoValido = True
                break
            else:
                pago = int(input("Opción no válida."))
                break

        alta = int(input("\nEs posible dar de alta a su mascota. ¿Desea hacerlo? (1-2) \n1. Sí \n2. No"))

        if alta == 1:
            print("\nSe ha registrato el alta de su mascota " + mascota.getNombre() + ".")
            centro.registrarAlta(mascota)
            print("Saliendo de Emergencia Veterinaria")
        elif alta == 2:
            print("\nSu mascota " + mascota.getNombre() + " sigue hospitalizada.")
            print("Saliendo de Emergencia Veterinaria")

