# Crie uma funcao para imprimir a sequencia de Fibonacci com até N termos, definido pelo usuario



def fibonatti(termos):

    lista = []
    a, b = 0, 1

    while len(lista) < termos:
        lista.append(a)
        a, b = b, a+b

    print(lista)


termos=int(input("Digite a quantidade de termos: "))

fibonatti(termos)