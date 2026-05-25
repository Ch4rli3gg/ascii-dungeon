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

mapa = [
    list("####################"),
    list("#     #            #"),
    list("# ### # ####### ## #"),
    list("# #           #    #"),
    list("# # ####### # #### #"),
    list("# #       # #      #"),
    list("# ####### # ###### #"),
    list("#         #      X #"),
    list("####################")
]

jugador_x, jugador_y = 1, 1
enemigo_x, enemigo_y = 9, 3


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def dibujar():

    radio_vision = 2

    for y in range(len(mapa)):
        pixel= ""
        for x in range(len(mapa[y])):
            
            # distancia entre jugador y celda
            distancia = abs(x - jugador_x) + abs(y - jugador_y)

            # niebla de guerra
            if distancia > radio_vision:
                pixel += NEGRO + "░" + RESET
                continue

            # jugador
            if x == jugador_x and y == jugador_y:
                pixel += AZUL + "@" + RESET

            # enemigo
            elif x == enemigo_x and y == enemigo_y:
                pixel += ROJO + "E" + RESET

            # paredes
            elif mapa[y][x] == "#":
                pixel += CYAN + "█" + RESET

            # salida
            elif mapa[y][x] == "X":
                pixel += VERDE + "X" + RESET

            # espacios vacíos
            else:
                pixel += " "

        print(pixel)
               
vidas = 3
nivel = 1

def hud():
    print(CYAN + "=== LABERINTO TERMINAL ===" + RESET)
    print(f"{'❤️ ' * vidas}   🗺️ Nivel: {nivel}")
    print("WASD para mover | Q para salir")
    print()    

def tecla():
        return msvcrt.getch().decode("utf-8").lower()
    
def mover_jugador(movimiento):

    global jugador_x, jugador_y

    
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

    if mapa[nueva_y][nueva_x] != "#":
        jugador_x, jugador_y = nueva_x, nueva_y

def mover_enemigo():

    global enemigo_x, enemigo_y

    ex, ey = enemigo_x, enemigo_y

    distancia = abs(jugador_x - enemigo_x) + abs(jugador_y - enemigo_y)

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

        direccion = random.choice(["w","a","s","d"])

        if direccion == "w":
            ey -= 1

        elif direccion == "s":
            ey += 1

        elif direccion == "a":
            ex -= 1

        elif direccion == "d":
            ex += 1

    if mapa[ey][ex] != "#":
        enemigo_x, enemigo_y = ex, ey

def verificar_choque():
    global enemigo_x, enemigo_y, jugador_x, jugador_y
    global vidas
    
    if jugador_x == enemigo_x and jugador_y == enemigo_y:

        vidas -= 1

        if vidas <= 0:
            limpiar()
            print(ROJO + "💀 GAME OVER" + RESET)
            
            return True

        # reiniciar posiciones
        jugador_x, jugador_y = 1, 1
        enemigo_x, enemigo_y = 9, 3

        print(AMARILLO + "⚠️ El enemigo te atrapó" + RESET)
        input("Presiona Enter para continuar...")
    
    return False
    
def verficar_victoria():
    if mapa[jugador_y][jugador_x] == "X":
        limpiar()
        print("🎉 GANASTE")
        
        return True
    return False
    
while True:
    limpiar()
    
    """print(CYAN + "=== LABERINTO TERMINAL ===" + RESET)
    print(f"{'❤️ ' * vidas}   🗺️ Nivel: {nivel}")
    print("WASD para mover | Q para salir")
    print()"""
    hud()
    dibujar()

    #movimiento = input("\nMover (w/a/s/d): ")
    movimiento = tecla()
    
    if movimiento == "q":
        break
    
    mover_jugador(movimiento)

    mover_enemigo()
    

    # choque
    """if jugador_x == enemigo_x and jugador_y == enemigo_y:

        vidas -= 1

        if vidas <= 0:
            limpiar()
            print(ROJO + "💀 GAME OVER" + RESET)
            break

        # reiniciar posiciones
        jugador_x, jugador_y = 1, 1
        enemigo_x, enemigo_y = 9, 3

        print(AMARILLO + "⚠️ El enemigo te atrapó" + RESET)
        input("Presiona Enter para continuar...")"""
    if verificar_choque():
        break
    # victoria
    if verficar_victoria():
        break
    """if mapa[jugador_y][jugador_x] == "X":
        limpiar()
        print("🎉 GANASTE")
        break"""
    