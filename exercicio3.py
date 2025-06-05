# Some os valores do intervalo definido pelo usuario
# Utilize a funcao e range

inicial = int(input("Digite o valor inicial: "))
final = int(input("Digite o valor final: "))

def soma(inicial, final):

    print(sum(range(inicial, final+1)))

soma(inicial, final)

