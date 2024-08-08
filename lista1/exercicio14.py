'''
ax2 + bx + c

delta = b2 - 4ac

raiz1 = (-b + raizquadrada(delta)) / 2a

raiz2 = (-b - raizquadrada(delta)) / 2a
'''

a = int(input('Digita o valor de a: '))
b = int(input('Digita o valor de b: '))
c = int(input('Digita o valor de c: '))

delta = b*b - 4*a*c # b**2

if delta < 0:
    print(f'Delta: {delta} - Não há raízes')
elif delta == 0:
    print(f'Delta: {delta} - Não é equação do segundo grau')
else:
    raiz1 = (-b + (delta**0.5)) / 2*a

    raiz2 = (-b - (delta**0.5)) / 2*a

    print(f'Delta: {delta} - raiz 1: {raiz1}, raiz 2: {raiz2}')


