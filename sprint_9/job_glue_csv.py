import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_CSV', 'S3_OUTPUT_PATH_CSV'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


source_file = args['S3_INPUT_PATH_CSV']
target_path = args['S3_OUTPUT_PATH_CSV']

df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [
            source_file
            ]
    },
    "csv",
    {"withHeader": True, "separator": "|"},
    )
    
    
spark_df = df.toDF()

colunas_inutilizadas = ['tituloOriginal', 'generoArtista', 'personagem', 'nomeArtista', 'anoNascimento', 'anoFalecimento', 'profissao', 'titulosMaisConhecidos']
spark_df = spark_df.drop(*colunas_inutilizadas)  # limpeza das colunas que não serão utilizadas na análise

spark_df = spark_df.dropDuplicates(['id'])  # limpeza das duplicatas

spark_df = spark_df.where( (spark_df.anoLancamento > 1990) & (spark_df.anoLancamento < 1999) )  # filtro dos anos 1990 a 1999

spark_df = spark_df.where(spark_df.genero.contains('Romance'))  # filtro do gênero Romance

spark_df = spark_df.filter(spark_df.tempoMinutos != '\\N')  # limpeza das linhas com dados ausentes

dynamic_df = DynamicFrame.fromDF(spark_df, glueContext, "dynamic_frame")


glueContext.write_dynamic_frame.from_options(
    frame = dynamic_df,
    connection_type = "s3",
    connection_options = {"path": target_path},
    format = "parquet")
    

job.commit()
