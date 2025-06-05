# Conte quantas vezes o usuario interagiu ate digitar a opcao de sair
# utilize funcao, while e crie um menu com 3 opcoes

def interacao():

    menu = ["1. Lista", "2. Produto", "3. Sair"]
    contador = 0

    while True:
        print(menu)
        opc = int(input("Escolha uma opção: "))
        
        if opc == 3:
            print (f"Tiveram {contador} interações")
            break

        else:
            contador += 1

interacao()
