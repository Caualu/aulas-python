class Alunos:
    def cadastro (self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self,curso = curso
    def imprimir(self):
        return f"Nome: {self.nome}, idade:{self.idade} curso: {self.curso}"
    
#lista para armazenar os alunos 
cadastro_Alunos = []

#loop para coletar os dados de 10 alunos 
for i in range(3): 
    nome = input("digite o nome do aluno:")
    idade =int(input("digite a idade do aluno"))
    curso = input("digite o curso do aluno:")
    aluno = Aluno()
    aluno.cadastro(nome, idade, curso)
    cadastro_alunos.append(aluno)