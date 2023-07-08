import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')

    tenant_id = event["tenant_id"]

    username = event['nombre_usuario']
    nombre = event['nombre']
    telefono = event['telefono']
    direccion = event['direccion']
    email = event['email']
    contrasenha = event['contrasenha']

    register = {
        "tenant_id": tenant_id,
        "username": username,
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion,
        "email": email,
        "contrasenha": contrasenha,
    }
    
    try:
        sns_client = boto3.client('sns')
        response_sns = sns_client.publish(
            TopicArn = 'arn:aws:sns:us-east-1:267046291430:tema-nuevoUser',
            Subject = f"Bienvenido {nombre} a UTEC SHOP",
            Message = json.dumps(register),
            MessageAttributes = {
                'tenant_id': {'DataType': 'String', 'StringValue': tenant_id },
                'username': {'DataType': 'String', 'StringValue': username }
            }
        )
        
        
        return {
            'statusCode': 200,
            'body': json.dumps(response_sns)
        }
    
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': 'Error en el registro debido a: ' + str(e)
        }