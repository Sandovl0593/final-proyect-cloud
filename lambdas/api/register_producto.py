import boto3
from botocore.exceptions import ClientError
from random import randint


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('proy-productos')
    
    codigo = 'P' + str(randint(1, 90000))
    usuario = event['usuario']
    nombre = event['nombre']
    precio = event['precio']
    marca = event['marca']
    categoria = event['categoria']

    try:

        table.put_item(
            Item={
                "codigo_p": codigo,
                'username': usuario,
                "nombre": nombre,
                'precio': precio,
                'marca': marca,
                'categoria': categoria
            }
        )
        
        return {
            'statusCode': 200,
            'body': 'Nuevo producto insertado'
        }
    
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': 'Error en la ejecución de nuevo producto debido a: ' + str(e)
        }