from gestorAplicacion.elementos import Dieta
from gestorAplicacion.gestion import Empleado
from gestorAplicacion.elementos import Mascota, EstadoSalud
from gestorAplicacion.gestion import Tienda

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
    mascota = Mascota(nombre, especie, edad, sexo, EstadoSalud.SANO, tamano, peso)

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