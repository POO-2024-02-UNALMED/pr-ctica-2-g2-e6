import sys
import os
# Añade el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.gestorAplicacion.elementos.Dieta import Dieta
from src.gestorAplicacion.gestion.Empleado import Empleado
from src.gestorAplicacion.elementos.Mascota import Mascota
from src.gestorAplicacion.gestion.Tienda import Tienda
from src.gestorAplicacion.elementos.Cliente import Cliente
from src.gestorAplicacion.elementos.CentroAdopcion import CentroAdopcion
from src.uiMain import InitialWin

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

    tienda = Tienda(Empleado("Albert", 22, 555, 1323, "West Elm", "Vendedor"))
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

 
##------------------------------------------------------------------------------------------------------------------------------------------##
def agendar_servicio_seleccionado():
    citas_agendadas = []
    print("\033[32m\n\n🐾 ¡Bienvenido a UNServicio! 🐾\033[0m")
    print("\033[37mGracias por elegirnos para cuidar y entrenar a tu peludito.")
    print("Por favor, sigue las instrucciones a continuación para que podamos atenderlo de la mejor manera.\n\033[0m")

    repetir = False
    cliente_conocido = False
    cliente = None

    while True:
        sede_seleccionada = 0
        servicio_seleccionado = 0

        # Selección de sede
        print("\033[31m📍 Selección de Sede 📍\033[0m")
        print("\033[34m1. SEDE MEDELLIN\033[0m")
        print("\033[35m2. SEDE BOGOTA\033[0m")
        print("\033[33m3. SEDE CALI\033[0m")
        print("\033[37m4. SEDE CARTAGENA\n\033[0m")

        # Pedir al usuario que seleccione una sede
        while sede_seleccionada < 1 or sede_seleccionada > 4:
            try:
                sede_seleccionada = int(input("\033[30mIngrese su elección dentro del rango [1-4]: "))
                if sede_seleccionada < 1 or sede_seleccionada > 4:
                    print("\033[37mProporcione una respuesta válida.\n")
            except ValueError:
                print("Proporcione una respuesta válida.\n\033[0m")

        # Mostrar los servicios disponibles según la sede seleccionada
        print("\033[36m\n📋 Servicios Disponibles 📋\033[0m")
        if sede_seleccionada == 1:
            print("\033[37mSEDE MEDELLIN - Servicios Disponibles: \033[32m\n1. Entrenamiento \033[35m\n2. Veterinaria")
        elif sede_seleccionada == 2:
            print("\033[37mSEDE BOGOTA - Servicios Disponibles: \033[33m\n1. Peluquería")
        elif sede_seleccionada == 3:
            print("\033[37mSEDE CALI - Servicios Disponibles: \033[35m\n1. Veterinaria \033[32m\n2. Entrenamiento")
        elif sede_seleccionada == 4:
            print("\033[37mSEDE CARTAGENA - Servicios Disponibles: \033[32m\n1. Entrenamiento")

        print("\033[37m3. Cancelar Selección\n")

        # Pedir al usuario que seleccione un servicio o cambiar de sede
        while servicio_seleccionado < 1 or servicio_seleccionado > 3:
            try:
                servicio_seleccionado = int(input("\033[30mIngrese su elección dentro del rango [1-3]:\033[0m"))
                if servicio_seleccionado < 1 or servicio_seleccionado > 3:
                    print("\033[37mProporcione una respuesta válida.\n")
            except ValueError:
                print("Proporcione una respuesta válida.\n\033[0m")

        # Si el usuario decide cambiar de sede
        if servicio_seleccionado == 3:
            continue

        # Verificar si el servicio seleccionado está disponible para la especie de la mascota del cliente
        servicio_seleccionado_disponible = False
        if sede_seleccionada == 1:
            if servicio_seleccionado == 1:
                print("\nEl servicio de Entrenamiento tiene un costo de $80000 y solo está disponible para perros y gatos.")
                while True:
                    respuesta = input("¿Pertenece su mascota a alguna de estas especies? Responda si / no: ").strip().lower()
                    if respuesta not in ["si", "no"]:
                        print("Proporcione una respuesta válida.\n")
                    else:
                        break
                if respuesta == "si":
                    servicio_seleccionado_disponible = True
                    servicio_seleccionado = 1
            elif servicio_seleccionado == 2:
                print("\nEl servicio de veterinaria tiene un costo de $50000 y solo está disponible para perros, gatos, conejos y aves.")
                while True:
                    respuesta = input("¿Pertenece su mascota a alguna de estas especies? Responda si / no: ").strip().lower()
                    if respuesta not in ["si", "no"]:
                        print("Proporcione una respuesta válida.\n")
                    else:
                        break
                if respuesta == "si":
                    servicio_seleccionado_disponible = True
                    servicio_seleccionado = 2
        elif sede_seleccionada == 2:
            if servicio_seleccionado == 1:
                print("\nEl servicio de Peluquería tiene un costo de $25000 y solo está disponible para perros y gatos.")
                while True:
                    respuesta = input("¿Pertenece su mascota a alguna de estas especies? Responda si / no: ").strip().lower()
                    if respuesta not in ["si", "no"]:
                        print("Proporcione una respuesta válida.\n")
                    else:
                        break
                if respuesta == "si":
                    servicio_seleccionado_disponible = True
                    servicio_seleccionado = 1
        elif sede_seleccionada == 3:
            if servicio_seleccionado == 1:
                print("\nEl servicio de Veterinaria tiene un costo de $50000 y solo está disponible para perros, gatos, conejos y aves.")
                while True:
                    respuesta = input("¿Pertenece su mascota a alguna de estas especies? Responda si / no: ").strip().lower()
                    if respuesta not in ["si", "no"]:
                        print("Proporcione una respuesta válida.\n")
                    else:
                        break
                if respuesta == "si":
                    servicio_seleccionado_disponible = True
                    servicio_seleccionado = 1
            elif servicio_seleccionado == 2:
                print("\nEl servicio de Entrenamiento tiene un costo de $80000 y solo está disponible para perros y gatos.")
                while True:
                    respuesta = input("¿Pertenece su mascota a alguna de estas especies? Responda si / no: ").strip().lower()
                    if respuesta not in ["si", "no"]:
                        print("Proporcione una respuesta válida.\n")
                    else:
                        break
                if respuesta == "si":
                    servicio_seleccionado_disponible = True
                    servicio_seleccionado = 2
        elif sede_seleccionada == 4:
            if servicio_seleccionado == 1:
                print("\nEl servicio de Entrenamiento tiene un costo de $80000 y solo está disponible para perros y gatos.")
                while True:
                    respuesta = input("¿Pertenece su mascota a alguna de estas especies? Responda si / no: ").strip().lower()
                    if respuesta not in ["si", "no"]:
                        print("Proporcione una respuesta válida.\n")
                    else:
                        break
                if respuesta == "si":
                    servicio_seleccionado_disponible = True
                    servicio_seleccionado = 1

        # Si el servicio seleccionado no está disponible para la especie, se termina el proceso
        if not servicio_seleccionado_disponible:
            print("\nNos disculpamos, pero el servicio seleccionado que desea no está disponible para su tipo de mascota. Agradecemos su comprensión.\n")
            repetir = False
            continue

        # Obtener la sede seleccionada y los empleados disponibles
        sede = centro_adopcions[sede_seleccionada - 1]
        empleados_disponibles = sede.tiene_empleados()

        # Si no hay empleados disponibles, se termina el proceso
        if len(empleados_disponibles) == 0:
            print("\nActualmente, debido a la falta de disponibilidad de citas, no es posible continuar con el proceso de agendamiento.")
            repetir = False
        else:
            if servicio_seleccionado == 1:
                print("\nContamos con los siguientes entrenadores de mascotas, seleccione el de su preferencia:")
            elif servicio_seleccionado == 2:
                print("\nContamos con los siguientes veterinarios, seleccione el de su preferencia:")
            elif servicio_seleccionado == 3:
                print("\nContamos con los siguientes peluqueros de mascotas, seleccione el de su preferencia:")

            for i, emple in enumerate(empleados_disponibles, 1):
                print(f"{i} - {emple}")

            # Seleccionar al empleado
            num_empleado = 0
            while num_empleado < 1 or num_empleado > len(empleados_disponibles):
                try:
                    num_empleado = int(input(f"\nIngrese su elección dentro del rango [1-{len(empleados_disponibles)}]: "))
                    if num_empleado < 1 or num_empleado > len(empleados_disponibles):
                        print("Proporcione una respuesta válida.")
                except ValueError:
                    print("Proporcione una respuesta válida.")

            empleado_seleccionado = empleados_disponibles[num_empleado - 1]
            print(f"Empleado seleccionado: {empleado_seleccionado}")

            # Seleccionar el día (lunes, martes, miércoles...) en el que se quiere el servicio
            print("\nSeleccione el día en el que desea el servicio.")
            dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]
            for j, dia in enumerate(dias_semana, 1):
                print(f"{j}. {dia}")

            num_dia = 0
            while num_dia < 1 or num_dia > 6:
                try:
                    num_dia = int(input("Ingrese su elección dentro del rango [1-6]: "))
                    if num_dia < 1 or num_dia > 6:
                        print("Proporcione una respuesta válida.\n")
                except ValueError:
                    print("Proporcione una respuesta válida.\n")

            # Cupos que tiene el empleado para el día seleccionado
            cupos_disponibles = empleado_seleccionado.cupos_disponibles(num_dia)

            # Si el empleado no tiene cupos para ese día, entonces el proceso no podrá continuar
            if len(cupos_disponibles) == 0:
                print("Lamentablemente, el empleado seleccionado no tiene disponibilidad para el día que se eligió.")
                repetir = False
            else:
                # Si el empleado tiene cupos para el día seleccionado, entonces se le mostrarán al cliente
                print("\nPor favor, seleccione la franja horaria que mejor se adapte a su necesidad. Si ninguna opción es adecuada,"
                      f"\npuedes seleccionar la opción {len(cupos_disponibles) + 1} para cancelar.\n")

                print(f"Cupos disponibles para el {dias_semana[num_dia - 1]} {cupos_disponibles[0].fecha_formateada()}: ")
                for o, cupo in enumerate(cupos_disponibles, 1):
                    print(f"{o}. {cupo}")

                print(f"{len(cupos_disponibles) + 1}. Cancelar")

                # Seleccionar el cupo de preferencia, o cancelar
                num_cupo = 0
                while num_cupo < 1 or num_cupo > len(cupos_disponibles) + 1:
                    try:
                        num_cupo = int(input(f"Ingrese su elección en el rango [1 - {len(cupos_disponibles) + 1}]: "))
                        if num_cupo < 1 or num_cupo > len(cupos_disponibles) + 1:
                            print("Proporcione una respuesta válida")
                    except ValueError:
                        print("Proporcione una respuesta válida.")

                # Si el usuario decide cancelar el proceso de agendamiento de cita, entonces el proceso finalizará
                if num_cupo == len(cupos_disponibles) + 1:
                    print("Se ha cancelado el agendamiento de la cita.")
                else:
                    # De lo contrario, si selecciona uno, entonces se procede a recoger los datos del cliente
                    # y la mascota
                    cupo_seleccionado = cupos_disponibles[num_cupo - 1]

                    if not cliente_conocido:
                        cliente = obtener_datos_cliente()  # Datos del cliente
                        cliente = CentroAdopcion.es_cliente(cliente)  # Comprobar si el cliente ya está registrado

                    mascota = obtener_datos_mascota(servicio_seleccionado)  # Datos de la mascota

                    # Crear el objeto de tipo Cita
                    nueva_cita = Cita(cliente, mascota, empleado_seleccionado, cupo_seleccionado, servicio_seleccionado)

                    citas_agendadas.append(nueva_cita)  # Agregar la cita al array de citas que el usuario está agendando

                    # Si hay citas agendadas
                    if len(citas_agendadas) != 0:
                        # Si el cliente tiene más de 15 puntos, se le ofrece un descuento
                        if cliente.get_puntos() > 15:
                            print(f"\nSr./Sra. {cliente.nombre} en estos momentos cuenta con {cliente.get_puntos()} puntos."
                                  "\n¿Desea hacer uso de 15 puntos para obtener un descuento del 10%?")
                            while True:
                                scanner = input("Responda si / no: ").strip().lower()
                                if scanner not in ["si", "no"]:
                                    print("Proporcione una respuesta válida.\n")
                                else:
                                    break

                            # Si acepta el descuento, se aplica a todas las citas agendadas y se descuentan los puntos
                            if scanner == "si":
                                for cita in citas_agendadas:
                                    cita.aplicar_descuento()
                                    cliente.disminuir_puntos(15)

                                print("¡Descuento aplicado exitosamente! Se han descontado 15 puntos de su cuenta.")
                            else:
                                print("No se aplicó el descuento.")

                        # Mostrar los detalles de las citas agendadas
                        print("\033[33m\n🗓️ DETALLES DE LAS CITAS AGENDADAS 🗓️\033[0m")

                        for cita in citas_agendadas:
                            print(cita)
                            print("-------------------------------------\n")

                        print("\n¡Cita agendada exitosamente!")

                        print("\n¿Desea agendar otra cita?")
                        while True:
                            respuesta = input("Responda si / no: ").strip().lower()
                            if respuesta not in ["si", "no"]:
                                print("Proporcione una respuesta válida.\n")
                            else:
                                break

                        if respuesta == "si":
                            repetir = True
                            cliente_conocido = True
                        else:
                            repetir = False
                            cliente_conocido = False

        if not repetir:
            break


