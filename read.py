import pandas as pd
import tkinter as tk
from tkinter import filedialog

def abrir():
    archivo = tk.filedialog.askopenfile(mode = "r")
    print(f"Archivo cargado correctamente")

def limpiar_nulos():
    df = pd.read_csv("archivo")
    df.dropna()





    


