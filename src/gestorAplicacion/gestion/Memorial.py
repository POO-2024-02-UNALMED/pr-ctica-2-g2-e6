from gestorAplicacion.elementos import Fallecido
from gestorAplicacion.elementos.centroAdopcion import CentroAdopcion

class Memorial:
    tumbas = []
    osarios = []
    arboles = []
    cenizas = []

    def __init__(self, centro: CentroAdopcion):
        self.centro = centro

    def get_centro(self) -> CentroAdopcion:
        return self.centro

    def get_nombre(self) -> str:
        return self.centro.get_nombre()

    def set_centro(self, centro: CentroAdopcion):
        self.centro = centro

    @classmethod
    def get_tumbas(cls) -> list:
        return cls.tumbas

    @classmethod
    def get_osarios(cls) -> list:
        return cls.osarios

    @classmethod
    def get_arboles(cls) -> list:
        return cls.arboles

    @classmethod
    def get_cenizas(cls) -> list:
        return cls.cenizas

    def visita(self, tipo: str) -> str:
        if tipo == "Tumbas":
            return self.visita_memorial(self.tumbas)
        elif tipo == "Osarios":
            return self.visita_memorial(self.osarios)
        elif tipo == "Arbol":
            return self.visita_memorial(self.arboles)
        elif tipo == "Cenizas":
            return self.visita_memorial(self.cenizas)
        return ""

    def visita_memorial(self, lista: list) -> str:
        resultado = ""
        for i, fallecido in enumerate(lista, 1):
            resultado += f"{i}, {fallecido}\n"
        return resultado

    def anadir_sepulcro(self, tumba: Fallecido):
        tumba.set_tipo("Tumba")
        self.tumbas.append(tumba)

    def anadir_osario(self, huesos: Fallecido):
        huesos.set_tipo("Osario")
        self.osarios.append(huesos)

    def anadir_arbol(self, arbol: Fallecido):
        arbol.set_tipo("Arbol")
        self.arboles.append(arbol)

    def anadir_cenizas(self, ceniza: Fallecido):
        ceniza.set_tipo("Cenizas")
        self.cenizas.append(ceniza)

    def obtener_fallecidos_por_tipo(self, tipo: str) -> list:
        if tipo == "Tumba":
            return self.tumbas.copy()
        elif tipo == "Osario":
            return self.osarios.copy()
        elif tipo == "Cenizas":
            return self.cenizas.copy()
        elif tipo == "Arbol":
            return self.arboles.copy()
        return []

    def cupos(self, tipo: str) -> bool:
        if tipo == "Tumba":
            return len(self.tumbas) < 20
        elif tipo == "Osario":
            return len(self.osarios) < 20
        elif tipo == "Cenizas":
            return len(self.cenizas) < 20
        elif tipo == "Arbol":
            return len(self.arboles) < 30
        else:
            raise ValueError("Tipo de memorial no válido.")

    def anadir_fallecido(self, fallecido: Fallecido, tipo: str) -> bool:
        if tipo == "Tumba":
            self.anadir_sepulcro(fallecido)
        elif tipo == "Osario":
            self.anadir_osario(fallecido)
        elif tipo == "Cenizas":
            self.anadir_cenizas(fallecido)
        elif tipo == "Arbol":
            self.anadir_arbol(fallecido)
        else:
            return False
        return True