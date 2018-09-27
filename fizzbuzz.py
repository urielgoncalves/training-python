import numpy

def fizzbuzz(numero):
    #se o numero for multiplo de 3 e 5 escreve fizzbuzz
    #se o numero dor multiplo de 3 escreve fizz
    #se o numero for multiplo de 5 escreve buzz
    #else escreve o numero
    #pass

    multiploDeTres = numero % 3 == 0
    multiploDeCinco = numero % 5 == 0

    if multiploDeTres and multiploDeCinco:
        print("fizzbuz")
    elif multiploDeTres:
        print("fizz")
    elif multiploDeCinco:
        print("buzz")
    else:
        print(numero)



numero = int(input("informe um número de 10 a 100: "))
fizzbuzz(numero)