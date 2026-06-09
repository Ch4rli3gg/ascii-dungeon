from salas.leer_salas import cargar_mapa
from salas.buscar_jugador import buscar_jugador
from salas.buscar_enemigos import buscar_enemigos

def cargar_nivel(sala):
    
    mapa = cargar_mapa(sala)

    jugador_x, jugador_y = buscar_jugador(mapa)

    enemigos = buscar_enemigos(mapa)
    
    return mapa, jugador_x, jugador_y, enemigos

#print(cargar_mapa("sala_prueba.txt"))

