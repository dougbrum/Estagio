import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_JSON', 'S3_OUTPUT_PATH_JSON'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


source_file = args['S3_INPUT_PATH_JSON']
target_path = args['S3_OUTPUT_PATH_JSON']

df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={
        "paths": [
            source_file
        ]
    },
    format="json",
)


    
spark_df = df.toDF()

spark_df = spark_df.dropDuplicates(["Titulo"])  # limpeza de IDs duplicados

spark_df = spark_df.where( (spark_df["Votos"] > 0) & (spark_df["Popularidade"] > 0) & (spark_df["Média de votos"] > 0) )  # limpeza de valores zerados/outliers

dynamic_df = DynamicFrame.fromDF(spark_df, glueContext, "dynamic_frame")


glueContext.write_dynamic_frame.from_options(
    frame = dynamic_df,
    connection_type = "s3",
    connection_options = {
        "path": target_path
    },
    format = "parquet")

job.commit
