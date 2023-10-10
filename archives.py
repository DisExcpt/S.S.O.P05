import os
import tkinter as tk  
from tkinter import filedialog


class folders:
    def __init__(self):
        self.root = ''
        self.archives = []
        
    def selectRoot(self):
        root = tk.Tk()  # esto se hace solo para eliminar la ventanita de Tkinter
        root.withdraw()  # ahora se cierra
        file_path = filedialog.askdirectory()
        self.root = file_path
        return self.root+'/'
    
    def formarRute(self):
        newRute = ''
        for char in self.root:
            if(char == '\\'):
                newRute += '/'
            else:
                newRute += char
        return newRute
    
    def selectElements(self,root_dir):
        folder_list = []
        
        for file in os.listdir(root_dir):
            name,ext = os.path.splitext(root_dir+file)
            size = os.path.getsize(name+ext)
            # print(file,name,ext,size)
            string = '{},{}'.format(file,size)
            self.archives.append(string)
            if ext in ['']:
                folder_list.append(name)
        
        for i in range(len(folder_list)):
            self.selectElements(folder_list[i]+'/')
        
    def getArchives(self):
        return self.archives