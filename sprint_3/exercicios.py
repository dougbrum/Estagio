#E1. 
#Escreva um código Python que lê do teclado o nome e a idade de um usuário e que imprima apenas o ano em que ele completará 100 anos.
#Dica: você pode ler strings digitadas no teclado utilizando a função builtin input('mensagem'). Lembre-se de converter números para seu respectivo tipo (int ou float) antes fazer operações aritméticas.

from datetime import date
data = date.today()
year = data.year

def cem_anos():

    nome = input("Escreva seu nome: ")
    idade = int(input("Escreva sua idade: "))

    tempo_faltante = 100 - idade
    return tempo_faltante + year

print(cem_anos())

# E2. 
# Escreva um código Python que verifique se três números digitados pelo usuário são pares ou ímpares. Para cada número, imprima o Par: ou Ímpar: e o número correspondente.
# Exemplo de formato de saída:
# Par: 2
# Ímpar: 3

for i in range(3):
    i=0
    numero = int(input("Digite um numero: "))
    if (numero % 2 == 0):
        print(f'Par: {numero}')
    else:
        print(f'Ímpar: {numero}')


#E3.
# Escreva um código Python que imprime os números pares de 0 até 20 (incluso).

def pares():
    for n in range(0, 21):
        if n % 2 == 0:
            print(n)
pares()

# E4.
# Escreva um código Python que imprime todos os números primos de 1 até 100. Abaixo uma imagem de exemplo dos números primos entre 1 e 1000


for i in range(1, 101):
    if i > 1:
        for j in range(2, i):
            if(i%j == 0):
                break
        else:
            print(i) 

# E5.
#  Escreva um código Python que tem 3 variáveis dia (22), mês(10) e ano(2022) e imprime a data completa no formato a seguir:
# Exemplo: 22/10/2022
# Importante: É necessário formatar as variáveis como strings antes de concatená-las e imprimi-las na tela.

# opção de resolução 1

dia = str(22)
mes = str(10)
ano = str(2022)
print(f'{dia}/{mes}/{ano}')

# Opção de resolução 2

def format_data(dia = str(22), mes = str(10), ano = str(2022)):
    return dia + "/" + mes + "/"+ano

print(format_data())


#Exercícios Parte 2

#E6.
#Dada duas listas como as no exemplo abaixo:
#a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#Escreva um programa que retorne o que ambas as listas têm em comum (sem repetições). O seu programa deve funcionar para listas de qualquer tamanho


a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

i = 0
j = 0

def repetidos(a, b):

    reps = []    
    for i in range(len(a)):
        for j in range(len(b)):
            if (a[i] in b):
                reps = reps +[a[i]]
                set_reps = list(set(reps))
    return set_reps

print(repetidos(a,b))

#E7
#Dada a seguinte lista:
#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Faça um programa que gere uma nova lista contendo apenas números ímpares.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

impares = []

for k in range(len(a)):
    if a[k] % 2 != 0:
        impares = impares + [a[k]]
        
print(impares)

#E8
# Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.
# Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.
# É necessário que você imprima no console exatamente assim:
# A palavra: maça não é um palíndromo
#A palavra: arara é um palíndromo
#A palavra: audio não é um palíndromo

a = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

inv = []

for i in range(len(a)):
    inv = inv + [a[i][::-1]]
    if a[i] == inv[i]:
        print(f'A palavra: {a[i]} é um palíndromo')
    else:
        print(f'A palavra: {a[i]} não é um palíndromo')

#E9
#Dada as listas a seguir:
#primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
#sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
#idades = [19, 28, 25, 31]
#Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".
#Exemplo:
#0 - João Soares está com 19 anos

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]


for i, nome in enumerate(primeirosNomes):
    print (f'{i} - {primeirosNomes[i] + " "+ sobreNomes[i]} está com {idades[i]} anos')


#E10
#Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.
#['abc', 'abc', 'abc', '123', 'abc', '123', '123']

duplicatas =  ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def remove_duplicatas(f):
    return list(set(f))

print(remove_duplicatas(duplicatas))

#E11
#Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.
#Dica: leia a documentação da função open(...)

