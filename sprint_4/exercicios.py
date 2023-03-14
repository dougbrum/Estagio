#Questao1
#Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
#Você deverá aplicar as seguintes funções no exercício:
#map
#filter
#sorted
#sum
#Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
#a lista dos 5 maiores números pares em ordem decrescente;
#a soma destes valores.
arquivo = open('number.txt', 'r')
numero = [x for x in arquivo]

def separador(f):
    return int(f.strip())

numeros =list(map(separador, numero))

numeros = list(filter(lambda x : x % 2 == 0, numeros))

def cinco_maiores(numeros):
    numeros_ordenados = sorted(numeros, reverse = True)
    return numeros_ordenados[:5]

print(cinco_maiores(numeros))
print(sum(cinco_maiores(numeros)))

#Questão2
#Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.
#É obrigatório aplicar as seguintes funções:
#len
#filter
#lambda
#Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.

texto = 'Ola mundo!'

def conta_vogais(texto:str)-> int:
    vogais = ['a', 'e', 'i', 'o', 'u']
    texto_selecionado = list(filter(lambda x : x in vogais, texto.lower()))
    return len(texto_selecionado)
print(conta_vogais(texto))

#Questão3
#A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 
#Abaixo apresentando uma possível entrada para a função.

#lancamentos = [
#    (200,'D'),
#    (300,'C'),
#    (100,'C')
#]

#A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. Na lista anterior, por exemplo, teríamos como resultado final 200.
#Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:
#reduce (módulo functools)
#map

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]
from functools import reduce

def calcula_saldo(lancamentos) -> float:
    return reduce(lambda x,y : x + y, list(map(lambda x: -x[0] if x[1] =='D' else x[0], lancamentos)), 0)
print(calcula_saldo(lancamentos))

#Questão4
#A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %), as quais devem ser aplicadas à lista de operadores nas respectivas posições. Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles.
#Veja o exemplo:
#Entrada
#operadores = ['+','-','*','/','+']
#operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]
#Aplicar as operações aos pares de operandos
#[ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ] 
#Obter o maior dos valores
#12
#Na resolução da atividade você deverá aplicar as seguintes funções:
#max

#zip

#map

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

def calcular_valor_maximo(operadores,operandos) -> float:
    operacoes = list(zip(operadores, operandos))
    resultados = list(map(lambda x : eval(f'{x[1][0]}{x[0]}{x[1][1]}') , operacoes))
    return max(resultados)

print(calcular_valor_maximo(operadores, operandos))

#Questão5
# Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.
#Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:
#Nome do estudante
#Três maiores notas, em ordem decrescente
#Média das três maiores notas, com duas casas decimais de precisão
#O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:
#Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>
#Exemplo:
#Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67
#Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33
#Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:
#round
#map
#sorted

arquivo = open('estudantes.csv', 'r')
estudante = [x for x in arquivo]

f = [x.strip() for x in estudante]

nomes = [x.split(',')[0] for x in f]
notas = [x.split(',')[1:] for x in f]


lista = []
tres_maiores_notas = []
for x in notas:
    for y in x:
        lista.append(int(y))

        
for x in range(0, 200, 5):
    tres_maiores_notas.append(sorted(lista[x: x+5], reverse = True))
    
[x.pop(4) for x in tres_maiores_notas]
[x.pop(3) for x in tres_maiores_notas]

nome_ordenado = sorted(nomes)
dicionario= dict(zip(nomes, tres_maiores_notas))
notas_ordenadas = [dicionario[nomes] for nomes in nome_ordenado]

def media_func(x):
    return round(sum(x)/len(x), 2)

medias = list(map(media_func, notas_ordenadas))

for i in range(40):
    print(f'Nome: {nome_ordenado[i]} Notas: {notas_ordenadas[i]} Média: {medias[i]}')
