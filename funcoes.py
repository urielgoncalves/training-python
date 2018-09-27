def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def funcao_sem_argumento():
    print("Oi")

print(somar(1,4))

print(multiplicar("a", 5))

print(funcao_sem_argumento())

def foo(primeiro, segundo, *outros):
        print(primeiro)
        print(segundo)
        print(list(outros))

def calcular(primeiro, segundo, **operacao):
    if operacao.get("operacao") == "somar":
        return primeiro + segundo

        