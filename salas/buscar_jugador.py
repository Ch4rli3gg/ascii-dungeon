from leer_salas import cargar_mapa

def buscar_jugador(mapa):
    
    for y in range(len(mapa)):
        
        for x in range(len(mapa[y])):
            
            if mapa[y][x] == "@":
                
                return x,y
            
    #por si la sala no tiene @:
    return None
            
#mapa = cargar_mapa("sala_inicio.txt")
#print(buscar_jugador(mapa))