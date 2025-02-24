import os
import sys
import pickle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.gestorAplicacion.elementos.centroAdopcion import CentroAdopcion
from src.gestorAplicacion.gestion.Cupo import Cupo
from src.gestorAplicacion.gestion.empleado import Empleado
from src.gestorAplicacion.elementos.Producto import Producto

def crear_datos_iniciales():
    # Crear centros de adopción con datos iniciales
    centros_adopcion = {
        "Sede Medellin": CentroAdopcion("Medellin"),
        "Sede Bogota": CentroAdopcion("Bogota"),
        "Sede Cali": CentroAdopcion("Cali"),
        "Sede Cartagena": CentroAdopcion("Cartagena")
    }

    # Datos para empleados
    nombres = [
        ["Ana", "Juan", "Carlos", "Luisa", "Pedro", "Marta", "Sofia", "Diego", "Laura", "Jorge"],
        ["Luis", "María", "Fernando", "Carmen", "Roberto", "Elena", "Pablo", "Natalia", "Andrés", "Patricia"],
        ["José", "Andrea", "Daniel", "Paula", "Ricardo", "Claudia", "Miguel", "Sara", "Tomás", "Verónica"],
        ["Alberto", "Valeria", "Santiago", "Isabel", "Javier", "Lorena", "Manuel", "Rosa", "Álvaro", "Gabriela"]
    ]
    edades = [
        [30, 40, 35, 28, 50, 32, 27, 45, 31, 29],
        [33, 42, 38, 26, 52, 34, 29, 48, 35, 31],
        [31, 43, 36, 27, 51, 33, 28, 46, 32, 30],
        [34, 41, 37, 29, 53, 35, 30, 47, 33, 32]
    ]
    cedulas = [
        [123456789, 987654321, 456789123, 789123456, 321654987, 654321789, 147258369, 258369147, 369147258, 741852963],
        [223456789, 887654321, 356789123, 689123456, 221654987, 554321789, 247258369, 158369147, 269147258, 641852963],
        [323456789, 787654321, 256789123, 589123456, 121654987, 454321789, 347258369, 258369147, 169147258, 541852963],
        [423456789, 687654321, 156789123, 489123456, 421654987, 354321789, 447258369, 358369147, 469147258, 441852963]
    ]
    telefonos = [
        [3000000001, 3000000002, 3000000003, 3000000004, 3000000005, 3000000006, 3000000007, 3000000008, 3000000009, 3000000010],
        [3100000001, 3100000002, 3100000003, 3100000004, 3100000005, 3100000006, 3100000007, 3100000008, 3100000009, 3100000010],
        [3200000001, 3200000002, 3200000003, 3200000004, 3200000005, 3200000006, 3200000007, 3200000008, 3200000009, 3200000010],
        [3300000001, 3300000002, 3300000003, 3300000004, 3300000005, 3300000006, 3300000007, 3300000008, 3300000009, 3300000010]
    ]
    direcciones = [
        ["Direccion 1", "Direccion 2", "Direccion 3", "Direccion 4", "Direccion 5", "Direccion 6", "Direccion 7", "Direccion 8", "Direccion 9", "Direccion 10"],
        ["Direccion 11", "Direccion 12", "Direccion 13", "Direccion 14", "Direccion 15", "Direccion 16", "Direccion 17", "Direccion 18", "Direccion 19", "Direccion 20"],
        ["Direccion 21", "Direccion 22", "Direccion 23", "Direccion 24", "Direccion 25", "Direccion 26", "Direccion 27", "Direccion 28", "Direccion 29", "Direccion 30"],
        ["Direccion 31", "Direccion 32", "Direccion 33", "Direccion 34", "Direccion 35", "Direccion 36", "Direccion 37", "Direccion 38", "Direccion 39", "Direccion 40"]
    ]
    profesiones = [
        [Empleado.Especialidad.VETERINARIO, Empleado.Especialidad.PELUQUERO, Empleado.Especialidad.ENTRENADOR, Empleado.Especialidad.VETERINARIO, Empleado.Especialidad.PELUQUERO, Empleado.Especialidad.ENTRENADOR, Empleado.Especialidad.VETERINARIO, Empleado.Especialidad.PELUQUERO, Empleado.Especialidad.ENTRENADOR, Empleado.Especialidad.VETERINARIO],
        [Empleado.Especialidad.ENTRENADOR, Empleado.Especialidad.VETERINARIO, Empleado.Especialidad.PELUQUERO, Empleado.Especialidad.ENTRENADOR, Empleado.Especialidad.VETERINARIO, Empleado.Especialidad.PELUQUERO, Empleado.Especialidad.ENTRENADOR, Empleado.Especialidad.VETERINARIO, Empleado.Especialidad.PELUQUERO, Empleado.Especialidad.ENTRENADOR],
        [Empleado.Especialidad.PELUQUERO, Empleado.Especialidad.ENTRENADOR, Empleado.Especialidad.VETERINARIO, Empleado.Especialidad.PELUQUERO, Empleado.Especialidad.ENTRENADOR, Empleado.Especialidad.VETERINARIO, Empleado.Especialidad.PELUQUERO, Empleado.Especialidad.ENTRENADOR, Empleado.Especialidad.VETERINARIO, Empleado.Especialidad.PELUQUERO],
        [Empleado.Especialidad.VETERINARIO, Empleado.Especialidad.PELUQUERO, Empleado.Especialidad.ENTRENADOR, Empleado.Especialidad.VETERINARIO, Empleado.Especialidad.PELUQUERO, Empleado.Especialidad.ENTRENADOR, Empleado.Especialidad.VETERINARIO, Empleado.Especialidad.PELUQUERO, Empleado.Especialidad.ENTRENADOR, Empleado.Especialidad.VETERINARIO]
    ]

    # Crear y asignar empleados a cada centro de adopción
    for idx, centro in enumerate(centros_adopcion.values()):
        for i in range(10):  # 10 empleados por centro
            empleado = Empleado(
                nombre=nombres[idx][i],
                edad=edades[idx][i],
                cedula=cedulas[idx][i],
                telefono=telefonos[idx][i],
                direccion=direcciones[idx][i],
                profesion=profesiones[idx][i]
            )
            centro.agregarEmpleado(empleado)

    productos = [
        Producto("Comida para Perros", 25.99, "Alimento", 100, "Perro"),
        Producto("Comida para Gatos", 20.99, "Alimento", 80, "Gato"),
        Producto("Juguete para Perros", 15.50, "Juguete", 50, "Perro"),
        Producto("Juguete para Gatos", 12.50, "Juguete", 60, "Gato"),
        Producto("Cama para Conejos", 30.00, "Accesorio", 30, "Conejo"),
        Producto("Jaula para Aves", 45.00, "Accesorio", 20, "Ave"),
        Producto("Shampoo para Perros", 10.00, "Higiene", 70, "Perro"),
        Producto("Shampoo para Gatos", 9.50, "Higiene", 65, "Gato"),
        Producto("Cepillo para Conejos", 8.00, "Higiene", 40, "Conejo"),
        Producto("Comedero para Aves", 12.00, "Accesorio", 25, "Ave")
    ]

    return centros_adopcion, productos


def guardar_datos_centros(centros_adopcion, ruta_centros="src/baseDatos/temp/centros_adopcion.pkl"):
    os.makedirs(os.path.dirname(ruta_centros), exist_ok=True)
    with open(ruta_centros, 'wb') as file:
        pickle.dump(centros_adopcion, file)

def guardar_datos_productos(productos, ruta_productos="src/baseDatos/temp/productos.pkl"):
    os.makedirs(os.path.dirname(ruta_productos), exist_ok=True)
    with open(ruta_productos, 'wb') as file:
        pickle.dump(productos, file)

def cargar_datos_centros(ruta_centros="src/baseDatos/temp/centros_adopcion.pkl"):
    centros_adopcion = None

    if os.path.exists(ruta_centros):
        with open(ruta_centros, 'rb') as file:
            centros_adopcion = pickle.load(file)
    return centros_adopcion

def cargar_datos_productos(ruta_productos="src/baseDatos/temp/productos.pkl"):
    productos = None

    if os.path.exists(ruta_productos):
        with open(ruta_productos, 'rb') as file:
            productos = pickle.load(file)

    return productos

