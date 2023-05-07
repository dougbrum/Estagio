# Warm up 1
import random

lista = [random.randint(0, 1000) for _ in range(250)]

print("Lista original:", lista)

lista.reverse()

print("Lista invertida:", lista)

#Warm up 2

import csv

animais = ['gato', 'tigre', 'orca', 'gaviao', 'cabra', 'vaca', 'girafa', 'pato', 'leão', 'tubarao', 'golfinho', 'cobra', 'elefante', 'macaco', 'camelo', 'pinguim', 'baleia', 'arara', 'galinha', 'abelha']

animais_ordenados = sorted(animais)

print("Animais em ordem crescente:")
for animal in animais_ordenados:
    print(animal)

with open('animais.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for animal in animais_ordenados:
        writer.writerow([animal])

#Lab
# pip install names
import random
import time
import os
import names

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000


nomes_unicos = set()
while len(nomes_unicos) < qtd_nomes_unicos:
    nomes_unicos.add(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))


dados=[]
for i in range(0,qtd_nomes_aleatorios):
    dados.append(random.choice(list(nomes_unicos)))


with open('nomes_aleatorios.txt', 'w') as file:
    for nome in dados:
        file.write(nome+'\n')

# Verificar o conteúdo do arquivo
os.system('cat nomes_aleatorios.txt')