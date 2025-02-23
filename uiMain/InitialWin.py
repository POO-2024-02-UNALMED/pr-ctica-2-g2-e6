import tkinter as tk
from tkinter import Menu, messagebox
import sys
import os
import glob

try:
    from PIL import Image, ImageTk
except ModuleNotFoundError:
    import subprocess
    print("Pillow no está instalado. Instalándolo ahora...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageTk

window = tk.Tk()
window.title("Ventana Principal de Inicio")
window.geometry("1024x768")
window.img_width = 300
window.img_height = 225


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


def ingresar_sistema():
    print("Ingresando al sistema...")

window.image_sets = [load_images_from_folder(f"images/set{i}") for i in range(1, 6)]
window.blue_images = load_images_from_folder("images/blue")
window.img_index = 0
window.text_index = 0

window.texts = ["Tomas Ospina", "Melanie Bula", "Santiago", "Emmanuel Betancur Uribe", "Alejandro López"]

main_frame = tk.Frame(window)
main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

frame_p3 = tk.Frame(main_frame, height=100, bg="lightgrey")
frame_p5 = tk.Frame(main_frame, height=100, bg="lightpink")
frame_p1 = tk.Frame(main_frame, bg="lightblue")
frame_p2 = tk.Frame(main_frame, bg="lightgreen")
frame_p4 = tk.Frame(main_frame, height=100, bg="lightyellow")

frame_p3.grid(row=0, column=0, columnspan=2, sticky="nsew")
frame_p5.grid(row=0, column=2, sticky="nsew")
frame_p1.grid(row=1, column=0, sticky="nsew")
frame_p2.grid(row=1, column=1, columnspan=2, sticky="nsew")
frame_p4.grid(row=2, column=0, columnspan=3, sticky="sew")

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)
main_frame.rowconfigure(0, weight=0)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=0)

label_saludo = tk.Label(frame_p3, text="¡Bienvenido al sistema!", font=("Arial", 12))
label_saludo.pack(pady=20)

btn_ingresar = tk.Button(frame_p4, text="Ingresar", font=("Arial", 12), command=ingresar_sistema)
btn_ingresar.pack(side='left', padx=20, pady=20)

window.label_img = tk.Label(frame_p1, image=window.blue_images[window.img_index])
window.label_img.pack(expand=True, pady=20)
window.label_img.bind("<Enter>", cambiar_imagen)

window.p2_labels = []
for i in range(2):
    frame_p2.rowconfigure(i, weight=1)
    for j in range(2):
        frame_p2.columnconfigure(j, weight=1)
        lbl = tk.Label(frame_p2, image=window.image_sets[window.text_index][i * 2 + j], bg='lightgreen')
        lbl.grid(row=i, column=j, padx=2, pady=2, sticky='nsew')
        window.p2_labels.append(lbl)

window.label_text = tk.Label(frame_p5, text=window.texts[window.text_index], font=("Arial", 12), cursor="hand2")
window.label_text.pack(pady=20)
window.label_text.bind("<Button-1>", cambiar_texto)

#def run():
#    window.mainloop()

window.mainloop()
