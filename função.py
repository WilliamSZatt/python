# FUNÇÕES

# 1. O que são funções e pra que utilizá-las?

# Funções que já utilizamos anteriormente

''' 
print() - imprime uma mensagem (int, float, str) no console (terminal, cmd)

input() - Retorna um dado informado pelo usuário (entrada padrão)

len() - Recebe uma lista e retorna o tamanho dessa lista

max() - Retorna o maior valor de uma lista
'''

# 2. Criação de funções

# Função inicial

def saudacao():
  print('Seja Bem Vindo(a)!')

saudacao()
saudacao()
saudacao()

# Função com parâmetros

def saudacao(nome, curso):
  print(f'Seja Bem Vindo(a), {nome}!')
  print(f'Ola, é um prazer ter você fazendo parte do curso de {curso}')

saudacao('William', 'Python: Noções Basicas')
saudacao('Miguel', 'JavaScript')

# Função com parâmetros default

def saudacao(nome, curso='Python: Noções Basicas'):
  print(f'Seja Bem Vindo(a), {nome}!')
  print(f'Ola, é um prazer ter você fazendo parte do curso de {curso}') 

saudacao('William')

# Funções com retorno

# Exemplo 1

def soma(num1, num2):
  return num1 + num2

resultado = soma(5, 7)

print('O resultado da soma é: ', resultado)

# Exemplo 2 

def calculadora(num1, num2, operacao='+'):
  if operacao == '+':
    return num1 + num2
  elif operacao == '-':
    return num1 - num2
  elif operacao == '*':
    return num1 * num2
  elif operacao == '/':
    return num1 / num2
  
resultado = calculadora(20, 10, '-')

print(resultado)