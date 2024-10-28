# DICIONÁRIOS

# Criando dicionários

# Criando dicionários vazios

dicionario = {}
dicionario = dict()

# Criando dicionários com conteúdo

dicionario = { 'nome': 'William', 'idade': 19, 'altura': 1.95 }

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos em um dicionario

dicionario['Programdor'] = True

print(dicionario)

# Iterando sobre um dicionário

for chave in dicionario:
  print(chave, dicionario[chave])

# Testando a existencia de uma chave

print('peso' in dicionario)
print('altura' in dicionario)
