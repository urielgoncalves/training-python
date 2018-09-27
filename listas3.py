numeros = [1,2,3,4,5,6,7,8,9,10]
impares = []
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(numeros)
print(pares)
print(impares)

pares = [numero for numero in numeros if numero % 2 ==0]#list compreensions
impares = [numero for numero in numeros if numero % 2 !=0]#list compreensions
print(pares)
print(impares)

obj = {"a":"teste"}

print(obj)

nome = ["Uriel", "Rocha", "gonçalves"]
print(str(nome))

print(str(nome).strip("[]"))