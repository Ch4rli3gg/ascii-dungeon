conexiones = {

    "inicio": {

        (4,6): {
            "sala": "pasillo",
            "archivo": "salas/pasillo.txt",
            "spawn": (4,0)
        }

    },


    "pasillo": {

        (4,-1): {
            "sala": "inicio",
            "archivo": "salas/sala_inicio.txt",
            "spawn": (4,5)
        },

        (4,6): {
            "sala": "enemigos",
            "archivo": "salas/sala_enemigos.txt",
            "spawn": (4,0)
        }

    },


    "enemigos": {

        (4,-1): {
            "sala": "pasillo",
            "archivo": "salas/pasillo.txt",
            "spawn": (4,5)
        },

        (4,6): {
            "sala": "llave",
            "archivo": "salas/sala_llave.txt",
            "spawn": (4,0)
        }

    },


    "llave": {

        (4,-1): {
            "sala": "enemigos",
            "archivo": "salas/sala_enemigos.txt",
            "spawn": (4,5)
        },

        (4,6): {
            "sala": "puerta",
            "archivo": "salas/sala_puerta.txt",
            "spawn": (4,0)
        }

    },


    "puerta": {

        (4,-1): {
            "sala": "llave",
            "archivo": "salas/sala_llave.txt",
            "spawn": (4,5)
        }

    }

}

archivos_salas = {

    "inicio": "salas/sala_inicio.txt",
    "pasillo": "salas/pasillo.txt",
    "enemigos": "salas/sala_enemigos.txt",
    "llave": "salas/sala_llave.txt",
    "puerta": "salas/sala_puerta.txt"

}