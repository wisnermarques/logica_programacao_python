from models.cliente import Cliente
from models.funcionario import Funcionario

def cadastro_pessoa(op):
    nome = input('Digite o nome: ')
    sexo = input('Digite o sexo: ')
    cpf = input('Digite o cpf: ')
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    
    if op == 1:
        endereco = input('Digite o endereço: ')
        cliente = Cliente(nome, sexo, cpf, telefone, email)
        cliente.endereco = endereco
        return cliente
    elif op == 2:
        matricula = input('Digite a matricula: ')
        funcao = input('Digite a função: ')
        salario = float(input('Digite o salário: '))
        funcionario = Funcionario(nome, sexo, cpf, telefone, email, matricula, funcao, salario)
        return funcionario
    else:
        return None