# LISTAS

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com Lista
notas = [7.9, 9.7, 8.2]

# Criando Listas 
lista = []
lista = list()
lista = [26, 'William', 3.1415, False]
lista_de_Listas = [10, [1, 2, 3]]


# Indexação e Slices (fatiamento)

# Indexação

lista = [10, 'William', 3.1415, True]

print(lista[0]) # = 10
print(lista[1]) # = 'William'
print(lista[2]) # = 3.1415
print(lista[3]) # = True
print(lista[-1]) # = True
print(lista[-2]) # = 3.1415
print(lista[-3]) # = 'William'

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

# começa pelo primeiro índice informado e para em uma casa antes do índice informado

print(lista[0:3]) # [10, 50, 30]
print(lista[3:6]) # [40, 25, 60]
print(lista[3:]) # [40, 25, 60, 5]
print(lista[2:6:2]) # [30, 25]

# Iterações com FOR 

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
  print(elemento)

# 2. Utilizando os índices

## len() = Utiliza-se para informar o tamanho/quantidade de elementos na lista 
print('Comprimento da lista:', len(lista))

for i in range(len(lista)):
  # print(i)
  print(lista[i])

# MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]

# append = o elemento sempre é adicionado ao final

print('Antes do append:', lista)

lista.append(3)

print('Depois do append:', lista)

# insert = Você escolhe a posição onde o elemento adicionado será inserido

print('Antes do insert:', lista)

# O primeiro paramêtro é o índice, e o segundo paramêtro é o número que será adicionado
lista.insert(2, 10)

print('Depois do insert:', lista)

# extend = Serve para juntar duas listas

lista2 = [5, 2, 3]

print('Antes do extend:', lista)

lista.extend(lista2)

print('Depois do extend:', lista)

# pop = elimina o ÍNDICE adicionado aos parênteses (), se os () estiverem vazios, elimina o último índice da lista

lista.pop(0)

print('Lista após o pop:', lista)

# remove = procura em toda lista até achar o NÚMERO adicionado aos parênteses () e remove APENAS o primeiro encontrado

lista.remove(3)

print('Lista após o remove:', lista)

# count = mostra a quantidade do número digitado na lista

print('Quantidade do número 2 na lista:', lista.count(2))

# index = mostra o índice do elemento solicitado

print('Indice do elemento 12:', lista.index(12))

# sort = serve para ordenar a lista

lista.sort()

print(lista)

# FUNÇÕES PARA LISTAS

# len = para saber quantos elementos tem na lista

print('O total de elementos na lista são:', len(lista))

# sum = soma todos elementos da lista

print('A soma da lista é:', sum(lista))

# max = retorna o maior elmento da lista

print('Qual é o maior elemento da lista:', max(lista))

# min = retorna o menor elmento da lista

print('Qual é o menor elemento da lista:', min(lista))