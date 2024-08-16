def pesquisa_cliente(clientes):
    print('####### Pesquisa de cliente ########')
    busca = input('Digite o cpf do cliente: ')
    achei = None
    for cliente in clientes:
        if busca == cliente.cpf:
            achei = cliente
            break
    if achei is not None:
        return achei
    else:
       return achei
    
def pesquisa_funcionario(funcionarios):
    print('####### Pesquisa de cliente ########')
    busca = input('Digite a matricula do funcionário: ')
    achei = None
    for func in funcionarios:
        if busca == func.matricula:
            achei = func
            break
    if achei is not None:
        return achei
    else:
       return achei