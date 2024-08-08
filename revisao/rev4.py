def conceito(ma):
    if ma < 40:
        return 'E'
    elif ma < 60:
        return 'D'
    elif ma < 75:
        return 'C'
    elif ma < 90:
        return 'B'
    else:
        return 'A'

def resultado(conceito):
    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        return 'APROVADO'
    else: 
        return 'REPROVADO'

try:
    matricula = input('Digite a matricula: ')
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    nota3 = float(input('Digite a nota 3: '))
    ME = float(input('Digite a média de exercícios: '))
    ma = (nota1 + nota2 * 2 + nota3 * 3 + ME) / 7 
    print('\n##################Resultados####################')
    print(f'Matrícula: {matricula}')
    print(f'Nota 1: {nota1} | Nota 2: {nota2} | Nota 3: {nota3} | ME: {ME}')
    print(f'Média de aproveitamento MA: {round(ma, 1)}')
    print(f'Conceito: {conceito(ma)}')
    print(f'Resultado: {resultado(conceito(ma))}')
except Exception as e:
    print(f'Ocorreu o seguite erro: {e}')