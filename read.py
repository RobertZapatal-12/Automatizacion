import pandas as pd
import tkinter as tk
from tkinter import filedialog


class CSVRead():
    def __init__(self):
        self.dataframe = None

    def abrir(self):
        self.dataframe = tk.filedialog.askopenfile(mode = "r", )

        if self.dataframe:
            print("Archivo cargado correctamente")
            self.dataframe = pd.read_csv(
                self.dataframe,
                encoding= "cp1252"
        )

        return self.dataframe

class Limpieza:
    def __init__(self):
        pass
        
    def limpiar_nulos(self, dataframe):
        if dataframe is None:
            print("Carga un dataframe primero")
            return dataframe
        
        dataframe = dataframe.dropna()
        return dataframe


    def limpiar_duplicados(self, dataframe):
        if dataframe is None:
            print("Carga un dataframe primero")
            return dataframe

        dataframe = dataframe.drop_duplicates()
        return dataframe



    
