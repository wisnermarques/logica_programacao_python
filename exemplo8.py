import random

maridos=['João','José','Paulo','Luiz','Claudio']
esposas=['Maria','Carla','Sueli','Fernanda','Renata']

random.seed()
x = random.randint(0,4)

n=int(input('Escolha seu sexo 1-Homem e 2-Mulher e pressione [ENTER]: '))
print('Número sorteado ', x)

if n==1:
    print ('Você vai casar com a ',esposas[x])
elif n==2:
    print ('Você vai casar com o ',maridos[x])
else:
    print ('você não vai casar')