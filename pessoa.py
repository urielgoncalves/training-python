class Pessoa:
    #todo método em python precisa receber a classe como parâmetro(self). Os parâmetro vem na sequencia
    #o construtor não leva o nome da classe como no C#
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def dizer_oi(self):
        print("Olá meu nome é %s e tenho %d anos" % (self.nome, self.idade))

    def dizer_tchau(self):
        print("tchau")

pessoa = Pessoa("Uriel", 33)
pessoa.dizer_oi()
pessoa.dizer_tchau()