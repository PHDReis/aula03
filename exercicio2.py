# Imprima uma contagem regressiva com input de partida feito pelo usuario
# Utilize While e função


import time

def contagem(tempo):

    contador = tempo

    while contador >= 0:
        print (contador)
        time.sleep(1)
        contador = contador - 1


tempo = int(input("Digite o tempo: "))

contagem(tempo)

