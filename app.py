# write 'hello world' to the console
print('hello world')
import random

def juego_piedra_papel_tijera(jugador, computadora):
    if jugador == computadora:
        return "¡Es un empate!"
    elif (jugador == 'piedra' and computadora == 'tijera') or \
         (jugador == 'tijera' and computadora == 'papel') or \
         (jugador == 'papel' and computadora == 'piedra'):
        return "¡Ganaste! La {} derrota a la {}.".format(jugador, computadora)
    else:
        return "Perdiste. La {} derrota a la {}.".format(computadora, jugador)

# Opciones válidas para el jugador
opciones = ['piedra', 'papel', 'tijera']

# El jugador elige
jugador_elige = input("Elige piedra, papel o tijera: ").lower()

# Validar la elección del jugador
if jugador_elige not in opciones:
    print("Elección no válida. Por favor, elige entre piedra, papel o tijera.")
else:
    # La computadora elige aleatoriamente
    computadora_elige = random.choice(opciones)

    # Mostrar elecciones
    print("Tu elección: {}".format(jugador_elige))
    print("Elección de la computadora: {}".format(computadora_elige))

    # Determinar el resultado
    resultado = juego_piedra_papel_tijera(jugador_elige, computadora_elige)
    print(resultado)
