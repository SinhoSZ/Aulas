num1 = 5
num2 = 3.5

# TYPE Vai dizer que tipo de classe elas são
print(type(num1)) # num1 é INT 
print(type(num2)) # num2 é FLOAT

a = float(num1) # O resultado é transformado de INT para FLOAT
print(a)
print(type(a))

b = int(num2) # O resultado é tranformado em FLOAT para INT
print(b)
print(type(b))

print(num1 + num2)      # SOMA
print(num1 - num2)      # SUBTRAÇÃO
print(num1 * num2)      # MULTIPLICAÇÃO
print(num1 / num2)      # DIVISÃO COM RESULTADO DECIMAL SE TIVER
print(num1 // num2)     # DIVISÃO SEM NUMERO DECIMAL MESMO SE TIVER
print(num1 % num2)      # O RESULTADO QUE SOBROU NA DIVISÃO
print(num1 ** num2)     # EXPONECIAÇÃO

print(3 + 5 * 7 + 5)        # Estilo matemática básica, regra para resolver
print((3 + 5) * (7 + 3))    # Caso queria soma primeiro, é só colocar entre parentes

print(abs(-15))     # Número absoluto
print(pow(3, 3))    # Mesma coisa de exponeciação
print(max(1, 5))    # Retorna o número maior
print(min(1, 5))    # retorna o número menor
print(round(8.3))   # Arredonda para o mais próximo

import math

print(math.floor(8.3))  # Arredonda para baixo
print(math.ceil(8.3))   # Arredonda para cima
print(math.sqrt(81))    # Retorna a raiz quadrada do número