from gestorAplicacion.elementos import Persona
from gestorAplicacion.elementos import Mascota
from uiMain import Main
import pickle

# LÓPEZ GONZÁLEZ, ALEJANDRO
# BETANCUR URIBE, EMMANUEL
# MARTÍNEZ RÍOS, SANTIAGO
# BULA FUENTES, MELANIE
# OSPINA GAVIRIA, TOMAS

# DESCRIPCIÓN DE LA CLASE:
# Representa a los usuarios que buscan adoptar animales y que pueden utilizar otros servicios del centro, como la tienda y citas.


class Cliente(Persona):
    EDAD_MINIMA = 18

    def __init__(self, nombre, edad, cedula, telefono=None, direccion=None):
        super().__init__(nombre, edad, cedula, telefono, direccion)
        self.puntos = 0
        self.mascota = None

    def actualizar_datos(self, edad, telefono, direccion):
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion

    def agregar_puntos(self, puntos):
        self.puntos += puntos

    def disminuir_puntos(self, puntos):
        self.puntos -= puntos

    def get_puntos(self):
        return self.puntos

    @staticmethod
    def registro():
        datos = Main.capturar_datos_cliente()
        cliente = Cliente(datos[0], datos[1], datos[2])
        cliente.agregar_puntos(0)
        return cliente

    def set_mascota(self, mascota):
        self.mascota = mascota

    def get_mascota(self):
        return self.mascota

    def __str__(self):
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, Cedula: {self.cedula}, "
                f"Telefono: {self.telefono}, Direccion: {self.direccion}")