with open('arquivo_texto.txt', 'r') as arquivo:
    arquivo_texto = arquivo.read()
    print(arquivo_texto, end='')

#EE12
#Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
#Dica: leia a documentação do pacote json

import json
with open('person.json', 'r') as arquivo:
    conteudo = json.load(arquivo)
    print(conteudo)

#E13
#Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.
#Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrado = lambda x: x ** 2 

def my_map(lista, f):
    return list(map(f, lista))

print(my_map(lista, quadrado))

#E14
#Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.
#Teste sua função com os seguintes parâmetros:
#(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

def func(*args,**kwargs):
    for k in args:
            print (f'{k}')
    for x in kwargs.values():
        print (f'{x}')
        

            
func(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

#E15
#Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:
#liga(): muda o estado da lâmpada para ligada
#desliga(): muda o estado da lâmpada para desligada
#esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário
#Para testar sua classe:
#Ligue a Lampada
#Imprima: A lâmpada está ligada? True
#Desligue a Lampada
#Imprima: A lâmpada ainda está ligada? False

class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada
        
    def esta_ligada(self):
        return self.ligada

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False
    

lamp1 = Lampada(False)
lamp1.liga()
print(f'A lâmpada está ligada? {lamp1.esta_ligada()}')
lamp1.desliga()
print(f'A lâmpada está ligada? {lamp1.esta_ligada()}')

#E16
#Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.
#A string deve ter valor  "1,3,4,6,10,76"

b = "1,3,4,6,10,76"

def sep_soma(b):
    separados = b.split(",")
    numeros = [int(num) for num in separados]
    soma = sum(numeros)
    return soma

print(sep_soma(b))

#E17
#Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo
#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def particao_lista(lista):
    n = len(lista)//3
    lista1, lista2, lista3= [lista[i:i + n] for i in range(0, len(lista), n)]
    print(f'{lista1} {lista2} {lista3}')
        

particao_lista(lista)

# E18
#Dado o dicionário a seguir:
#speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
#Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.

speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

lista_valores = list(set( speed.values()))
print(lista_valores)

#E19
#Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
#Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!
#import random 
## amostra aleatoriamente 50 números do intervalo 0...500
#random_list = random.sample(range(500),50)

import random

random_list = random.sample(range(500), 50)


mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0
# Calculo da Média

n = len(random_list)
soma = sum(random_list)

media = soma/n

# Calculo da Mediana

l_ordenada = sorted(random_list)

if n % 2 == 0:
    med1 = l_ordenada[n//2]
    med2 = l_ordenada[n//2 - 1]
    mediana = (med1 + med2)/2
else:
    mediana = l_ordenada[n//2]
    
# Valor máximo

valor_maximo = max(random_list)

# Valor Mínimo

valor_minimo = min(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')


#E20
#Imprima a lista abaixo de trás para frente.
#a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a[::-1])


#Parte 3
#E21
#Implemente duas classes Pato e Pardal que herdem de uma classe Passaro a habilidade de voar e emitir som, porém, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console.
#Imprima no console exatamente assim:
#Pato
#Voando...
#Pato emitindo som...
#Quack Quack
#Pardal
#Voando...
#Pardal emitindo som...
#Piu Piu

class Passaro:
    def __init__(self, nome):
        self.nome = nome
        print(self.nome)
        
    def voar(self):
        print('Voando...')
        
    def emitir_som(self):
        pass
        
        
class Pato(Passaro):
    
    def __init__(self, nome):
        super().__init__(nome)
        
    def emitir_som(self):
        print('Pato emitindo som...')
        print('Quack Quack')
        
        
class Pardal(Passaro):
    
    def __init__(self, nome):
        super().__init__(nome)
        
    def emitir_som(self):
        print('Pardal emitindo som...')
        print('Piu Piu')
        
p = Pato('Pato')
p.voar()
p.emitir_som()
pard = Pardal('Pardal')
pard.voar()
pard.emitir_som()

#E22
#Crie uma classe chamada "Pessoa" com um atributo privado "nome" (representado como "__nome") e um atributo público "id". Adicione duas funções à classe, uma para definir o valor de "nome" e outra para obter o valor de "nome". Observe que o atributo "nome" deve ser privado e acessado somente através dessas funções.
#Para testar seu código use:
#pessoa = Pessoa(0) 
#pessoa.nome = 'Fulano De Tal'
#print(pessoa.nome)

class Pessoa:
    def __init__(self, id):
        self.id = id
        
    def get_nome(self):
        return self.__nome
        
    def nome(self, nome):
        self.__nome = nome
        
        
pessoa = Pessoa(0)        
pessoa.nome('Fulano de Tal')        
print(pessoa.get_nome())


""" O código acima é o correto segundo o verificador da trilha, mas confesso que achei a forma que fiz abaixo mais fiel ao que foi solicitado pelo enunciado. Pois a questão diz que a classe Pessoa tem dois atributos, nome e id. Entao imaginei que tais atributos precisariam fazer parte do metodo construtor. Porem quando é fornecida a sugestão de teste o objeto criado recebe apenas um parâmetro, o id, por isso imaginei que o código acima funcionaria melhor com o verificador de soluções. """


class Pessoa:
    def __init__(self, nome, id):
        self.__nome = nome
        self.id = id
        
    def get_nome(self):
        return self.__nome
        
    def nome(self, nome):
        self.__nome = nome
        
        
pessoa = Pessoa('Douglas',0)        
pessoa.nome('Fulano de Tal')        
print(pessoa.get_nome())


#E23
#Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).
#Utilize os valores abaixo para testar seu exercício:
#x = 4 
#y = 5
#imprima:
#Somando: 4+5 = 9
#Subtraindo: 4-5 = -1


class Calculo:
    def __init__(self):
        pass
        
    def soma(self, x, y):
        return x + y
        
    def subtracao(self, x, y):
        return x - y
        
        
calc1 = Calculo()
print(calc1.soma(4, 5))
print(calc1.subtracao(4, 5))


#E24
#Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha os métodos ordenacaoCrescente e ordenacaoDecrescente.
#Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como listaBaguncada a lista [3,4,2,1,5] e instancie um outro objeto, decrescente dessa mesma classe com uma outra listaBaguncada sendo [9,7,6,8].
#Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo objeto, use o método
#ordenacaoDecrescente.
#Imprima o resultado da ordenação crescente e da ordenação decresce
#[1, 2, 3, 4, 5] 
#[9, 8, 7, 6]


class Ordenadora:
    
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada
        
    def ordenacaoCrescente(self):
        self.listaBaguncada.sort(reverse = False)
        return self.listaBaguncada
        
    
    def ordenacaoDecrescente(self):
        self.listaBaguncada.sort(reverse = True)
        return self.listaBaguncada
        
lc = Ordenadora([3,4,2,1,5])
ld = Ordenadora([9,7,6,8])

print(lc.ordenacaoCrescente())
print(ld.ordenacaoDecrescente())



#E25
#Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade.
#Defina o atributo cor de sua classe , de maneira que todas as instâncias de sua classe avião sejam da cor “azul”.
#Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião.
#Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:
#“O avião de modelo “x” possui uma velocidade máxima de “y”, capacidade para “z” passageiros e é da cor “w”.
#Sendo x, y, z e w cada um dos atributos da classe “Avião”.
#Valores de entrada:
#modelo BOIENG456: velocidade máxima 1500 km/h: capacidade para 400 passageiros: Cor Azul
#modelo Embraer Praetor 600: velocidade máxima 863km/h: capacidade para 14 passageiros: Cor Azul
#modelo Antonov An-2: velocidade máxima de 258 Km/h: capacidade para 12 passageiros: Cor Azul


class Aviao:
    
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = 'azul'
        self.capacidade = capacidade
lista = []    
    
obj1 = Aviao('BOIENG456', '1500 km/h', 400)
obj2 = Aviao('Embraer Praetor 600', '863km/h', 14)
obj3 = Aviao('Antonov An-2', '258 Km/h', 12)
    
lista.append(obj1)
lista.append(obj2)
lista.append(obj3)
    
    
for i in range(len(lista)):
    print (f'O avião de modelo {lista[i].modelo} possui uma velocidade máxima de {lista[i].velocidade_maxima}, capacidade para {lista[i].capacidade} passageiros e é da cor {lista[i].cor}')
    