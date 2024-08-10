from services import cadastro, lista_produtos, pesquisa, reajuste_produto, venda_produto

produtos = []
while True:
    opcao = int(input('Escolha a opção desejada \n'
                    '[1- Para cadastrar produto'
                    '\n2- Para pesquisar produto'
                    '\n3- Para impressão da lista de produtos'
                    '\n4- Para venda do produto'
                    '\n5- Para reajuste]: '
                  ))
    if opcao == 1: 
        produtos.append(cadastro())
    elif opcao == 2:
        pesquisa(produtos)
    elif opcao == 3:
        lista_produtos(produtos)
    elif opcao == 4:
        venda_produto(produtos)
    elif opcao == 5:
        reajuste_produto(produtos)
    else:
        print('Opção inválida!')

    sair = input('Digite s para sair ou enter para continuar: ')
    if sair.upper() == 'S':
        break



