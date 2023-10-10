from memory import *

def primer_ajuste(memoria:list, proceso:list, size):
    for bloque in memoria:
        if bloque.process is None and bloque.size >= size:
            bloque.process = proceso
            #dividimos si es necesario
            if bloque.size > size:
                bloque.size -= size
                #crear un nuevo bloque para el espacio restante
                index = memoria.index(bloque)
                memoria.insert(index, MemoryBlock(bloque.start+size, bloque.size))
            return True
    # No se pudo asignar la memoria papu
    return False 

def mejor_ajuste(memoria:list, proceso, size):
    mejor_bloque = None
    for bloque in memoria:
        if bloque.process is None and bloque.size >= size:
            if mejor_bloque is None or bloque.size < mejor_bloque.size:
                mejor_bloque = bloque
    if mejor_bloque is not None:
        mejor_bloque.process = proceso
        # dividimos el proceso
        if mejor_bloque.size > size:
            mejor_bloque.size -= size
            # creamos un nuevo bloque para el espacio restante
            index = memoria.index(mejor_bloque)
            memoria.insert(index, MemoryBlock(mejor_bloque.start+size,mejor_bloque.size))
        return True
    # no se pudo asignar memoria
    return False

def peor_ajuste(memoria:list,proceso,size):
    peor_bloque = None
    for bloque in memoria:
        if bloque.process is None and bloque.size >= size:
            if peor_bloque is None or bloque.size > peor_bloque.size:
                peor_bloque = bloque
    if peor_bloque is not None:
        peor_bloque.process = proceso
        # dividimos el proceso
        if peor_bloque.size > size:
            index = memoria.index(peor_bloque)
            memoria.insert(index, MemoryBlock(peor_bloque.start+size,peor_bloque.size))
        return True
    # no se puso asignar
    return False

def siguiente_ajuste(memoria, proceso, tamano, ultimo_asignado):
    for bloque in memoria[ultimo_asignado:] + memoria[:ultimo_asignado]:  # Recorremos desde el último asignado hasta el principio y luego desde el principio hasta el último asignado
        if bloque.process is None and bloque.size >= tamano:
            bloque.process = proceso
            # Dividir el bloque si es necesario
            if bloque.size > tamano:
                bloque.size -= tamano
                # Crear un nuevo bloque para el espacio restante
                index = memoria.index(bloque)
                memoria.insert(index, MemoryBlock(bloque.start + tamano, bloque.size))
            return memoria.index(bloque)  # Devolvemos el índice del bloque asignado

    return -1  # No se pudo asignar memoria

def liberar_memoria(memoria:list,proceso):
    for bloque in  memoria:
        if bloque.process == proceso:
            bloque.process = None
            # se juntan denuevo los bloques de memoria si es posoble
            index = memoria.index(bloque)
            if index > 0 and memoria[index - 1].process is None:
                bloque_anterior = memoria.pop(index-1)
                bloque.start = bloque_anterior.start
                bloque.size += bloque_anterior.size
            if index < len(memoria) - 1 and memoria[index + 1].process is None:
                bloque_siguiente = memoria.pop(index + 1)
                bloque.size += bloque_siguiente.size
    return True

