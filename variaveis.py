nome = "Uriel"
idade = 33
altura = 1.81
joga_dark_souls = False
joga_bloodborne, joga_fifa = True, False
a = b = True

print("Nome: "+ nome)
print("Idade: %d" %idade)#quebra de linha
print("Seu nome é %s, sua idade é %d e sua altura é %.2f" % (nome, idade, altura)) #%.2f limita as casas decimais em 2

print(nome[0])

print("b" in "abc")#existe b na string

print(len(nome))

print(nome.upper())

print(nome.lower())

print("Teste    ".strip())#remove espaços