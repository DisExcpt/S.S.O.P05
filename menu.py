import os,time as tm
from rich.progress import Progress
from rich.theme import Theme
from rich.console import Console
from memory import *
from ajsutes import *
from archives import *
from rich.prompt import Prompt

timeSleep = 7

custom_theme = Theme({
    'menu':'#aaffaa',
    'opc':'yellow',
    'exit':'#ff0000',
    'ask':'#00a0ff',
    'list':'#ae34fe',
    'pr1':'#af45ec'

})
console = Console(theme=custom_theme)
class menu:
    def __init__(self):
        # obteniendo los valores del archivo inicial
        self.test = folders()
        self.root = self.test.selectRoot()
        self.test.selectElements(self.root)
        self.process = self.test.getArchives()
        # process = gd.getData()
        self.procesos = []
        self.ultimo_asignado = 0  # Inicializamos el índice del último asignado en 0
        for i in self.process:
            lista = i.split(',')
            tam = lista[1].split('kb' or '')
            self.procesos.append((lista[0],int(tam[0])))
    
    def exit(self):
        with Progress() as progress:
            task1 = progress.add_task("[blue]Saliendo...", total=100)
            while not progress.finished:
                progress.update(task1, advance=2)
                tm.sleep(0.02) 

        os.system('cls')   

    def menu(self):
        memoria_total = [MemoryBlock(0,1000),
                MemoryBlock(1000,400),
                MemoryBlock(1400,1800),
                MemoryBlock(3200,700),
                MemoryBlock(3900,900),
                MemoryBlock(4800,1200),
                MemoryBlock(6000,1500),
                MemoryBlock(7500,6500),
                MemoryBlock(14000,75000),
                ]
        console.print('[pr1]estado inicial de la memoria[\pr1]: ')
        

        console.print(self.procesos)

        for bloque in memoria_total:
            console.print(f'Bloque {bloque.start}-{bloque.start + bloque.size - 1}:{bloque.process or "libre"}')
        
    

        
        console.print("[opc]1.-[/opc] [menu]Agregar proceso[/menu]"
                    "\n[opc]2.-[/opc] Primer ajuste"
                    "\n[opc]3.-[/opc] Mejor ajuste"
                    "\n[opc]4.-[/opc] Peor ajuste"
                    "\n[opc]5.-[/opc] Rsiguiente ajuste"
                    "\n[opc]6.-[/opc] Liberar memoria"
                    "\n[opc]7.-[/opc] [exit]Salir[/exit]")
        opc = input("Digita la opcion que deseas realizar: ")
        match opc:
            case '1':
                os.system('cls')
                name = Prompt.ask("[ask]Digita el nombre del proceso[/ask] ",console=console)
                size = Prompt.ask("[ask]Digita el tamaño del proceso[/ask] ",console=console)
                self.procesos.append((name,int(size)))
                os.system('cls')
                return self.menu()
            case '2':
                os.system('cls')  
                for proceso,tamanio in self.procesos:
                    if primer_ajuste(memoria_total,proceso,tamanio):
                        console.print(f"Se asigno memoria a {proceso} usando Primer Ajueste.")
                    else:
                        console.print(f"No se pudo asignar memoria a {proceso} usando primer ajuste")

                console.print("Estado de la memoria despues de asignar memoria usando Primer ajuste")
                for bloque in memoria_total:
                    console.print(f"Bloque {bloque.start}-{bloque.start + bloque.size -1}: {bloque.process or 'libre'}")
                # reiniciar la memoria antes de usar mejor y peor
                for bloque in memoria_total:
                    bloque.process = None
                tm.sleep(timeSleep) 
                os.system('cls')  
                return self.menu() 
            case '3':
                os.system('cls')  
                for proceso,tamanio in self.procesos:
                    if mejor_ajuste(memoria_total,proceso,tamanio):
                        console.print(f"Se asigno memoria a {proceso} usando Mejor Ajuste")
                    else:
                        console.print(f"No se pudo asignar memoria a {proceso} usando Mejor ajuste")
                console.print("Estado de la memoria despues de asignar memoria usando Mejor Ajuste:")
                for bloque in memoria_total:
                    console.print(f"Bloque {bloque.start}-{bloque.start+bloque.size - 1}: {bloque.process or 'libre'}")

                # reiniciar la memoria antes de usar Peor ajuste
                for bloque in memoria_total:
                    bloque.process = None
                tm.sleep(timeSleep) 
                os.system('cls')  
                return self.menu()
            case '4':
                os.system('cls') 
                for proceso,tamanio in self.procesos:
                    if peor_ajuste(memoria_total,proceso,tamanio):
                        console.print(f"Se asino la memoria a {proceso} usando Peor ajuste")
                    else:
                        console.print(f"No se pudo asignar memoria a {proceso} usando Peor ajuste.")
                console.print("Estado de la memoria despues de Asignar memoria usando Peor ajuste")
                for bloque in memoria_total:
                    console.print(f"Bloque {bloque.start}-{bloque.start + bloque.size - 1}:{bloque.process or 'libre'}")

                # Reiniciar la memoria antes de usar Siguiente Ajuste
                for bloque in memoria_total:
                    bloque.process = None
                tm.sleep(timeSleep) 
                os.system('cls') 
                return self.menu()
            case '5':
                os.system('cls')  
                console.print("Usando Siguiente Ajuste:")
                for proceso, tamano in self.procesos:
                    self.ultimo_asignado = siguiente_ajuste(memoria_total, proceso, tamano, self.ultimo_asignado)
                    if self.ultimo_asignado != -1:
                        console.print(f"Se asignó memoria a {proceso} usando Siguiente Ajuste.")
                    else:
                        console.print(f"No se pudo asignar memoria a {proceso} usando Siguiente Ajuste.")

                console.print("Estado de la memoria después de asignar memoria usando Siguiente Ajuste:")
                for bloque in memoria_total:
                    console.print(f"Bloque {bloque.start}-{bloque.start + bloque.size - 1}: {bloque.process or 'Libre'}")

                tm.sleep(timeSleep) 
                os.system('cls') 
                return self.menu()
            case '6':
                os.system('cls') 
                # liberar memoria (puedes utilizar la funcion liberar memoria existente)
                for proceso,_ in self.procesos:
                    liberar_memoria(memoria_total,proceso)

                console.print("Estado de la memoria despues de liberar memoria:")
                for bloque in memoria_total:
                    console.print(f"Bloque {bloque.start}-{bloque.start + bloque.size -1}:{bloque.process or 'libre'}")
                tm.sleep(4) 
                os.system('cls') 
                return self.menu()
            
            case '7':
                exit()
            



