def buscar_enemigos(mapa):
    
    enemigos=[]
    
    contador_id = 0
    
    for y in range(len(mapa)):
        
        for x in range(len(mapa[y])):
            
            if mapa[y][x] == "E":
                
                enemigos.append({
                    "id": contador_id,
                    "x": x,
                    "y": y,
                    "tipo": "normal"
                })
                
                contador_id += 1
            elif mapa[y][x] == "C":
                
                enemigos.append({
                    "id": contador_id,
                    "x": x,
                    "y": y,
                    "tipo": "loco"
                })
                
                contador_id += 1
                
    return enemigos
                
            
    
    

    