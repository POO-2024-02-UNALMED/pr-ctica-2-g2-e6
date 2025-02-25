from tkinter import *
from tkinter import ttk
class FieldFrame(Frame):
    def __init__(self, ventana, tituloCriterios="", criterios=[], tituloValores="", valores=None, habilitado=None):
        super().__init__(ventana)
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._habilitado = habilitado
        self._elementos = []

        # Configuración de estilo
        self.configure(bg='#f7f7f7')  # Fondo más claro
        estilo_etiqueta = {'font': ("Poppins", 12, 'bold'), 'bg': '#f7f7f7', 'fg': '#333'}
        estilo_campo = {'font': ("Poppins", 11), 'bg': '#ffffff', 'fg': '#333', 'bd': 2, 'relief': GROOVE}

        # Crear y colocar titulo de los criterios
        etiquetaTituloCriterios = Label(self, text=tituloCriterios, font=("Poppins", 14, 'bold'), bg='#f7f7f7', fg='#000')
        etiquetaTituloCriterios.grid(column=1, row=0, padx=(10, 10), pady=(10, 10), sticky='ew')

        # Crear y colocar titulo de los valores
        etiquetaTituloValores = Label(self, text=tituloValores, font=("Poppins", 14, 'bold'), bg='#f7f7f7', fg='#000')
        etiquetaTituloValores.grid(column=2, row=0, padx=(10, 10), pady=(10, 10), sticky='ew')

        # Crear y colocar las etiquetas y campos de entrada para cada criterio
        for i in range(len(criterios)):
            etiquetaCriterio = Label(self, text=criterios[i], **estilo_etiqueta)
            etiquetaCriterio.grid(column=1, row=i + 1, padx=(10, 10), pady=(5, 5), sticky='e')

            campoValor = Entry(self, **estilo_campo)
            campoValor.grid(column=2, row=i + 1, padx=(10, 10), pady=(5, 5), sticky='ew')

            if valores is not None:
                campoValor.insert(0, valores[i])

            if habilitado is not None and not habilitado[i]:
                campoValor.configure(state=DISABLED)

            self._elementos.append(campoValor)

    def getValue(self, criterio):
        indice = self._criterios.index(criterio)
        return self._elementos[indice].get()

    def setValue(self, criterio, valor):
        indice = self._criterios.index(criterio)
        self._elementos[indice].delete(0, END)
        self._elementos[indice].insert(0, valor)

    def disableEntry(self, criterio):
        indice = self._criterios.index(criterio)
        self._elementos[indice].configure(state=DISABLED)

    def crearBotones(self, comando1, texto="Aceptar", pady=8, column=1, padx=5):
        estilo_boton = {
            'font': ("Poppins", 10, 'bold'),
            'fg': 'black',
            'bg': '#d3d3d3',  # Gris claro
            'activebackground': '#bfbfbf',
            'bd': 2,
            'relief': RAISED,
            'cursor': "hand2",
            'width': 12,
            'height': 1
        }
        Button(self, text=texto, command=comando1, **estilo_boton).grid(padx=padx, pady=pady, column=column, row=len(self._criterios) + 1, sticky='ew')

    def agregar_combobox(self, criterio, valores):
        indice = self._criterios.index(criterio)
        cuadroOpciones = ttk.Combobox(self, values=valores, state="readonly", font=("Poppins", 10))
        cuadroOpciones.grid(column=2, row=indice + 1, padx=(10, 10), pady=(5, 5), sticky='ew')
        self._elementos[indice] = cuadroOpciones