# Imprimir os números a partir de um input do usuario
# até um limite definido, também pelo usuario
# utilize funcao definindo parametros


inicial = int(input("Informe o valor inicial: "))
final = int(input("Informe o valor final: "))

def imprimir (inicial, final):
    for numeros in range (inicial,final+1):
        print(f"{numeros}")

imprimir(inicial,final)