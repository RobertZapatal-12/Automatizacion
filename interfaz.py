import tkinter as tk
from read import CSVRead, Limpieza
from tkinter import filedialog


def root():

    reads = CSVRead()
    cleaner = Limpieza()
    dataframe = None

    root = tk.Tk()
    root.title("Doc cleaner")
    root.geometry("600x400")

    widget_showcsv = tk.LabelFrame(
        root, 
        text="Informaion del archivo", 
        padx= 5, 
        pady= 5
    )
    
    widget_showcsv.pack()

    label_filas = tk.Label(widget_showcsv, text="Filas:")
    label_filas.pack()

    label_columnas = tk.Label(widget_showcsv, text="Columnas:")
    label_columnas.pack()

    def seleccionar_archivo():
        nonlocal dataframe
        dataframe = reads.abrir()

        label_columnas.config(text=f"Columnas:{len(dataframe.columns)}"
        )
        label_filas.config(text=f"Filas:{len(dataframe)}")

        return dataframe

    button_selectcsv = tk.Button(
        root, 
        text="Selecciona un documento", 
        command=seleccionar_archivo
    )
    
    button_selectcsv.pack()

    def limpiar():
        nonlocal dataframe

        dataframe = cleaner.limpiar_nulos(dataframe)
        print("Nulos limpios")

        label_columnas.config(text=f"Columnas:{len(dataframe.columns)}"
        )    
        label_filas.config(text=f"Filas:{len(dataframe)}")

        label_nulos = tk.Label(root, text=(f"Cantidad de nulos restantes por filas: {dataframe.isna().sum()}")
        )
        label_nulos.pack()

        return dataframe

    def limpiar_dup():
        nonlocal dataframe

        dataframe = cleaner.limpiar_duplicados(dataframe)
        print("Duplicados limpios")

        label_columnas.config(text=f"Columnas:{len(dataframe.columns)}"
                )    
        label_filas.config(text=f"Filas:{len(dataframe)}")

        label_duplicados = tk.Label(root, text=(f"Cantidad de duplicados restantes por filas: {dataframe.duplicated().sum()}")
        )

        label_duplicados.pack()
        
                                      
    boton_limpiar = tk.Button(
        root, 
        text="Limpiar nulos",
        command= limpiar
    )

    boton_limpiar_duplicados = tk.Button(
            root, 
            text="Limpiar duplicados",
            command= limpiar_dup
        )


    boton_limpiar.pack()
    boton_limpiar_duplicados.pack()
        


    root.mainloop()

