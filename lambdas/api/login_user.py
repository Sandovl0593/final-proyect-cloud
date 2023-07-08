import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("proy-users")

    l_usuario = event['nombre_usuario']
    l_contrasenha = event['contrasenha']
    
    try:
        response = table.scan(
            FilterExpression='username = :user and password = :pass',
            ExpressionAttributeValues={
                ':user': l_usuario,
                ':pass': l_contrasenha
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': 'Error en el login debido a: ' + str(e)
        }