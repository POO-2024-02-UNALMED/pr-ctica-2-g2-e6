from .Producto import Producto
from .CentroAdopcion import CentroAdopcion

# BULA FUENTES, MELANIE
# OSPINA GAVIRIA, TOMAS

# Descripción de la Clase:
# Representa los artículos en venta en la tienda, incluyendo nombre, precio, tipo de animal, tipo de uso y cantidad disponible.

class Producto:
    def __init__(self, nombre: str, precio: float, tipo_uso: str, cantidad_unidades: int, tipo_animal: str = None):

        self.nombre = nombre
        self.precio = precio
        self.tipo_uso = tipo_uso
        self.cantidad_unidades = cantidad_unidades
        self.tipo_animal = tipo_animal

    # Métodos Getters y Setters
    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_nombre(self) -> str:
        return self.nombre

    def set_precio(self, precio: float):
        self.precio = precio

    def get_precio(self) -> float:
        return self.precio

    def set_tipo_animal(self, tipo: str):
        self.tipo_animal = tipo

    def get_tipo_animal(self, tipo_animal: str):
        return self.tipo_animal

    def set_tipo_uso(self, tipo_uso: str):
        self.tipo_uso = tipo_uso

    def get_tipo_uso(self) -> str:
        return self.tipo_uso

    def set_cantidad_unidades(self, cantidad: int):
        self.cantidad_unidades = cantidad

    def get_cantidad_unidades(self) -> int:
        return self.cantidad_unidades

    # Método toString (__str__)
    def __str__(self) -> str:
        return (
            f"\nProducto: {self.get_nombre()}\n"
            f"Precio: {self.get_precio()}\n"
            f"Destinado a: {self.get_tipo_animal() if self.get_tipo_animal() else 'General'}\n"
            f"Tipo del Producto: {self.get_tipo_uso()}\n"
            f"Cantidad unidades: {self.get_cantidad_unidades()}\n"
        )