# Función para obtener los datos del cliente
def obtener_datos_cliente():
    print("\nAntes de continuar, le informamos que para hacer uso del servicio seleccionado la persona encargada de la mascota debe ser mayor de edad.\n")
    input()
    nombre = input("Ingrese su nombre: ").strip()
    edad = 0
    while edad <= 0:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad <= 0:
                print("Proporcione una respuesta válida.\n")
        except ValueError:
            print("Proporcione una respuesta válida.\n")

    # Si el usuario es menor de edad, se piden los datos de un adulto responsable
    if edad < Cliente.EDAD_MINIMA:
        print("El interesado en hacer uso del servicio seleccionado es menor de edad.\n")
        while edad < 18:
            print("Proporcione los datos de un adulto responsable: ")
            nombre = input("Ingrese su nombre: ").strip()
            try:
                edad = int(input("Ingrese su edad: "))
                if edad <= 0:
                    print("Proporcione una edad válida.\n")
                if edad > 0 and edad < 18:
                    print("La edad ingresada no corresponde a la de un adulto.\n")
            except ValueError:
                print("Proporcione una respuesta válida.\n")

    cedula = 0
    while cedula <= 0:
        try:
            cedula = int(input("Ingrese su número de identificación: "))
            if cedula <= 0:
                print("Proporcione una respuesta válida.\n")
                cedula = 0
        except ValueError:
            print("Proporcione una respuesta válida.\n")

    cliente = Cliente(nombre, edad, cedula)
    return cliente

