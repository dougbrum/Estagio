from botocore.exceptions import ClientError
import logging
import pandas as pd
import boto3
import datetime

# Ler os arquivos CSV
movies_df = pd.read_csv('movies.csv', on_bad_lines='skip')
series_df = pd.read_csv('series.csv', on_bad_lines='skip')

# Configurar as credenciais de acesso
access_key = 'AKIAUVEYMYLCOYTSM4O5'
secret_key = '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'


# Criar uma conexão com o S3
s3 = boto3.client(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)

def create_bucket(bucketNome):
    try:
        s3.create_bucket(Bucket=bucketNome)
    except ClientError(e) as e:
        logging.error(e)
        return False
    return True

create_bucket('sprint7dougbrum')


# Configurar o nome do bucket e a camada de armazenamento
bucket_name = 'sprint7dougbrum'
storage_layer = 'Raw'

# Configurar a estrutura de diretórios de destino
current_date = datetime.datetime.now().strftime('%Y/%m/%d')
movies_destino = f'{storage_layer}/Local/CSV/Movies/{current_date}/movies.csv'
series_destino = f'{storage_layer}/Local/CSV/Series/{current_date}/series.csv'

# Enviar os arquivos CSV para o S3
s3.upload_file('movies.csv', bucket_name, movies_destino)
s3.upload_file('series.csv', bucket_name, series_destino)
