# Utilizando o metodo random.choice para escolher um iten aleátorio na lista
#Fzendo lista com colchetes sempre depois da lista feita.

'''import random

l = str(input('Primeiro aluno: '))
l1 = str(input('Segundo aluno: '))
l2 = str(input('Terceiro aluno: '))
list = [l, l1, l2]
ale = random.choice(list)
print('O aluno esolhido foi {}'.format(ale))'''

# utilizando o segundo método de funciona para todos os imports separadamente. from random import choice

from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))