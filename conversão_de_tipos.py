# CONVERSÃO DE TIPOS

idade = '26'

print(idade, type(idade))

# CONVERSÃO
idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))

'''
  Conversões:
    1. int() = conversão para inteiros
    2. str() = conversão para string
    3. float() = conversão para decimal
    4. bool() = conversão para booleano
'''

# O tipo do input é sempre string, se não for convertido
altura = float( input('informe sua altura? '))

print(altura, type(altura))