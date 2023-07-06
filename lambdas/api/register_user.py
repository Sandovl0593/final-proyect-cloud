import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("proy-users")

    tenant_id = event["tenant_id"]

    nombre_usuario = event['nombre_usuario']
    nombre = event['nombre']
    telefono = event['telefono']
    direccion = event['direccion']
    email = event['email']
    contrasenha = event['contrasenha']
    
    try:
        # Inserta el nuevo usuario en DynamoDB
        table.put_item(
            Item={
                "tenant_id": tenant_id,
                'username': nombre_usuario,
                'name': nombre,
                'phone': telefono,
                'address': direccion,
                'email': email,
                'password': contrasenha
            }
        )
        
        return {
            'statusCode': 200,
            'body': 'Nuevo usuario registrado'
        }
    
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': 'Error en el registro debido a: ' + str(e)
        }