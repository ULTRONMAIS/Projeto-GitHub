#para saber ser tem um nome específico dentro de um nome cmopleto usa a tag ('nome aléatorio' in nome.upper or slow()) para saber, lembrando de colocar o .strip() no ínicio da variavel para retirar os espaços.
nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in  nome.upper()))