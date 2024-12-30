# EXEMPLO 1
tenho_sede = True

if tenho_sede: # IF = SE
    print("beber água")

# EXEMPLO 2
esta_frio = True

if esta_frio: # se estiver
    print("vestir caçaco")
else: # se não estiver
    print("vestir a camisa")

#EXEMPLO 3
tenho_sede = True
tenho_fome = False
estou_em_dieta = True

if tenho_sede or tenho_fome:    # OU
    print("vou a cozinha")
else:
    print("vou ficar vend netflix")

if tenho_sede and tenho_fome:   # E
    print("vou a cozinha")
else:
    print("vou ficar vendo netflix")

if tenho_sede and tenho_fome:   # E, NÃO
    print("vou a cozinha")
elif tenho_sede and not (tenho_fome):
    if estou_em_dieta:
        print("beber água")
    else:
        print("vou tomar uma coca")
elif not (tenho_sede) and tenho_fome:
    print("fazer um sandwich")
else:
    print("ficar vendo netflix")

# COMPARAÇÃO

num1 = 5
num2 = 32

if num1 == num2:   
    print("num1 é igual ao num2")
elif num1 != num2:
    print("num1 é diferente ao num2")
elif num1 > num2:
    print("num1 é maior que  num2")
elif num1 < num2:
    print("num1 é menor que o num2")

# OPERADORES LÓGICOS

# OR = OU
# AND = E
# NOT = NÃO

# OPERADORES DE COMPARAÇÃO

# == IGUAL
# != DIFERENTE
# > MAIOR Q
# < MENOR Q
# >= MAIOR OU IGUAL Q
# <= MENOR OU IGUAL Q