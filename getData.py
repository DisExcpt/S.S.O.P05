from io import open
import tkinter as tk  # this is the preferred import for tkinter
from tkinter import filedialog

def getData():
    root = tk.Tk()  # esto se hace solo para eliminar la ventanita de Tkinter
    root.withdraw()  # ahora se cierra
    file_path = filedialog.askopenfilename()
    archive = open(file_path)
    try:
        arc = archive.readlines()
        archive.close()
        data = []
        for i in arc:
            data.append(i)
        return data
    except:
        print('Error al abrir el archivo')
        archive.close()
