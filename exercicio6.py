# Crie uma função para verificar palindromo e retorne verdadeiro ou falso


def palindromo(palavra):

    if palavra == palavra [::-1]:
        print("É um palindromo")
        return True

    else:
        print("Não é")
        return False


palavra = input("Digite a palavra: ")
palindromo(palavra)

print(palindromo(palavra))