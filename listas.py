jogos = []

jogos.append("Dark Souls")
jogos.append("Dark Souls 2")
jogos.append("Dark Souls 3")

print(jogos)


for jogo in jogos:
    print(jogo)

if "Dark Souls" in jogos:
    print("\n Dark Souls está na lista de jogos")

if "Blood Born" not in jogos:
    print("\n Blood Born não está na lista de jogos")