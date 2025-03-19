class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getEndereco(self):
        return self.endereco

pessoa = Pessoa('João', 19, 'Rua 1')

print(pessoa.getNome())
print(pessoa.getIdade())
print(pessoa.getEndereco())

class Funcionario(Pessoa):
    def __init__(self, nome, idade, endereco, salario):
        super().__init__(nome, idade, endereco)
        self.salario = salario
    
    def getsalario(self):
        return self.salario


funcionario = Funcionario('João', 19, 'Rua 1', 1000)

print(funcionario.getNome())     
print(funcionario.getIdade())     
print(funcionario.getEndereco())  
print(funcionario.getsalario())   