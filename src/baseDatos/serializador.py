import os
import sys
import pickle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.gestorAplicacion.elementos.centroAdopcion import CentroAdopcion
from src.gestorAplicacion.gestion.Cupo import Cupo
from src.gestorAplicacion.gestion.empleado import Empleado
from src.gestorAplicacion.elementos.Producto import Producto

def crear_datos_iniciales():
   
    productos2  = [
        Producto(f"Dieta Barf Alta en Proteínas para perros (Gramo)", 45.0, "Dieta", f"Alimento para perro", 1000),
        Producto(f"Dieta Barf Alta en Grasas para perros (Gramo)", 45.0, "Dieta", f"Alimento para perro", 1000),
        Producto(f"Dieta Barf Alta en Carbohidratos para perros (Gramo)", 45.0, "Dieta", f"Alimento para perro", 1000),
        Producto(f"Dieta Barf Alta en Proteínas para gatos (Gramo)", 45.0, "Dieta", f"Alimento para perro", 1000),
        Producto(f"Dieta Barf Alta en Grasas para gatos (Gramo)", 45.0, "Dieta", f"Alimento para perro", 1000),
        Producto(f"Dieta Barf Alta en Carbohidratos para gatos (Gramo)", 45.0, "Dieta", f"Alimento para perro", 1000)
    ]

    return productos2


def guardar_datos_centros(centros_adopcion, ruta_centros="src/baseDatos/temp/centros_adopcion.pkl"):
    os.makedirs(os.path.dirname(ruta_centros), exist_ok=True)
    with open(ruta_centros, 'wb') as file:
        pickle.dump(centros_adopcion, file)

def guardar_datos_productos(productos, ruta_productos="src/baseDatos/temp/productos.pkl"):
    os.makedirs(os.path.dirname(ruta_productos), exist_ok=True)
    with open(ruta_productos, 'wb') as file:
        pickle.dump(productos, file)

def guardar_datos_productos2(productos2, ruta_productos2="src/baseDatos/temp/productos2.pkl"):
    os.makedirs(os.path.dirname(ruta_productos2), exist_ok=True)
    with open(ruta_productos2, 'wb') as file:
        pickle.dump(productos2, file)

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

def cargar_datos_productos2(ruta_productos2="src/baseDatos/temp/productos2.pkl"):
    productos2 = None

    if os.path.exists(ruta_productos2):
        with open(ruta_productos2, 'rb') as file:
            productos2 = pickle.load(file) 
    return productos2
