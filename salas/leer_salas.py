def cargar_mapa(archivo):
    mapa = []
    
    with open(archivo) as f:
        
        contenido= f.read()
    
    for fila in contenido.splitlines():
        mapa.append(list(fila))
        
    return(mapa)
        
    
