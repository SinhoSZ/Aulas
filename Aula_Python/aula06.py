# DEF = Para criar uma função

def big_mac():
    print("sandwich big mc")

print("inicio")
big_mac() # Chama a função
print("fim")

def fazer_big_mac(nome):
    print(f"sandwich big mc {nome}")

fazer_big_mac("Zoro")
fazer_big_mac("Nami")

def fazer_batata(tamanho):
    print(f"batata {tamanho}")

def prepara_refrigerante(tipo, tamanho):
    print(f'{tipo} {tamanho}')

fazer_big_mac("Luffy")
fazer_batata("grande")
prepara_refrigerante("coca", "média")

def fazer_combo_big_mac(nome, tamanho_batata, tipo_refri, tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    prepara_refrigerante(tipo_refri, tamanho_refri)

fazer_combo_big_mac("Luffy", "grande", "coca", "grande")

def soma_num(num1, num2):
    return num1 +num2

Resultado = soma_num(15, 5)
print(Resultado)

def maior_num(list_num):
    list_num.sort()         # Ordena do menor para o maior
    list_num.reverse()      # Ordena do maior para o menor
    maior_num = list_num[0] # Seleciona o primeiro indice
    return maior_num        # Retorna o que pede a função

resultado = maior_num([1, 4, 7, 2, 5, 8, 3, 6, 9])
print(resultado)