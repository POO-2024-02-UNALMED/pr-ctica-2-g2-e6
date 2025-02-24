from gestorAplicacion.elementos import Mascota
from gestorAplicacion.elementos import Cliente

# BULA FUENTES, MELANIE
# OSPINA GAVIRIA, TOMAS

# DESCRIPCIÓN DE LA CLASE:
# Representa a los animales que han fallecido, Incluyendo datos sobre el dueño, fecha de fallecimiento y mensajes de recuerdo.

class Fallecido:
    # ---> Atributos <---
    def __init__(self, mascota=None, fecha="", mensaje="", dueño=None, tiempo="", tipo=""):
        self.mascota = mascota
        self.fecha = fecha
        self.mensaje = mensaje
        self.dueño = dueño
        self.tiempo = tiempo
        self.tipo = tipo
        self.flores = []

    # ---> Métodos Getters And Setters <---
    def set_mascota(self, mascota):
        self.mascota = mascota

    def get_mascota(self):
        return self.mascota

    def set_fecha(self, fecha):
        self.fecha = fecha

    def get_fecha(self):
        return self.fecha

    def set_mensaje(self, mensaje):
        self.mensaje = mensaje

    def get_mensaje(self):
        return self.mensaje

    def set_dueño(self, dueño):
        self.dueño = dueño

    def get_dueño(self):
        return self.dueño

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo

    def set_tiempo(self, tiempo):
        self.tiempo = tiempo

    def get_tiempo(self):
        return self.tiempo

    def set_flores(self, flores):
        self.flores = flores

    def get_flores(self):
        return self.flores

    # ---> Métodos <---
    def poner_flor(self, flor):
        if self.flores == ["Sin Flores."]:
            self.flores.clear()
            self.flores.append(flor)
            return f"Este memorial ahora cuenta con una: {flor}."
        elif len(self.flores) <= 5:
            self.flores.append(flor)
            return f"Este memorial ahora cuenta con una: {flor}."
        else:
            return "Solo puede tener 5 tipos de flores."

    def mostrar_flores(self):
        if self.flores == ["Sin Flores."]:
            return self.flores[0]
        elif len(self.flores) == 1:
            return f"Hay una flor: {self.flores[0]}"
        else:
            acomulador = "Flores que hay: "
            acomulador += " ".join(self.flores)
            return acomulador

    # ---> Método ToString <---
    def __str__(self):
        return f"{self.mascota.getNombre()}\n{self.fecha}\n{self.mensaje}\n{self.mostrar_flores()}\n"