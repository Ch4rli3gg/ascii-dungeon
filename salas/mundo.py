conexiones = {

    "inicio": {

        (4,5): {
            "sala": "pasillo",
            "archivo": "salas/pasillo.txt",
            "spawn": (4,0)
        }

    },


    "pasillo": {

        (4,0): {
            "sala": "inicio",
            "archivo": "salas/sala_inicio.txt",
            "spawn": (4,5)
        },

        (4,5): {
            "sala": "enemigos",
            "archivo": "salas/sala_enemigos.txt",
            "spawn": (4,0)
        }

    },


    "enemigos": {

        (4,0): {
            "sala": "pasillo",
            "archivo": "salas/pasillo.txt",
            "spawn": (4,5)
        },

        (4,5): {
            "sala": "llave",
            "archivo": "salas/sala_llave.txt",
            "spawn": (4,0)
        }

    },


    "llave": {

        (4,0): {
            "sala": "enemigos",
            "archivo": "salas/sala_enemigos.txt",
            "spawn": (4,5)
        },

        (4,5): {
            "sala": "puerta",
            "archivo": "salas/sala_puerta.txt",
            "spawn": (4,0)
        }

    },


    "puerta": {

        (4,0): {
            "sala": "llave",
            "archivo": "salas/sala_llave.txt",
            "spawn": (4,5)
        }

    }

}