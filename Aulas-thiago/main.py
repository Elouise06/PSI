# 01 - Crie duas variaveis em que A = 10 e B = 20,
# em seguida faça A = B e B = A
# de modo a obter os resultados finais A = 20 e B = 10.

# usuario_1 = "josé Caetano da Silva"
# usuario_2 = "Maria Souza Lemos"

# print("usuario 1: ", usuario_1)
# print("usuario 2: ", usuario_2)

#troca_usuario = usuario_1
#usuario_1 = usuario_2
#usuario_2 = troca_usuario

#print(usuario_1)
#print(usuario_2)


# 03 - Crie uma função que recebe um valor e retorna a 
# informação dizendo se é um valor positivo, negativo ou nulo.

#ef avalia_valor(numero):
#  if type(numero) == int:
#       if numero > 0:
#           return 'O número é positivo'
#       elif numero < 0:
#           return 'O número é negativo'
#       elif numero == 0:
#           return 'O número é nulo'
#   else:
#       return 'Valor inválido'
    
#rint(avalia_valor("lolo"))


#O custo de um carro novo ao consumidor é a soma do custo de
#fábrica com a porcetagem do distribuidor e dos impostos
#(aplicados ao custo de fábrica). Supondo que o percentual do
#distribuidor seja de 28% e os impostos de 45%, escrever um
#algoritmo para ler o custo de fábrica de um carro,
#calcular e escrever o custo final ao consumior.

# def calular_custo(custo_fabrica):
#   imposto_distribuidor = custo_fabrica*0.28
#   imposto_geral = custo_fabrica*0.45
#  custo_total = custo_fabrica + imposto_distribuidor + imposto_geral
#   return custo_total

#print(calcular_custo((10000))


# Crie uma função que ler 3 valores (A, B e C)
# representando as medidas do lados de um triangulo
# e escrever se formam ou não um triangulo.
# OBS: para formar um triangulo, o valor de cada lado deve ser menor
# que a soma dos outros 2 lados.

import math
A = 4; B = 5; C = 5
#Isoceles = 2
#Equilatero = 3
#Escaleno = Todos diferentes
def verificar_triangulo(A, B, C):
    if A < B + C and B < A + C and C < A + B:
        print("Formam um triângulo.")
        if A == B and B == C:
            print("É um triângulo Equilatero")
            area = (math.sqrt(3)*pow(A,2))/4
            print(f"A área do triangulo é: {area:.2f}")
        elif A == B or B == C or A == C:
            print("É um triangulo Isoceles")
            if A == B:
                base = C
                lado = A
            elif B == C:
                base = A
                lado = B
            else:
                base = B
                lado = A

            h = math.sqrt(lado**2 - (base / 2)**2)
            area = (base * h) / 2
            print(f"Área = {area:.2f}")

        else:
            print("É um triângulo Escaleno")
            s = (A + B + C) / 2
            area = math.sqrt(s * (s - A) * (s - B) * (s - C))
            print(f"Área = {area:.2f}")

    else:
        print("Não formam um triângulo.")

verificar_triangulo(A, B, C)