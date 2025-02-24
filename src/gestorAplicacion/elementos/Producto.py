from typing import Optional

class Producto:
    def __init__(self, nombre: str, precio: float, tipo_uso: str, cantidad_unidades: int, tipo_animal: Optional[str] = None):
        self.nombre = nombre
        self.precio = precio
        self.tipo_uso = tipo_uso
        self.cantidad_unidades = cantidad_unidades
        self.tipo_animal = tipo_animal

    # Métodos Getters y Setters
    def set_nombre(self, nombre: str) -> None:
        """Establece el nombre del producto."""
        self.nombre = nombre

    def get_nombre(self) -> str:
        """Devuelve el nombre del producto."""
        return self.nombre

    def set_precio(self, precio: float) -> None:
        """Establece el precio del producto."""
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = precio

    def get_precio(self) -> float:
        """Devuelve el precio del producto."""
        return self.precio

    def set_tipo_animal(self, tipo_animal: Optional[str]) -> None:
        """Establece el tipo de animal al que está destinado el producto."""
        self.tipo_animal = tipo_animal

    def get_tipo_animal(self) -> Optional[str]:
        """Devuelve el tipo de animal al que está destinado el producto."""
        return self.tipo_animal

    def set_tipo_uso(self, tipo_uso: str) -> None:
        """Establece el tipo de uso del producto."""
        self.tipo_uso = tipo_uso

    def get_tipo_uso(self) -> str:
        """Devuelve el tipo de uso del producto."""
        return self.tipo_uso

    def set_cantidad_unidades(self, cantidad_unidades: int) -> None:
        """Establece la cantidad de unidades disponibles del producto."""
        if cantidad_unidades < 0:
            raise ValueError("La cantidad de unidades no puede ser negativa.")
        self.cantidad_unidades = cantidad_unidades

    def get_cantidad_unidades(self) -> int:
        """Devuelve la cantidad de unidades disponibles del producto."""
        return self.cantidad_unidades

    # Método toString (__str__)
    def __str__(self) -> str:
        return (
            f"\nProducto: {self.get_nombre()}\n"
            f"Precio: ${self.get_precio():.2f}\n"
            f"Destinado a: {self.get_tipo_animal() if self.get_tipo_animal() else 'General'}\n"
            f"Tipo del Producto: {self.get_tipo_uso()}\n"
            f"Cantidad unidades: {self.get_cantidad_unidades()}\n"
        )

    # Método para reducir la cantidad de unidades (útil para ventas)
    def reducir_cantidad(self, cantidad: int) -> None:
        if cantidad > self.cantidad_unidades:
            raise ValueError("No hay suficientes unidades disponibles.")
        self.cantidad_unidades -= cantidad

    # Método para aumentar la cantidad de unidades (útil para restock)
    def aumentar_cantidad(self, cantidad: int) -> None:
        if cantidad < 0:
            raise ValueError("La cantidad a aumentar no puede ser negativa.")
        self.cantidad_unidades += cantidad