#funcion para obtener los datos de la mascota
def obtener_datos_mascota(servicio):
    input()  # Consumir salto de línea

    print("\nProporcione la siguiente información sobre su mascota.")
    nombre = input("Ingrese el nombre: ").strip()

    edad = 0
    while edad <= 0:
        try:
            edad = int(input("Ingrese la edad (meses): "))
            if edad <= 0:
                print("Proporcione una respuesta válida.\n")
        except ValueError:
            print("Proporcione una respuesta válida.\n")

    opciones = 2 if servicio in [1, 3] else 4
    print("\nSeleccione la especie de su mascota.")
    if servicio in [1, 3]:
        print("1. Perro \n2. Gato")
    elif servicio == 2:
        print("1. Perro \n2. Gato\n3. Conejo \n4. Hámster")

    eleccion = 0
    while eleccion < 1 or eleccion > opciones:
        try:
            eleccion = int(input(f"Ingrese su elección dentro del rango [1-{opciones}]: "))
            if eleccion < 1 or eleccion > opciones:
                print("Opción fuera de rango.\n")
        except ValueError:
            print("Se ha ingresado un tipo de dato incorrecto.\n")

    especie = ["Perro", "Gato", "Conejo", "Hámster"][eleccion - 1]

    print("\nSeleccione el género de su mascota: ")
    print("1. Macho\n2. Hembra")

    eleccion = 0
    while eleccion < 1 or eleccion > 2:
        try:
            eleccion = int(input("Ingrese su elección dentro del rango [1-2]: "))
            if eleccion < 1 or eleccion > 2:
                print("Proporcione una respuesta válida.\n")
        except ValueError:
            print("Proporcione una respuesta válida.\n")

    sexo = "Macho" if eleccion == 1 else "Hembra"

    mascota = Mascota(nombre, especie, edad, sexo)
    return mascota


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