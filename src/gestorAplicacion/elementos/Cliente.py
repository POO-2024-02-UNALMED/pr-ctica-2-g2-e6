from .Persona import Persona
from .Mascota import Mascota
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
        cliente.agregar_puntos(0)
        return cliente


    def set_mascota(self, mascota):
        self.mascota = mascota

    def get_mascota(self):
        return self.mascota

    def __str__(self):
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, Cedula: {self.cedula}, "
                f"Telefono: {self.telefono}, Direccion: {self.direccion}")