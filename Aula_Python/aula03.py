minha_string = 'qualquer texto'
print(type("minha_string"))
print(minha_string)

print(f"um livro falando de {minha_string}") # F chama a variavél 

print(minha_string.upper())                     # imprimi o texto todo maisculo
print(minha_string.lower())                     # imprimi o texto todo minusculo
print(minha_string.capitalize())                # imprimi a primeira letra maisculo
print(minha_string.isupper())                   # Diz se o texto está todo maisculo
print(minha_string.islower())                   # Diz se o texto está do minusculo
print(minha_string.strip())                     # Remove espaço na frente e atrás do texto
print(minha_string.replace("qualquer", "meu"))  # Substitui uma palavra, por outra
print(len(minha_string))                        # Conta quantas letras tem dentro da sua string
print(minha_string[7])                          # Diz qual letra está na posição na posição indicada
print(minha_string.index("qual"))               # Indica a posição da palavra ou parte da palavra

x = 'texto' in minha_string     # Diz se a palavra aparece no texto, verdadeiro ou falso
print(x)

minha_string = """ Linha 1,
Linha2,
Linha 3
"""
print(minha_string) # 3 apas o texto vai ser impresso em cada linha ou no exemplo abaixo
minha_string = "linha1, \n linha2, \n linha3"
print(minha_string)