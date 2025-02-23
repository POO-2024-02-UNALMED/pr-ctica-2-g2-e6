import json

class Dieta:
    def __init__(self, mascota):
        self.mascota = mascota
        self.pesoIdeal = 0
        self.gramosDiarios = 0
        self.proteinas = 0
        self.grasas = 0
        self.carbohidratos = 0

    # Métodos de cálculo
    def calcularPesoIdeal(self):
        tamano = self.mascota.tamano
        edad = self.mascota.edad
        pesoActual = self.mascota.peso
        self.pesoIdeal = ((tamano * 10.0) / (edad + 1)) + (pesoActual / 2)

    def comparacionPeso(self):
        if self.mascota.peso == self.pesoIdeal:
            return 1  # Peso ideal
        elif self.mascota.peso < self.pesoIdeal:
            return 2  # Necesita subir de peso
        else:
            return 3  # Necesita bajar de peso

    def planDieta(self):
        self.gramosDiarios = self.pesoIdeal * self.mascota.tamano * 10
        comparacion = self.comparacionPeso()

        if comparacion == 1:  # Peso ideal
            self.grasas = self.gramosDiarios * 0.20
            self.proteinas = self.gramosDiarios * 0.30
            self.carbohidratos = self.gramosDiarios * 0.50
        elif comparacion == 2:  # Subir de peso
            self.grasas = self.gramosDiarios * 0.30
            self.proteinas = self.gramosDiarios * 0.40
            self.carbohidratos = self.gramosDiarios * 0.30
        elif comparacion == 3:  # Bajar de peso
            self.grasas = self.gramosDiarios * 0.15
            self.proteinas = self.gramosDiarios * 0.50
            self.carbohidratos = self.gramosDiarios * 0.35

    def __str__(self):
        estadoPeso = {
            1: "Está en su peso ideal.",
            2: "Debe subir de peso.",
            3: "Debe bajar de peso."
        }.get(self.comparacionPeso(), "Estado no definido.")

        return (f"Nombre de la mascota: {self.mascota.nombre}\n"
                f"Peso Actual: {self.mascota.peso} kg\n"
                f"Edad: {self.mascota.edad} años\n"
                f"Tamaño: {self.mascota.getTamanoStr}\n"
                f"Peso ideal: {round(self.pesoIdeal, 2)} kg\n"
                f"Cantidad de Gramos de alimento diarios: {round(self.gramosDiarios, 2)} g\n"
                f"{estadoPeso}\n\n"
                f"Distribución en porcentajes de nutrientes:\n"
                f" Proteínas: {round((self.proteinas / self.gramosDiarios) * 100, 2)}%\n"
                f" Grasas: {round((self.grasas / self.gramosDiarios) * 100, 2)}%\n"
                f" Carbohidratos: {round((self.carbohidratos / self.gramosDiarios) * 100, 2)}%\n\n"
                f"Distribución en gramos de nutrientes:\n"
                f" Proteínas: {round(self.proteinas, 2)} g\n"
                f" Grasas: {round(self.grasas, 2)} g\n"
                f" Carbohidratos: {round(self.carbohidratos, 2)} g")

    def menu(self):
        try:
            ruta = f"./src/src/basedatos/dieta_{self.mascota.nombre}.txt"
            with open(ruta, "w", encoding="utf-8") as archivo:
                archivo.write(str(self))
            print(f"Archivo de dieta guardado con éxito en basedatos/dieta.")
        except Exception as e:
            print(f"Error al guardar el archivo de dieta: {e}")
