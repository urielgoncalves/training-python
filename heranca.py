class MembroDaEscola:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print("Nome: {} Idade: {}".format(awlf.nome, self.idade), end=" :)")


#Professor herda de MembroDaEscola
class Professor(MembroDaEscola):
    def __init__(self, nome, idade, salario)
        MembroDaEscola.__init__(self, nome, idade)
        self.salario = salario

    def apresentar(self):
        MembroDaEscola.apresentar(self)
        print("Salário: %f" %self.salario)

class Aluno(MembroDaEscola):
    def __init__(self, nome, idade, materia_preferida)
        MembroDaEscola.__init__(self, nome, idade)
        self.materia_preferida = materia_preferida

    def apresentar(self):
        MembroDaEscola.apresentar(self)
        print("Matéria preferida: %f" %self.materia_preferida)

aluno = Aluno("Zezinho", 15, "aula vaga")
professor = Professor("Pardal", 60, 890)

membros_da_escola = [aluno, professor]

for membros_da_escola in membros_da_escola:
    membros_da_escola.apresentar()