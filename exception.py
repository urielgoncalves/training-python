def dividir(primeiro_valor, segundo_valor):
    if segundo_valor == 0:
        raise ValueError("Não é permitido fazer divisão por 0.")
    return primeiro_valor / segundo_valor

try:
    dividir(10,0)
except ZeroDivisionError as erro:
    print("Tentativa de divisão por zero: {}".format(erro))
except Exception as erro:
    print("Exception genérica: {}".format(erro))