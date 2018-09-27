numeros = [1,2,3,4,5]

for numero in numeros:
    print(numero)

for s in range(10):
    print(s)

for s in range(10, 20):
    print(s)

for i in range (1,10):
#    if i % 5 ==0:
 #       break
    print(i)
else:
    print("acabou o for")#não executa com o break

total = 0
while total < 5:
    print (total)
    total +=1
else:
    print("Variável total está com o valor %d", total)