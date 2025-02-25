import sys
import os
# Añade el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.gestorAplicacion.elementos.Dieta import Dieta
from src.gestorAplicacion.gestion.empleado import Empleado
from src.gestorAplicacion.elementos.Mascota import Mascota
from src.gestorAplicacion.gestion.Tienda import Tienda
from src.gestorAplicacion.elementos.Cliente import Cliente
from src.gestorAplicacion.elementos.centroAdopcion import CentroAdopcion
from src.gestorAplicacion.elementos.Producto import Producto
from src.gestorAplicacion.gestion.Cupo import Cupo
from src.gestorAplicacion.elementos.estado_Salud import EstadoSalud
from src.gestorAplicacion.gestion.Memorial import Memorial
from src.gestorAplicacion.elementos.Fallecido import Fallecido
from tkinter import messagebox
from src.baseDatos.serializador import cargar_datos_centros, cargar_datos_productos, cargar_datos_productos2

if __name__ == "__main__":
    from src.uiMain import InitialWin

##================================================================================================
##AGENDAR UNSERVICIO
##================================================================================================
def inicializar_agendador():
    # Cargar datos iniciales desde el archivo
    centros_adopcion = cargar_datos_centros()
    if centros_adopcion is None:
        raise Exception("No se pudieron cargar los datos iniciales.")

    return {
        'cliente': None,
        'mascota': None,
        'citas_agendadas': [],
        'centros_adopcion': centros_adopcion
    }

def agendar_servicio(agendador, sede, servicio, cliente_data, mascota_data, dia, hora, empleado_nombre):
    cliente = Cliente(*cliente_data)
    mascota = Mascota(*mascota_data)
    agendador['cliente'] = cliente
    agendador['mascota'] = mascota

    centro = agendador['centros_adopcion'][sede]

    empleados_disponibles = centro.tieneEmpleados()
    if not empleados_disponibles:
        return "No hay empleados disponibles"

    empleado_seleccionado = next((emp for emp in empleados_disponibles if emp.nombre == empleado_nombre), None)
    if not empleado_seleccionado:
        return "Empleado no disponible"

    cupos_disponibles = empleado_seleccionado.cupos_disponibles(dia)
    cupo_seleccionado = next((cupo for cupo in cupos_disponibles if cupo.hora_inicio == hora), None)
    if not cupo_seleccionado:
        return "Cupo no disponible"

    # Asignar el cupo al cliente y mascota
    cupo_seleccionado.disponible = False
    return "Cita agendada exitosamente" 

def verificar_disponibilidad(agendador, sede, servicio):
    centro = agendador['centros_adopcion'][sede]
    empleados_disponibles = centro.tieneEmpleados()
    return bool(empleados_disponibles)

def obtener_sedes():
    return ["Sede Medellin", "Sede Bogota", "Sede Cali", "Sede Cartagena"]

def obtener_servicios(sede):
    servicios = {
        "Sede Medellin": ["Entrenamiento", "Veterinaria"],
        "Sede Bogota": ["Peluquería"],
        "Sede Cali": ["Entrenamiento", "Veterinaria"],
        "Sede Cartagena": ["Entrenamiento"]
    }
    return servicios.get(sede, [])

def obtener_empleados_disponibles(agendador, sede):
    centro = agendador['centros_adopcion'][sede]
    return centro.tieneEmpleados()
