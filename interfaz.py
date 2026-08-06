import tkinter as tk
from read import abrir
from tkinter import filedialog

def root():
    root = tk.Tk()
    root.title("Doc cleaner")
    root.geometry("600x400")

    button_selectcsv = tk.Button(root, text="Selecciona un documento", command=abrir)
    button_selectcsv.pack()


    widget_showcsv = tk.LabelFrame(root, text="Informaion del archivo", padx= 5, pady= 5)
    widget_showcsv.pack()

    tk.Label(widget_showcsv, text="Archivo:").pack()
    tk.Label(widget_showcsv, text="Filas:").pack()
    tk.Label(widget_showcsv, text="Columnas:").pack()

    # checkbutton = tk.Checkbutton(ventana, text= "Limpiar nulos")
    # checkbutton.grid()
    root.mainloop()