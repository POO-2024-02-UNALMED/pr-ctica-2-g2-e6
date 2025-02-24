from enum import Enum

class EstadoSalud(Enum):
    SANO = "SANO"
    ENFERMO = "ENFERMO"
    ENTRATAMIENTO = "EN TRATAMIENTO"

#Inicializador de la clase

class Mascota:
    def __init__(self, nombre, tipo, edad, sexo, estadoSalud=None, tamano=3, peso=5.0):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.sexo = sexo
        self.estadoSalud = estadoSalud
        self.tamano = tamano  # 1 = Miniatura, 2 = Pequeño, 3 = Mediano, 4 = Grande
        self.peso = peso
        self.veterinario = None

#Metodos get y set
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getTipo(self):
        return self.tipo
    
    def setTipo(self, tipo):
        self.tipo = tipo
    
    def getEdad(self):
        return self.edad
    
    def setEdad(self, edad):
        self.edad = edad
    
    def getSexo(self):
        return self.sexo
    
    def setSexo(self, sexo):
        self.sexo = sexo
    
    def getEstadoSalud(self):
        return self.estadoSalud
    
    def setEstadoSalud(self, estadoSalud):
        self.estadoSalud = estadoSalud
    
    def getVeterinario(self):
        return self.veterinario
    
    def setVeterinario(self, veterinario):
        self.veterinario = veterinario
    
    def getTamano(self):
        return self.tamano
    
    def setTamano(self, tamano):
        self.tamano = tamano
    
    def getTamanoStr(self):
        tamanoStr = ""
        if self.tamano == 1:
            tamanoStr = "Miniatura"
        elif self.tamano == 2:
            tamanoStr = "Pequeño"
        elif self.tamano == 4:
            tamanoStr = "Grande"
        else:
            tamanoStr = "Mediano"
        return tamanoStr
    
    def getPeso(self):
        return self.peso
    
    def setPeso(self, peso):
        self.peso = peso

#Otros metodos
    
    def __str__(self):
        info = f"Nombre: {self.getNombre()}, Especie: {self.getTipo()}, Edad: {self.getEdad()}, Sexo: {self.getSexo()}, Tamaño: {self.getTamanoStr()}, Peso: {self.getPeso()}kg"
        if self.getEstadoSalud():
            info += f", Estado de salud: {self.getEstadoSalud().value}"
        return info
    
    def esCompatible(self, otraMascota):
        if self.getTipo() == otraMascota.getTipo() and self.getEstadoSalud() == otraMascota.getEstadoSalud():
            return True
        else:
            return False 
    
    def indiceEmergencia(self, gravedad, compatibilidad):
        vulnerabilidad = 10 / (1 + (abs(self.getEdad() - 4)))
        ie = (gravedad * 0.7) + (vulnerabilidad * 0.3) + (compatibilidad * 0.1)
        return ie