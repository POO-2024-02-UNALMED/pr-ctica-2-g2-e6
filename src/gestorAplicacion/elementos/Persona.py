class Persona:
    def __init__(self, nombre, edad, cedula, telefono= None, direccion=None):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.telefono = telefono
        self.direccion = direccion

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad
    
    def setCedula(self, cedula):
        self.cedula = cedula

    def getCedula(self):
        return self.cedula
    
    def setTelefono(self, telefono):
        self.telefono = telefono

    def getTelefono(self):
        return self.telefono
    
    def setDireccion(self, direccion):
        self.direccion = direccion

    def getDireccion(self):
        return self.direccion
    
    def __str__(self):
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, Cedula: {self.cedula}, "
                f"Telefono: {self.telefono}, Direccion: {self.direccion}")