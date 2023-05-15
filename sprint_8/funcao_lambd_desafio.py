import os
import time
import boto3
import logging
import pandas as pd
import requests
import datetime
from botocore.exceptions import ClientError

def lambda_handler(event, context):

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
            time.sleep(10)  # Esperar 10 segundos para o bucket ficar disponível
        except ClientError as e:
            logging.error(e)
            return False
        return True

    bucket_created = create_bucket('sprint7dougbrum')
    
    if bucket_created:
        #api_key = "65c2bf3138f0b29ee4cec4fef2261a29"
        url = f"https://api.themoviedb.org/3/discover/movie?api_key=65c2bf3138f0b29ee4cec4fef2261a29&with_genres=10749&total_page="

        filmes = []

        # Inicia na primeira página
        pagina_atual = 1
        total_paginas = 2204

        while (pagina_atual <= total_paginas):
            response = requests.get(url + str(pagina_atual))
            data = response.json()
            total_paginas = data['total_pages']
            
            for movie in data['results']:
                df = {'Titulo': movie['title'],
                   'Data de lançamento': movie['release_date'],
                    'Visão geral': movie['overview'],
                    'Votos': movie['vote_count'],
                    'Média de votos': movie['vote_average'],
                    'Popularidade':movie['popularity'],
                    'vote_count': movie['vote_count']}
                filmes.append(df)
                
            # Passa para a próxima página
            pagina_atual += 1

        df = pd.DataFrame(filmes)

        # Salve o DataFrame como JSON em /tmp/
        df.to_json('/tmp/filmes.json')

        bucket_name = 'sprint7dougbrum'
        storage_layer = 'Raw'
        current_date = datetime.datetime.now().strftime('%Y/%m/%d')
        movies_destino = f'{storage_layer}/Tmdb/JSON/Movies/{current_date}/filmes.json'

        # Enviar os arquivos JSON para o S3
        s3.upload_file('/tmp/filmes.json', bucket_name, movies_destino)

        return {
            'statusCode': 200,
            'body': 'Upload concluído com sucesso!'
        }
    else:
        return {
            'statusCode': 500,
            'body': 'Falha na criação do bucket'
        }

