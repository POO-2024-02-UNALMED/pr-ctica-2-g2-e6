import tkinter as tk
from tkinter import messagebox
import tkinter as tk

class FieldFrame(tk.Frame):
    def __init__(self, master, criterio_label, criterios, valor_label):
        super().__init__(master)
        self.criterios = criterios
        self.entries = {}
        
        criterio_label = tk.Label(self, text=criterio_label)
        criterio_label.grid(row=0, column=0)

        valor_label = tk.Label(self, text=valor_label)
        valor_label.grid(row=0, column=1)

        for idx, criterio in enumerate(criterios):
            criterio_label = tk.Label(self, text=criterio)
            criterio_label.grid(row=idx+1, column=0)
            entry = tk.Entry(self)
            entry.grid(row=idx+1, column=1)
            self.entries[criterio] = entry

    def getValue(self, criterio):
        return self.entries[criterio].get()

    def setValue(self, criterio, value):
        self.entries[criterio].delete(0, tk.END)
        self.entries[criterio].insert(0, value)

    def disableEntry(self, criterio):
        self.entries[criterio].config(state='readonly')

    def enableEntry(self, criterio):
        self.entries[criterio].config(state='normal')