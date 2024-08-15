def impressao_dados(dado, op):
    print(f'Nome: {dado.nome}')
    print(f'Sexo: {dado.sexo}')
    print(f'CPF: {dado.cpf}')
    print(f'Telefone: {dado.telefone}')
    print(f'Email: {dado.email}')
    if op == 1:
        print(f'Endereço: {dado.endereco}')
        if dado.ativo:
            print(f'Ativo')
        else:
            print(f'Inativo')
    elif op == 2:
        print(f'Matricula: {dado.matricula}')
        print(f'Função: {dado.funcao}')
        print(f'Salário: {dado.salario}')
    else:
        print('Opção inválida!')
    