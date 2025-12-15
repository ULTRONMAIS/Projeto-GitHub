#para confimar o nome dentro da str utilizando a variavel + [:5] < para contar as letras que serão digitado, usa o .sstrip() para tirar os espaço no começo da frase,  e colocar o upper() para colocar tudo em maisculo, dai pode colocar qualquer palavra que conversa para maisculo.
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:8].upper() == 'CURITIBA')