#primeiro modo de fazer o import de random para ler uma lista e fazer o abaralhaento da mesma. o random.shuffle nao tem variavel.

'''import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentacão será {}.'.format(lista))'''

#O segundo modo de fazer o import e o from random import shuffle

from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentacão será {}.'.format(lista))