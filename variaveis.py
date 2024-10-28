# 1. Variáveis

idade = 26 # Criando uma variável (número)

print(idade) # Imprimindo uma variável

nome = 'William' # Criando uma variável (string)

print(nome) # Imprimindo uma variável

'''
  Tipos de variáveis:

  1. int: números inteiros ( 0, 5, -1, 1000 )

  2. float: números reais ( 1.0, -2.7, 3.14 )

  3. str: cadeias de caracteres, dados textuais (string)

  4. bool: valores lógicos (booleanos): True or False (Verdadeiro ou Falso)
'''

idade = 26 # tipo: int

altura = 1.77 # tipo: float

nome = 'William Serafin Zatt' # tipo: str

estudando = True # tipo: bool

# Para imprimir o TIPO da variável
print(type(idade))
print(type(altura))
print(type(nome))
print(type(estudando))

# Obtendo dados do usuário e salvando em variáveis

linguagem = input('Qual é a linguagem de programação que você está estudando? ')

print('A linguagem que você está estudando é', linguagem)