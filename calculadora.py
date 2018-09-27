'''def adicionar():
    print("chamou o método adicionar")

def multiplicar():
    print("chamou o método multiplicar")

#print(__name__)

if __name__ == "__main__":
    print(__name__)
    '''

def adicionar(primeiro_valor, segundo_valor):
    return primeiro_valor + segundo_valor

def multiplicar(primeiro_valor, segundo_valor):
    return primeiro_valor * segundo_valor

def subtrair(primeiro_valor, segundo_valor):
    return primeiro_valor - segundo_valor

def dividir(primeiro_valor, segundo_valor):
    if segundo_valor == 0:
        raise ValueError("Não é permitido fazer divisão por 0.")
    return primeiro_valor / segundo_valor