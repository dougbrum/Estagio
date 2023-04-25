# vamos precisar criar um sistema de computação distribuido e para isso usamos o RDD
arq = sc.textFile("README.md")
# Esse arquivo esta sendo dividido em linhas através do comando acima
# Aqui fazemos uma colaboração entre as funções split que vai fazer a separação das palavras nas linhas levando em 
#consideração o espaço entre palavras e a função flatMap que trata de transformar isso em um conjunto de palavras
palavras = arq.flatMap(lambda line: line.split(" "))
# É possível utilizar a função map para criar pares chaves e valor, onde cada valor é 1
# A função reduceByKey vai tratar de somar o valor contido nesses pares(chave, valor)
cont_palavras = palavras.map(lambda palavra: (palavra, 1)).reduceByKey(lambda x, y: x + y)
# A exibição fica por conta de collect()
cont_palavras.collect()