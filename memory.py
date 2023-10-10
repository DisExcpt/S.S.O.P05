class MemoryBlock:
    """ simulacion de los algoritmos de administracion de memoria
        \n-premer ajuste
        \n mejor ajuste
        \n peor ajuste
    """
    
    def __init__(self,start, size):
        """
        start direccion de incio de bloque de memeorias  \n
        size tamanio del bloque de memoria \n
        process el proceso asignado \n
        """
        self.start = start
        self.size = int(size)
        self.process = None
