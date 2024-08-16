from services.administracao.pesquisa_dados import pesquisa_cliente
from services.administracao.pesquisa_dados import pesquisa_funcionario
from utils.dados import impressao_dados
from utils.cadastro_pessoa import cadastro_pessoa
from services.administracao.cadastro import cadastro
from services.caixa.lista_produtos import lista_produtos
from services.caixa.pesquisa import pesquisa
from services.administracao.reajuste import reajuste_produto 
from services.caixa.vendas import venda_produto

def main():
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
                        '\n8- Para Pesquisa de cliente: '
                        '\n9- Para Pesquisa de funcionario: '
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
        elif opcao == 8:
            cliente = pesquisa_cliente(clientes)
            if cliente is not None:
                impressao_dados(cliente, 1)
            else:
                print('Cliente não cadastrado!')
        elif opcao == 9:
            funcionario = pesquisa_funcionario(funcionarios)
            impressao_dados(funcionarios, 2)
        else:
            print('Opção inválida!')

            sair = input('Digite s para sair ou enter para continuar: ')
            if sair.upper() == 'S':
                break

if __name__ == '__main__':
    main()

