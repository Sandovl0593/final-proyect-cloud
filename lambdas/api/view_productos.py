import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('proy-productos')
    
    try:
        response = table.scan()
        items = response['Items']
        
        return {
            'statusCode': 200,
            'body': json.dumps(items)
        }
    
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': 'Error en la visualización del inventario debido a: ' + str(e)
        }