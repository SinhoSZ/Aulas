# COLEÇÃO DE DADOS, LISTAS DE DADOS

familia = ['cebolinha', 'cascão', "magali", "monica", "franginha"]
        #       0           1          2        3           4
        #       -5          -4          -3      -2          -1

print(familia)      # Imprime tudo
print(familia[0])   # Imprime o primeiro indice
print(familia[-3])  # Imprime o terceiro de trás para frente
print(familia[2:])  # Imprime do indice 2 para frente
print(familia[2:4]) # Impreme o segundo e o terceiro e exclui o quarto

familia[2] = "maga" # trocou magali por maga
print(familia)

familia.extend(["dudu", "chico"]) # adicionou mais 2 na lista
print(familia)

familia.append("monicão")   # adiciounou apenas 1
print(familia)

familia.insert(1, "floquinho") # adiciona no indice indicado
print(familia)

familia.pop()               # Remove o último indice
familia.remove("floquinho") # Remove o indice indicado
print(familia)

print(familia.count("cebolinha"))   # indica qunatos cebolinha tem no texto

familia.clear()     # Limpa toda a lista

idade_familia = [27,12,11,40,60,28,24] # imprime na ordem que está digitado
print(idade_familia)
idade_familia.sort()    # imprime do menor para o maior ou por ordem alfabetica
print(idade_familia)
idade_familia.reverse() # imprime do maior para o menor ou por ordem alfabeica Z -A
print(idade_familia)

familia2  = familia # familia 2 é igual a familia 1
print(familia2)
familia.remove("cebolinha")
print(familia)

coordenadas = (-10, -20) # lista é com [] e pode ser mudadas, já o () o valor é imutavel
coordenadas


def remover_prefixo_des(palavra):
    if palavra.startswith("des"): # Retorna TRUE se a string "palavra" começar com "des" e FALSE  caso contrário
        return palavra.replace("des", "", 1)
    # substitui a primeira ocorrência de "des" na string "palavra" por uma string vazia, removend assim o prefixo "des"
    else:
        return palavra