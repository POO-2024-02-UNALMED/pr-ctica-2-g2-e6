from datetime import date, timedelta
from typing import List
from .Cupo import Cupo

class Empleado:
    class Especialidad:
        VETERINARIO = "VETERINARIO"
        PELUQUERO = "PELUQUERO"
        ENTRENADOR = "ENTRENADOR"
        VENDEDOR = "VENDEDOR"
    
    def __init__(self, nombre: str, edad: int, cedula: int, telefono: int, direccion: str, profesion: str):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.telefono = telefono
        self.direccion = direccion
        self.profesion = profesion
        self.mascota = None
        self.agenda_dias: List[List[Cupo]] = []
        
        if profesion != Empleado.Especialidad.VENDEDOR:  # El vendedor no tiene citas.
            self.llenar_agenda()
    
    def llenar_agenda(self):
        ciclos = [6, 5, 4, 3, 2, 1]
        fecha_actual = date.today()
        dia_semana = fecha_actual.weekday()
        
        if dia_semana == 6:  # Si es domingo, se llenan de lunes a sábado
            fecha_actual += timedelta(days=1)
            for _ in range(6):
                self.agenda_dias.append(self.crear_cupos_dia(fecha_actual))
                fecha_actual += timedelta(days=1)
        else:
            for _ in range(ciclos[dia_semana]):
                self.agenda_dias.append(self.crear_cupos_dia(fecha_actual))
                fecha_actual += timedelta(days=1)
            
            if dia_semana != 0 and dia_semana != 6:  # Se excluye el domingo
                fecha_actual += timedelta(days=1)
                for _ in range(dia_semana):
                    self.agenda_dias.append(self.crear_cupos_dia(fecha_actual))
                    fecha_actual += timedelta(days=1)
    
    @staticmethod
    def crear_cupos_dia(fecha):
        return [
            Cupo(fecha, "8:00", "10:00", True),
            Cupo(fecha, "10:00", "12:00", True),
            Cupo(fecha, "14:00", "16:00", True),
            Cupo(fecha, "16:00", "18:00", True)
        ]
    
    def actualizar_datos(self):
        for cupos_dia in self.agenda_dias:
            Cupo.actualizar_cupo(cupos_dia)
    
    def tiene_cupos(self) -> bool:
        self.actualizar_datos()
        return any(cupo.is_disponible() for cupos_dia in self.agenda_dias for cupo in cupos_dia)
    
    def cupos_disponibles(self, dia: int) -> List[Cupo]:
        disponibles = []
        for cupos_dia in self.agenda_dias:
            if cupos_dia[0].get_dia().weekday() == dia:
                disponibles.extend(cupo for cupo in cupos_dia if cupo.is_disponible())
                break
        return disponibles
    
    def set_mascota(self, mascota):
        self.mascota = mascota
    
    def get_mascota(self):
        return self.mascota
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad} años."
