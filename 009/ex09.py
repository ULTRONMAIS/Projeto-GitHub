# frase.count() para contar
#frase.find('') para encontrar frase especifica
#frase.find('') colocar algo que não temna str aparece o menos1, dizendo que nao tem na str
#'curso' in frase retorna true or false se tiver na str
#para trocar usa frase.replace('frase', por 'frase')
#fra.upper() para colocar a frase que você quer em maiusculo
#frase.lower() para trocar de maiusculo para menusculo
#frase.capilaliza() joga todos para manusculo e converte so a promeira letra de cada palavra mausculo
#frase.title() contar quantas palavras tem
#transformação
#frase.strip() para remover os espaços inúteis do início e do fim da frase
#frase.rstrip() para o lado direito é removido o espaço
#frase.lstrip() para remover o espaço da esquerda
#divisão
#frase.split() dividir entres os espaços ficando dentro de uma contagem  12345 12345 12345
#junção
#'-'.join(frase) para juntas todas as frase para colocar os espaços entre elas

#Exemplos:
# pode combinar também as frase com o ponto.
#print(frase.upper().count('O'))
#frase = 'Curso em Vídeo Python'
#print(frase.upper().count('O'))
#para colocar o testo todo entre as "" so colocar """ no início e """ no fim.
'''print("""lorem ljfldjlkfljalçdfjaçkldjfçlkajdçlkfj
asdfjçlajdfklajdçlfjaçlkdjfçlkajdçlkfjlaskjdlçfk
alkskdjfçlkjaçsdlfjaçldksjfçklajdçlfjçalkdjf""")'''

#usa-se o len(frase) para contar e len(frase.strip()))
'''frase = 'Curso em Vídeo Python'
print(len(frase))'''

#usando o replace para trocar a frase
'''frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Java'))'''

# usando a tranformação
'''frase = 'Curso em Vídeo Python'
frase = frase.replace('Python', 'Java')
print(frase)'''

#para saber se tem a frase na str usando o in.
'''frase = 'Curso em Vídeo Python'
print('Curso' in frase)'''

# saber a posição da frase na str usand o frase.find()
'''frase = 'Curso em Vídeo Python'
print(frase.split())'''

# Usando a tag split ele cria a lista da str separando
'''frase = 'Curso em Vídeo Python'
print(frase.split())'''

#