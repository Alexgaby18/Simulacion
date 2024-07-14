import random 

def juego():
    n_minimo = 1
    n_maximo = 6

    n_jugadas = 0
    apuesta = 5
    apuesta_acumulada = 0
    n_veces_ganadas = 0
    tirada = 0 
    gano= False

    while n_jugadas < 1000 and apuesta_acumulada > -100 and apuesta_acumulada < 500:
        tirada = random.randint(n_minimo, n_maximo)
        if apuesta_acumulada > 100: 
            apuesta = 10
        else:
            apuesta = 5
        #print (n_jugadas+1, "Numero del dado: ", tirada)
        if  tirada == 2 or tirada == 4 or tirada == 6:
            apuesta_acumulada += apuesta
            n_veces_ganadas += 1
            #print ("Ganancia: ", apuesta_acumulada)
        else:
            apuesta_acumulada -= apuesta
            #print ("Perdida: ", apuesta_acumulada)
        n_jugadas =+ 1
    #print ("Ganancias: ", apuesta_acumulada, " Veces ganadas: ", n_veces_ganadas)
    if (apuesta_acumulada >= 100):
        gano = True
        return gano
    else:
        return gano

def simular_partidas(cantidad):
    victorias = 0
    derrotas = 0
    for _ in range(cantidad):
        resultado = juego()
        if resultado == True:
            victorias += 1
        else:
            derrotas += 1
    return victorias, derrotas

victorias, derrotas = simular_partidas(1000)
print(f"Victorias: {victorias}, Derrotas: {derrotas}")
print ("Victorias porcentaje: ", (victorias/1000)*100,"%  Derrotas porcentaje: ", (derrotas/1000)*100, "%")