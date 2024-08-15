from utils.cadastro_pessoa import cadastro_pessoa
from services.administracao.cadastro import cadastro
from services.caixa.lista_produtos import lista_produtos
from services.caixa.pesquisa import pesquisa
from services.administracao.reajuste import reajuste_produto 
from services.caixa.vendas import venda_produto

produtos = []
clientes = []
funcionarios = []
while True:
    opcao = int(input('Escolha a opção desejada \n'
                    '1- Para cadastrar produto'
                    '\n2- Para pesquisar produto'
                    '\n3- Para impressão da lista de produtos'
                    '\n4- Para venda do produto'
                    '\n5- Para reajuste: '
                    '\n6- Para cadastro de cliente: '
                    '\n7- Para cadastro de funcionário: '
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
    elif opcao == 6:
        clientes.append(cadastro_pessoa(1))
    elif opcao == 7:
        funcionarios.append(cadastro_pessoa(2))
    else:
        print('Opção inválida!')

    sair = input('Digite s para sair ou enter para continuar: ')
    if sair.upper() == 'S':
        break




