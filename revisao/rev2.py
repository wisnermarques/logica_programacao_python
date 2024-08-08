preco = float(input('Preço do produto: '))
print('1- À vista em dinheiro ou cheque')
print('2- À vista no cartão de crédito' )
print('3- Em duas vezes no cartão de crédito')
print('4- Em três vezes no cartão de crédito, juros de 10%')

condicao = int(input('Código Condição de pagamento: '))

if condicao == 1:
    total = preco - 10/100 * preco # preco * 0.9
    print(f'Total a pagar com 10% de desconto: {total}')
elif condicao == 2:
    total = preco - 15/100 * preco # preco * 0.85
    print(f'Total a pagar com 15% de desconto: {total}')
elif condicao == 3:
    total = round(preco / 2, 2)
    print(f'Total a pagar 2x de: {total}')
elif condicao == 4:
    total = preco + 10/100 * preco # preco * 0.9
    total = round(total / 3, 2) # total /= 3
    print(f'Total a pagar 3x de: {total}')
else:
    print('Opção de pagamento inválida.')
