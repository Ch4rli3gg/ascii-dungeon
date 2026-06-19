from salas.buscar_jugador import buscar_jugador
from salas.buscar_enemigos import buscar_enemigos
from salas.cargar_nivel import cargar_nivel
from salas.mundo import conexiones

import os
import random
import msvcrt

NEGRO = "\033[30m"
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BLANCO = "\033[97m"

RESET = "\033[0m"

estado_salas = {

    "llave": {
        "llave": True
    },
    
    "puerta": {
        "puerta": True
    },
    
    "enemigos":{}

}

mapa, jugador_x, jugador_y, enemigos = cargar_nivel("inicio",estado_salas)

memoria = []

sala_actual="inicio"

for fila in mapa:

    nueva_fila = []

    for celda in fila:
        nueva_fila.append(False)

    memoria.append(nueva_fila)

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def dibujar():

    radio_vision = 4
    
    for y in range(len(mapa)):
        pixel= ""
        for x in range(len(mapa[y])):
            
            # distancia entre jugador y celda
            distancia = abs(x - jugador_x) + abs(y - jugador_y)
            if distancia <= radio_vision:
                memoria[y][x] = True

            # niebla de guerra
            """if distancia > radio_vision:
                
                if memoria[y][x]:
                    pixel += CYAN + "▒" + RESET
                else:
                    pixel += NEGRO + "░" + RESET
                continue"""

            # jugador
            if x == jugador_x and y == jugador_y:
                pixel += AZUL + "@" + RESET

            # enemigo
            
            
            else:
                enemigo_dibujado = False

            
                for enemigo in enemigos:

                    enemigo_x = enemigo["x"]
                    enemigo_y = enemigo["y"]
                    tipo = enemigo["tipo"]
                    

                    if x == enemigo_x and y == enemigo_y:

                        if tipo == "normal":
                            simbolo = "E"

                        
                        elif tipo == "loco":
                            simbolo = "C"

                        pixel += ROJO + simbolo + RESET
                        enemigo_dibujado = True
                        break
            # paredes
            #elif mapa[y][x] == "#":
                if not enemigo_dibujado:
                
                    if mapa[y][x] == "#":
                        pixel += CYAN + "█" + RESET

                    # salida
                    elif mapa[y][x] == "X":
                            pixel += VERDE + "X" + RESET
                    
                    elif mapa[y][x] == "K":
                        pixel += AMARILLO + "K" + RESET

                    elif mapa[y][x] == "D":
                        pixel += MAGENTA + "D" + RESET

                    # espacios vacíos
                    else:
                        pixel += " "

        print(pixel)
               
vidas = 3
nivel = 1
llaves = 0



def hud():
    print(CYAN + "=== LABERINTO TERMINAL ===" + RESET)
    print(f"{'❤️ ' * vidas}   🗺️ Nivel: {nivel}")
    print(f"🔑 Llaves: {llaves}")
    print("WASD para mover | Q para salir")
    print()    

def tecla():
        return msvcrt.getch().decode("utf-8").lower()
    
def mover_jugador(movimiento):

    global jugador_x, jugador_y, llaves
    global mapa, sala_actual, estado_salas
    global enemigos

    
    nueva_x = jugador_x
    nueva_y = jugador_y
    
    if movimiento == "w":
        nueva_y -= 1

    elif movimiento == "s":
        nueva_y += 1

    elif movimiento == "a":
        nueva_x -= 1

    elif movimiento == "d":
        nueva_x += 1

    #if mapa[nueva_y][nueva_x] != "#":
    

    destino = conexiones[sala_actual].get(
        (nueva_x, nueva_y)
    )
    

    if destino:

        mapa, jugador_x, jugador_y, enemigos = cargar_nivel(
            destino["sala"], estado_salas
        )

        sala_actual = destino["sala"]

        jugador_x, jugador_y = destino["spawn"]

        return
    
    if nueva_y < 0 or nueva_y >= len(mapa):
        return

    if nueva_x < 0 or nueva_x >= len(mapa[nueva_y]):
        return
    #    jugador_x, jugador_y = nueva_x, nueva_y
    celda = mapa[nueva_y][nueva_x]
    

    # pared
    if celda == "#":
        return

    # recoger llave
    if celda == "K":
        llaves += 1
        mapa[nueva_y][nueva_x] = " "
        estado_salas["llave"]["llave"] = False

    # puerta
    if celda == "D":

        if llaves > 0:
            llaves -= 1
            mapa[nueva_y][nueva_x] = " "
            estado_salas["puerta"]["puerta"] = False
            

        else:
            return

    jugador_x, jugador_y = nueva_x, nueva_y

