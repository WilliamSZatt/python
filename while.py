# Exemplo 1: Usuário informar o número sorteado

numero_sorteado = 15

numero_escolhido = int(input('Informe um número entre 1 e 20: '))

while numero_escolhido != numero_sorteado:
  print('Você errou o número, tente novamente...')

  numero_escolhido = int(input('Informe um número entre 1 e 20: '))

print('Parábens! Você acertou!')

# Exemplo 2: Estrutura com contador

contador = 0

while contador < 5:
  print(contador)

  contador = contador + 1