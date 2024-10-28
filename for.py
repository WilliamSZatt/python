# range(): significa faixa, ou seja, dentro de uma faixa de 10, range(10)

# for variavel in range(10):
#   print(variavel)

# Quando tiver 2 parâmetros no range(), ele começa do primeiro parâmetro e para uma casa antes do segundo parâmetro, ou seja, range(1, 10) = começa no 1, e para no 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for variavel in range(1, 10):
#   print(variavel)

# Quando tiver 3 parâmetros no range(), ele começa do primeiro parâmetro, para uma casa antes do segundo parâmetro, e no terceiro parâmetro seria quantas casas você gostaria de pular, ou seja, range(1, 12, 3) = começa no 1, para no 11, de 3 em 3 casas, [1, 4, 7, 10]

# for variavel in range(1, 12, 3):
#   print(variavel)

soma = 0

for i in range(1, 4):

  # O f no começo da string deixa com que você possa colocar uma variável dentro da string por meio de chaves {}

  nota = float(input(f'Informe a sua nota {i}: '))

  soma = soma + nota
  media = soma + nota

print(soma + 3)
print(media / 3)