def mover_enemigos():

    global enemigos

    nuevos_enemigos = []

    #for enemigo_x, enemigo_y in enemigos:

    #    ex, ey = enemigo_x, enemigo_y
    for enemigo in enemigos:

        enemigo_x = enemigo["x"]
        enemigo_y = enemigo["y"]
        tipo = enemigo["tipo"]
        ex, ey = enemigo_x, enemigo_y
        distancia = abs(jugador_x - enemigo_x) + abs(jugador_y - enemigo_y)

        
        # enemigo loco 🤪
        if tipo == "loco":

            direccion = random.choice(["w", "a", "s", "d"])

            if direccion == "w":
                ey -= 1

            elif direccion == "s":
                ey += 1

            elif direccion == "a":
                ex -= 1

            elif direccion == "d":
                ex += 1

        # enemigos normales y rápidos 👹⚡
        

        
        else:

            if distancia <= 5:

                if jugador_x > enemigo_x:
                    ex += 1

                elif jugador_x < enemigo_x:
                    ex -= 1

                elif jugador_y > enemigo_y:
                    ey += 1

                elif jugador_y < enemigo_y:
                    ey -= 1

            else:

                direccion = random.choice(["w", "a", "s", "d"])

                if direccion == "w":
                    ey -= 1

                elif direccion == "s":
                    ey += 1

                elif direccion == "a":
                    ex -= 1

                elif direccion == "d":
                    ex += 1

        # evitar paredes
        
        nueva_posicion = [ex, ey]

        ocupado = False

        for otro in enemigos:

            if otro != enemigo:

                if ex == otro["x"] and ey == otro["y"]:
                    ocupado = True
            #nuevos_enemigos.append(nueva_posicion)
        
        #if mapa[ey][ex] != "#" and not ocupado:
        if mapa[ey][ex] not in ["#", "D"] and not ocupado:
            nuevos_enemigos.append({
                "id": enemigo["id"],
                "x": ex,
                "y": ey,
                "tipo": tipo
            })
        
        
        else:
            nuevos_enemigos.append({
                "id": enemigo["id"],
                "x": enemigo_x,
                "y": enemigo_y,
                "tipo": tipo
            }
                
            )
    enemigos = nuevos_enemigos

def verificar_choque():

    global jugador_x, jugador_y
    global enemigos
    global vidas

    #for enemigo_x, enemigo_y in enemigos:
    for enemigo in enemigos:

        enemigo_x = enemigo["x"]
        enemigo_y = enemigo["y"]
    
        if jugador_x == enemigo_x and jugador_y == enemigo_y:

            vidas -= 1

            if vidas <= 0:
                limpiar()
                print(ROJO + "💀 GAME OVER" + RESET)

                return True

            jugador_x, jugador_y = buscar_jugador(mapa)

                        
            enemigos = buscar_enemigos(mapa)
            #mapa, jugador_x, jugador_y, enemigos = cargar_nivel("salas/sala_prueba.txt")

            print(AMARILLO + "⚠️ El enemigo te atrapó" + RESET)
            input("Presiona Enter para continuar...")

    return False
    
def atacar():

    global enemigos, estado_salas, sala_actual

    for enemigo in enemigos:

        distancia = abs(jugador_x - enemigo["x"]) + abs(jugador_y - enemigo["y"])

        if distancia < 2:

            print("⚔️ Eliminaste al enemigo")
            
            if sala_actual not in estado_salas["enemigos"]:
                estado_salas["enemigos"][sala_actual] = []
                
            

            estado_salas["enemigos"][sala_actual].append(
                enemigo["id"]
            )
            

            enemigos.remove(enemigo)

            return

def verificar_victoria():
    if mapa[jugador_y][jugador_x] == "X":
        limpiar()
        print("🎉 GANASTE")
        
        return True
    return False
    
while True:
    limpiar()
    hud()
    dibujar()

    #movimiento = input("\nMover (w/a/s/d): ")
    movimiento = tecla()
    
    if movimiento == "q":
        break
    if movimiento == "v":
        atacar()
    
    mover_jugador(movimiento)

    mover_enemigos()
    

    # choque
    
    if verificar_choque():
        break
    # victoria
    if verificar_victoria():
        break
    
    