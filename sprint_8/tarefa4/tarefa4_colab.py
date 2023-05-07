# -*- coding: utf-8 -*-
"""tarefa4_colab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vVsZSqzOa8CuU4jleo7OBFSLlKq-xwcd
"""

#Instalar as dependências

#Instalar Java 8
!apt-get install openjdk-8-jdk-headless -qq > /dev/null

#Realizar o download do Spark
!wget -q https://dlcdn.apache.org/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3.tgz

#Descompartar o arquivo baixado
!tar xf spark-3.4.0-bin-hadoop3.tgz

#Instalando a findspark
!pip install -q findspark

#Configurar as variáveis de ambiente

#Importando a biblioteca os
import os

#Definindo a variável de ambiente do Java
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"

#Definindo a variável de ambiente do Spark
os.environ["SPARK_HOME"] = "/content/spark-3.4.0-bin-hadoop3"

#Importando a findspark
import findspark

#Iniciando o findspark
findspark.init('spark-3.4.0-bin-hadoop3')

#1
from pyspark.sql import SparkSession

# Iniciar a sessão Spark
spark = SparkSession.builder \
    .appName("Exercicio Intro") \
    .getOrCreate()

# Ler o arquivo nomes_aleatorios.txt como um DataFrame
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

df_nomes.show(5)

#2
# Renomear a coluna para "Nomes"
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Imprimir o esquema do DataFrame
df_nomes.printSchema()

# Mostrar 10 linhas do DataFrame
df_nomes.show(10, truncate=False)

#3
from pyspark.sql.functions import when, rand

df_nomes = df_nomes.withColumn("Escolaridade", 
                               when(rand() < 0.333, "Fundamental")
                               .when(rand() < 0.666, "Medio")
                               .otherwise("Superior"))

df_nomes.show(5)

#4
from pyspark.sql.functions import *
from random import randint

paises_sulamericanos = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Equador", "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela"]
pais_aleatorio = udf(lambda: paises_sulamericanos[randint(0, len(paises_sulamericanos) - 1)], StringType())

df_nomes = df_nomes.withColumn("Pais", pais_aleatorio())



df_nomes.show(5)

#5
from pyspark.sql.functions import rand, floor

df_nomes = df_nomes.withColumn("AnoNascimento", (floor(rand() * 66) + 1945).cast("integer"))

#6
df_select = df_nomes.filter(df_nomes["AnoNascimento"] >= 2000)
df_select.select("Nomes").show(10, truncate=False)

#7
df_nomes.createOrReplaceTempView("pessoas")
spark.sql("SELECT Nomes FROM pessoas WHERE AnoNascimento >= 2000").show(10, truncate=False)

#8
qtd_millennials = df_nomes.filter((df_nomes["AnoNascimento"] >= 1980) & (df_nomes["AnoNascimento"] <= 1994)).count()
print("Número de pessoas da geração Millennials (DataFrame):", qtd_millennials)

#9

spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994").show()

#10
df_nomes.createOrReplaceTempView("pessoas")

query = """
SELECT Pais, 
       CASE WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
            WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials(Geração Y)'
            WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
       END AS Geracao,
       COUNT(*) AS Quantidade
FROM pessoas
GROUP BY Pais, Geracao
ORDER BY Pais, Geracao, Quantidade
"""

df_qtd_por_pais = spark.sql(query)
df_qtd_por_pais.show()

