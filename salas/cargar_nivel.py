from salas.leer_salas import cargar_mapa
from salas.buscar_jugador import buscar_jugador
from salas.buscar_enemigos import buscar_enemigos
from salas.mundo import archivos_salas

def cargar_nivel(sala, estado_salas):
    
    archivo = archivos_salas[sala]
    
    mapa = cargar_mapa(archivo)
    
    if sala == "salas/sala_llave.txt":

        if estado_salas["llave"]["llave"] == False:

            for y in range(len(mapa)):

                for x in range(len(mapa[y])):

                    if mapa[y][x] == "K":

                        mapa[y][x] = " "
                        
    elif sala == "salas/sala_puerta.txt":
        
        if estado_salas["puerta"]["puerta"] == False:

            for y in range(len(mapa)):

                for x in range(len(mapa[y])):

                    if mapa[y][x] == "D":

                        mapa[y][x] = " "
                        
        

    jugador_x, jugador_y = buscar_jugador(mapa)

    enemigos = buscar_enemigos(mapa)
    
    muertos = estado_salas["enemigos"].get(sala, [])
    
    

    enemigos = [
        e for e in enemigos
        if e["id"] not in muertos
    ]
        
    return mapa, jugador_x, jugador_y, enemigos

#print(cargar_mapa("sala_prueba.txt"))

