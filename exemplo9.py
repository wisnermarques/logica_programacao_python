def mensagem(a):
    print(f'Seja bem vindo(a) {a}!!!')

def dobro(x):
    return 2*x

nome = input('Digite o seu nome: ')
mensagem(nome)

numero = int(input('Digite um número: '))
print(f'O dobro de {numero} é {dobro(numero)}')
