from enum import Enum
from .Mascota import Mascota
from .Mascota import EstadoSalud
from ..gestion.empleado import Empleado
class Sedes(Enum):
    MEDELLIN = 1
    BOGOTA = 2
    CALI = 3
    CARTAGENA = 4

class CentroAdopcion:

    clientes = []

    def __init__(self, nombre):
        self._nombre = nombre
        self._animalesHospitalizados = []
        self._veterinarios = []
        self._sede = ""

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getAnimalesHospitalizados(self):
        return self._animalesHospitalizados
    
    def setAnimalesHospitalizados(self, animalesHospitalizados):
        self._animalesHospitalizados = animalesHospitalizados

    def getVeterinarios(self):
        return self._veterinarios
    
    def setVeterinarios(self, veterinarios):
        self._veterinarios = veterinarios

    def getSede(self):
        return self._sede
    
    def setSede(self, sede):
        self._sede = sede

    def getClientes(cls):
        return cls.clientes
    
    def setClientes(cls, clientes):
        cls.clientes = clientes

    

    def agregarVeterinario(self, veterinario):
        self._veterinarios.append(veterinario)

    def registrarCliente(cls, cliente):
        cls.clientes.append(cliente)

    def mostrarSedes(self):
        sedes_list = []
        for i, sede in enumerate(Sedes):
            nombre_sede = sede.name.capitalize()
            sedes_list.append(f"{i+1}. {nombre_sede}")
        return sedes_list
    
    def verificarHospitalizacion(self, mascota, listaSintomas, centro):
        gravedad = 0
        compatibilidad = 0

        for sintoma in listaSintomas:
            if sintoma.lower() == "fiebre":
                gravedad += 2
                compatibilidad += 3
            elif sintoma.lower() == "vomito":
                gravedad += 3
                compatibilidad += 2
            elif sintoma.lower() == "picazon":
                gravedad += 2
                compatibilidad += 1
            elif sintoma.lower() == "enrojecimiento":
                gravedad += 1
                compatibilidad += 2
            elif sintoma.lower() == "inflamacion":
                gravedad += 2
                compatibilidad += 2

            if mascota.indiceEmergencia(gravedad, compatibilidad) < 7.0:
                return False
            
            if centro.gestionarVeterinario() == None:
                return False
            
            if self.hay_capacidad() == False:
                return False
            
            for hospitalizado in self._animalesHospitalizados:
                if mascota.esCompatible(hospitalizado) == False:
                    return False
                
            return True
        

    def gestionarVeterinario(self):
        disponibles = []
        for veterinario in self._veterinarios:
            if veterinario.tieneCupos():
                disponibles.append(veterinario)

        return disponibles if disponibles else None
    
    def agregarHospitalizado(self, mascota):
        self._animalesHospitalizados.append(mascota)

    def mostrarOpcionesPago(self):
        opciones = ["Tarjeta de crédito", "Efectivo", "Puntos acumulados"]
        return opciones
    
    def procesarPago(self, metodo, cliente, monto):

        if metodo == 1:
            print("\nPago procesado con tarjeta por un monto de: $" + monto)
            return True
        elif metodo == 2:
            print("\nPago procesado en efectivo por un monto de: $" + monto)
            return True
        elif metodo == 3:
            if cliente != None and monto <= cliente.getPuntos():
                cliente.disminuirPuntos(monto)
                print("\nPago procesado con puntos acumulados.")
                return True
            else:
                print("\nNo tiene suficientes puntos.")
                return False
            
    def generarFactura(cliente, mascota, monto):
        return (
            "\n--------- Factura --------- "
            f"\n*|* Cliente     *|* {cliente if cliente else 'No registrado'}"
            f"\n*|* Animal      *|* {mascota}"
            f"\n*|* Monto total *|* {monto}"
            "\n-----------------------------\n"
        )
    
    def asignarVeterinario(self, mascota, veterinario):
        mascota.setVeterinario(veterinario)
        veterinario.setMascota(mascota)

    def registrarAlta(self, mascota):
        mascota.setEstadoSalud(EstadoSalud.SANO)
        self._animalesHospitalizados.remove(mascota)
        mascota.getVeterinario().setMascota(None)
        mascota.setVeterinario(None)

    def hay_capacidad(self):
        return len(self._animalesHospitalizados) < 10
    
    @staticmethod
    def esCliente(cliente):

        clienteNuevo = None

        for existe in CentroAdopcion.clientes:
            if existe != None:
                if existe.getCedula() == cliente.getCedula():
                    clienteNuevo = existe
                    break

        if clienteNuevo == None:

            clienteNuevo = cliente
            CentroAdopcion.registrarCliente(clienteNuevo)

        else:
            clienteNuevo.actualizarDatos(cliente.getEdad(), cliente.getTelefono(), cliente.getDireccion())

        return clienteNuevo
    
    def tieneEmpleados(self):
        return [empleado for empleado in self._veterinarios if empleado.tiene_cupos()]
