class Aluno:
    def __init__(self, nome='', matricula='', notas=[]):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas 
        self.conceito = ''
        self.media = 0
        self.resultado = ''

    def conceito_aluno(self):
        if self.media < 4:
            return 'E'
        elif self.media < 6:
            return 'D'
        elif self.media < 7.5:
            return 'C'
        elif self.media < 9:
            return 'B'
        else:
            return 'A'

    def resultado_aluno(self):
        if self.conceito == 'A' or self.conceito == 'B' or self.conceito == 'C':
            return 'APROVADO'
        else:
            return 'REPROVADO'
        
def impressao(aluno):
    print(f'Matrícula: {aluno.matricula}')
    print(f'Aluno: {aluno.nome}')
    print(f'Notas: {aluno.notas}')
    print(f'Média: {round(aluno.media, 1)}')
    print(f'Conceito: {aluno.conceito}')
    print(f'Resultado: {aluno.resultado}')

alunos = []
while True:
    notas = []
    nome = input('Digite o nome: ')
    matricula = input('Digite a matricula: ')
    for i in range(3):
        nota = float(input(f'Digite a nota {i+1}: '))
        notas.append(nota)
    aluno = Aluno(nome, matricula, notas)
    aluno.media = sum(aluno.notas) / len(aluno.notas)
    aluno.conceito = aluno.conceito_aluno()
    aluno.resultado = aluno.resultado_aluno()
    alunos.append(aluno)

    sair = input('Digite s para sair ou enter para continuar: ')

    if sair.upper() == 'S':
        break

for aluno in alunos:
    impressao(aluno)
    print('')

print('  #######Busca do aluno########  ')
busca = input('Digite a matricula do aluno que seja ver os dados: ')

achei = ''
for aluno in alunos:
    if busca == aluno.matricula:
        achei = aluno
        break
if achei != '':
    impressao(achei)
else:
    print('Matrícula não encontrada.')