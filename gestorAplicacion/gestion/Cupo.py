import datetime
from datetime import datetime as dt

# LÓPEZ GONZÁLEZ, ALEJANDRO
# BETANCUR URIBE, EMMANUEL
# MARTÍNEZ RÍOS, SANTIAGO
# BULA FUENTES, MELANIE
# OSPINA GAVIRIA, TOMAS

# DESCRIPCIÓN FUNCIONALIDAD:
# Representa un bloque de tiempo disponible para citas por cada empleado. Incluye información sobre el día, la hora de inicio y fin, y si está disponible.

class Cupo:
    def __init__(self, dia, hora_inicio, hora_fin, disponible):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.disponible = disponible

    # MÉTODOS GETTERS & ToString
    def get_dia(self):
        return self.dia

    def get_hora_inicio(self):
        return self.hora_inicio

    def get_hora_fin(self):
        return self.hora_fin

    def is_disponible(self):
        return self.disponible

    def set_disponible(self, booleano):
        self.disponible = booleano

    @staticmethod
    def actualizar_cupo(array_dia):
        fecha_actual = datetime.date.today()

        # Se comprueba que la fecha sea anterior a la actual.
        if array_dia[0].get_dia() < fecha_actual:
            # Si el día coincide con el actual, se habilitan los cupos para hoy.
            if fecha_actual.weekday() == array_dia[0].get_dia().weekday():
                array_dia.clear()

                array_dia.append(Cupo(fecha_actual, "8:00", "10:00", True))
                array_dia.append(Cupo(fecha_actual, "10:00", "12:00", True))
                array_dia.append(Cupo(fecha_actual, "14:00", "16:00", True))
                array_dia.append(Cupo(fecha_actual, "16:00", "18:00", True))

            else:
                fecha_actual = datetime.date.today()

                num_dia = array_dia[0].get_dia().weekday()

                continuar = True

                while continuar:
                    # Si el día no coincide, buscamos entre los próximos.
                    fecha_actual = fecha_actual + datetime.timedelta(days=1)  # Pasamos al día siguiente.

                    if fecha_actual.weekday() == num_dia:
                        array_dia.clear()

                        # Llenamos el día por delante
                        array_dia.append(Cupo(fecha_actual, "8:00", "10:00", True))
                        array_dia.append(Cupo(fecha_actual, "10:00", "12:00", True))
                        array_dia.append(Cupo(fecha_actual, "14:00", "16:00", True))
                        array_dia.append(Cupo(fecha_actual, "16:00", "18:00", True))

                        continuar = False

    def __str__(self):
        return f"De {self.hora_inicio} a {self.hora_fin}"

    def fecha_formateada(self):
        formatter = "%d %B %Y"
        return self.dia.strftime(formatter)