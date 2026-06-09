def buscar_enemigos(mapa):
    
    enemigos=[]
    
    for y in range(len(mapa)):
        
        for x in range(len(mapa[y])):
            
            if mapa[y][x] == "E":
                
                enemigos.append({
                    "x": x,
                    "y": y,
                    "tipo": "normal"
                })
                
            elif mapa[y][x] == "C":
                enemigos.append({
                    "x": x,
                    "y": y,
                    "tipo": "loco"
                })
    return enemigos
                
            
    
    

    