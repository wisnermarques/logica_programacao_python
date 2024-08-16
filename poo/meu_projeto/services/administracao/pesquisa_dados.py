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