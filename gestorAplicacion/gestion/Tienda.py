from gestorAplicacion.elementos import CentroAdopcion
from gestorAplicacion.elementos.Producto import Producto


class Tienda:
    # Listas estáticas para la serialización
    productos = []
    empleados = []

    def __init__(self, empleado, centro_adopcion=None):
        Tienda.empleados.append(empleado)
        self.centro_adopcion = centro_adopcion

    # Getters y Setters
    def set_centro_adopcion(self, centro_adopcion):
        self.centro_adopcion = centro_adopcion

    def get_centro_adopcion(self):
        return self.centro_adopcion

    @staticmethod
    def get_productos():
        return Tienda.productos

    @staticmethod
    def get_empleados():
        return Tienda.empleados

    def set_productos(self, productos):
        Tienda.productos = productos

    def set_empleados(self, empleados):
        Tienda.empleados = empleados

    # Métodos
    def agregar_empleado(self, empleado):
        Tienda.empleados.append(empleado)

    def empleados_tienda(self):
        return Tienda.empleados

    @staticmethod
    def agregar_producto(producto):
        if Tienda.empleados:
            Tienda.productos.append(producto)

    def inventario(self):
        if Tienda.empleados:
            resultado = ""
            for i, producto in enumerate(Tienda.productos, start=1):
                resultado += f"{i}. {producto}\n"
            return resultado
        else:
            return "🚫Lo lamentamos pero el centro UNamascota no tiene empleados disponibles para atender su solicitud.🚫"

    def filtrar(self, tipo):
        if Tienda.empleados:
            resultado = ""
            for i, producto in enumerate(Tienda.productos, start=1):
                if producto.get_tipo_animal() == tipo or producto.get_tipo_animal() == "Uso general":
                    resultado += f"{i}. {producto}\n"
            return resultado
        else:
            return "🚫Lo lamentamos pero el centro UNamascota no tiene empleados disponibles para atender su solicitud.🚫"

    def compra(self, indice, cliente, unidades=1):
        if Tienda.empleados:
            indice -= 1
            if indice >= len(Tienda.productos) or indice < 0:
                return "🚫¡Oh no!, verifica que el índice del producto sea el indicado, el centro UNamascota desconoce ese índice.🚫"

            producto = Tienda.productos[indice]
            cantidad = producto.get_cantidad_unidades()

            if cantidad > 0 and cantidad >= unidades:
                cantidad -= unidades
                producto.set_cantidad_unidades(cantidad)

                nombre = producto.get_nombre()
                tipo = producto.get_tipo_animal()
                precio = producto.get_precio() * unidades

                if cantidad == 0:
                    Tienda.productos.pop(indice)

                cliente = CentroAdopcion.es_cliente(cliente)
                puntos = cliente.get_puntos()

                if puntos >= 15:
                    cliente.disminuir_puntos(15)
                    precio *= 0.9  # Aplicar 10% de descuento
                    return (f"-------------------------------------------\n"
                            f"Has comprado {unidades} unidades de: {nombre} - Dirigido a: {tipo}\n"
                            f"Total a pagar: {precio} $\n"
                            f"Han sido descontados 15 puntos para un 10% de descuento\n"
                            f"Puntos restantes en tu cartera de puntos: {cliente.get_puntos()}\n"
                            f"-------------------------------------------")
                else:
                    return (f"-------------------------------------------\n"
                            f"Has comprado {unidades} unidades de: {nombre} - Dirigido a: {tipo}\n"
                            f"Total a pagar: {precio} $\n"
                            f"No cuentas con los suficientes puntos como para un descuento\n"
                            f"-------------------------------------------")
            else:
                return "🚫¡Oh no!, verifica la cantidad de unidades disponibles en la tienda y vuelve a intentarlo.🚫"
        else:
            return "🚫Lo lamentamos pero el centro UNamascota no tiene empleados disponibles para atender su solicitud.🚫"

    def __str__(self):
        return f"Tienda con empleados: {self.empleados_tienda()}"