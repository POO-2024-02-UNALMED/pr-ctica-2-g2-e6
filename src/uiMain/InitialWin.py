import tkinter as tk
from tkinter import Menu, messagebox
import sys
import os
import glob

# LÓPEZ GONZÁLEZ, ALEJANDRO
# BETANCUR URIBE, EMMANUEL

try:
    from PIL import Image, ImageTk
except ModuleNotFoundError:
    import subprocess
    print("Pillow no está instalado. Instalándolo ahora...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageTk

#Creacion ventana principal
window = tk.Tk()
window.title("Ventana Principal de Inicio")
window.geometry("800x600")
window.img_width = 240
window.img_height = 180

#Definicion de funciones
def mostrar_ventana_principal():
    window

def load_images_from_folder(folder_path):
    image_files = sorted(glob.glob(os.path.join(folder_path, "*.png")))
    return [load_and_resize(img) for img in image_files]


def load_and_resize(image_path):
    img = Image.open(image_path)
    img = img.resize((window.img_width, window.img_height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)


def cambiar_imagen(event):
    window.img_index = (window.img_index + 1) % len(window.blue_images)
    window.label_img.config(image=window.blue_images[window.img_index])


def cambiar_texto(event):
    window.text_index = (window.text_index + 1) % len(window.texts)
    window.label_text.config(text=window.texts[window.text_index])
    
    for i, lbl in enumerate(window.p2_labels):
        lbl.config(image=window.image_sets[window.text_index][i])

def info_app():
    messagebox.showinfo("Aplicación", "Está es la aplicación de UNmascota, un sistema de gestión veterinaria para tu mascota, servicios de tienda, osario y nutricionista.")

def salir_app():
    window.quit()

def ingresar_sistema():
    window.destroy()
    import MainWin

#Cargar Imagenes
window.image_sets = [load_images_from_folder(f"images/set{i}") for i in range(1, 6)]
window.blue_images = load_images_from_folder("images/blue")
window.img_index = 0
window.text_index = 0

#Textos hojas de vida
window.texts = ["Tomas Ospina:Tengo 18 años, nacido en \nMedellín y estudiante de Ingeniería de Sistemas\nen la UNAL Medellín. ", 
                "Melanie Bula:Soy de Sahagún, tengo 17 años \ny soy estudiante de ingeniería de sistemas\nen la universidad nacional de Colombia.", 
                "Santiago Martínez Ríos:Tengo 22 años, soy de \nMedellín y estudio Ingeniería de Sistemas en la\nUniversidad Nacional de Colombia", 
                "Emmanuel Betancur:Tengo 17 años, soy de Medellín\ny estudio Ingeniería de Sistemas en la Universidad\nNacional de Colombia.", 
                "Alejandro López:Tengo 21 años y soy estudiante\nde ingenierìa de sistemas en la\nuniversidad nacional de Colombia."]

#Menu inicio
menu = tk.Menu(window)
window.config(menu=menu)
inicio_menu = tk.Menu(menu, tearoff=0)
inicio_menu.add_command(label="Acerca De:", command=info_app)
inicio_menu.add_separator()
inicio_menu.add_command(label="Salir", command=salir_app)
menu.add_cascade(label="Inicio", menu=inicio_menu)

#Frame principal
main_frame = tk.Frame(window)
main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

#Subframes
frame_p1 = tk.Frame(main_frame, bg="lightblue")
frame_p2 = tk.Frame(main_frame, bg="lightpink")
frame_p3 = tk.Frame(main_frame, height=100, bg="lightblue")
#frame_p4 = tk.Frame(main_frame, height=100, bg="lightyellow")
frame_p5 = tk.Frame(main_frame, height=100, bg="lightpink")
frame_p1 = tk.Frame(main_frame, bg="lightblue")
frame_p2 = tk.Frame(main_frame, bg="lightpink")
frame_p4 = tk.Frame(main_frame, height=100, bg="lightyellow")

#Posicion Frames
frame_p3.grid(row=0, column=0, sticky="nsew")
frame_p5.grid(row=0, column=1, columnspan=2, sticky="nsew")
frame_p1.grid(row=1, column=0, sticky="nsew")
frame_p2.grid(row=1, column=1, columnspan=2, sticky="nsew")
frame_p3.grid(row=0, column=0, columnspan=1, sticky="nsew")
#frame_p4.grid(row=2, column=0, columnspan=3, sticky="sew") 
frame_p5.grid(row=0, column=1, columnspan=2, sticky="nsew")

#Posicion de Columas y figuras
main_frame.columnconfigure(0, weight=1)  
main_frame.columnconfigure(1, weight=1)  
main_frame.columnconfigure(2, weight=1) 
#main_frame.rowconfigure(0, weight=0)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=0)

#Bienvenida
label_saludo = tk.Label(frame_p3, text="Bienvenido al \ncentro veterinario: \nUNmascota", font=("Arial", 18), fg="blue", bg="lightblue")
label_saludo.pack(pady=20)

#Ingreso a la app principal
btn_ingresar = tk.Button(main_frame, text="Ingresar", font=("Arial", 12), command=ingresar_sistema)
btn_ingresar.place(x=10, rely=0.95, anchor="sw")

#Slide de imagenes principales
window.label_img = tk.Label(frame_p1, image=window.blue_images[window.img_index])
window.label_img.pack(expand=False, pady=65)
window.label_img.bind("<Enter>", cambiar_imagen)

#Imagenes de Hojas de vida
window.p2_labels = []
for i in range(2):
    frame_p2.rowconfigure(i, weight=1)
    for j in range(2):
        frame_p2.columnconfigure(j, weight=1)
        lbl = tk.Label(frame_p2, image=window.image_sets[window.text_index][i * 2 + j], bg='lightpink')
        lbl.grid(row=i, column=j, padx=2, pady=2, sticky='nsew')
        window.p2_labels.append(lbl)

#Eventos hoja de vida
window.label_text = tk.Label(frame_p5, text=window.texts[window.text_index], font=("Arial", 16), cursor="hand2", fg="green", bg="lightpink")
window.label_text.pack(pady=20)
window.label_text.bind("<Button-1>", cambiar_texto)

#Inicio del programa
window.mainloop()