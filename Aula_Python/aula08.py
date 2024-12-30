# CUIDADO  com o WHILE para não criar um loop infinito
# CTRL aborda um loop infinto

i = 1

# while i < 10:
#     print(i)      # Causará um loop infinito
#     i += 1        # Somará + 1 e terminará no 9

print("terminou")
print(i)

# FOR

crianças = ["mônica", "magali", "cebolinha"]

for item in crianças:
    print(item)     # para cada um ele colocou em uma lista

canal = "one piece"     # coloca as letra em vertical

for letra in canal:
    print(letra)

for index in range(7,20): # vai contar todos os números do 7 ao 15
    print(index)

# for index in range(0, a + 1, 2): # vai contar todos os números de 0 ao a, de 2 em 2
    print(index, end=" ")        # Imprime os números lado a lado com 3 espaços entre eles

for index in range(6, 20, 2): # Conta todos os números do 6 ao 19, de 2 em 2
    print(index)

for index in range(len(crianças)):  # Indica os indices
    print(crianças[index],index)    # Imprime o nome e o indice

for index in range(5):
    if index == 0:
        print("primeira linha")
    else:
        print(f"outras linhas {index}")

matrix_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0],
]

for linha in matrix_numeros:
    print(linha)
    for coluna in linha:
        print(coluna)