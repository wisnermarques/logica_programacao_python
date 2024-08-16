def impressao_dados(dados, op):
    
    print(f'Nome: {dados.nome}')
    print(f'Sexo: {dados.sexo}')
    print(f'CPF: {dados.cpf}')
    print(f'Telefone: {dados.telefone}')
    print(f'Email: {dados.email}')
    if op == 1:
        print(f'Endereço: {dados.endereco}')
        if dados.ativo:
            print(f'Ativo')
        else:
            print(f'Inativo')
    elif op == 2:
        print(f'Matricula: {dados.matricula}')
        print(f'Função: {dados.funcao}')
        print(f'Salário: {dados.salario}')
    else:
        print('Opção inválida!')
    