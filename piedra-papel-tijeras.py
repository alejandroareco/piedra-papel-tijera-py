nombre1 = input("Como se llamara el jugador 1? ")
nombre2 = input("Como se llamara el jugador 2? ")

jugador1 = input(f"Hola {nombre1}, Que eliges? piedra, papel o tijera?: ")
jugador2 = input(f"Hola {nombre2}, Que eliges? piedra, papel o tijera?: ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijera" and jugador2 == "papel"


if jugador1 == jugador2:
    print("Ha sido un empate")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado: ", nombre1)
else:
    print("Ha ganado: ", nombre2)