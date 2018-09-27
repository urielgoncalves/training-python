lista = []

dicionario = {}
dicionario["chave1"] = "valor 1"
dicionario["chave2"] = "valor 2"
print(dicionario)

telefones = {
    "Pessoa A" : 123456,
    "Pessoa B" : 654321
}

print(telefones)

for nome, telefone in telefones.items():
    print("Nome: %s - Telefone: %d" %(nome, telefone))

del telefones["Pessoa A"]
print(telefones)

telefones.pop("Pessoa B")
print(telefones)