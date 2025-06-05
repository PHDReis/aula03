# Crie uma função para imprimir um quadrado de asteristicos

tamanho = int(input("Informe o tamanho: "))

def parte_um(tamanho):

    for _ in range(tamanho):
        print("*" * tamanho)


def parte_dois(tamanho):

    meio = tamanho // 2
    for l in range(tamanho):
        linha = ""
        for c in range(tamanho):
            if l == meio and c == meio:
                linha += " "

            else:
                linha += "*"

        print(linha)


def parte_tres(tamanho):

    altura = tamanho // 2
    for i in range(altura+1):
        espacos = " " * (altura-i)
        asteristicos = "*" * (2*i+1)
        print(espacos + asteristicos + espacos)





#parte_um(tamanho)
#parte_dois(tamanho)
parte_tres(tamanho)