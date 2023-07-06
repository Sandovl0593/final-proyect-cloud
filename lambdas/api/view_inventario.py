import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('proy-productos')
    
    usuario_l = event['usuario']
    
    try:
        # Realiza una consulta en DynamoDB utilizando un filtro en los elementos
        response = table.scan(
            FilterExpression='username = :val',
            ExpressionAttributeValues={':val': usuario_l}
        )
        
        # Transforma la respuesta de DynamoDB en el formato deseado
        productos_l = []
        for item in response['Items']:
            producto_l = {
                'codigo': item['codigo_p'],
                'usuario_nombre': item['username'],
                'nombre': item['nombre'],
                'precio': item['precio'],
                'marca': item['marca'],
                'tipo': item['tipo']
            }
            productos_l.append(producto_l)
        
        return {
            'statusCode': 200,
            'body': productos_l
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': 'Error en la visualización del inventario debido a: ' + str(e)
        }