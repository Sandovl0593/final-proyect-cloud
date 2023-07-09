import boto3
import json
from botocore.exceptions import ClientError
from random import randint


def lambda_handler(event, context):
    sns_client = boto3.client('sns')

    tenant_id = event['tenant_id']
    codigo_c = 'C' + str(randint(1, 90000))
    comprador = event['usuario_comprador']
    codigo_p = event['codigo_producto']
    vendedor = event['usuario_vendedor']

    register = {
        "tenant_id": tenant_id,
        "codigo_c": codigo_c,
        "comprador": comprador,
        "codigo_p": codigo_p,
        "vendedor": vendedor,
    }

    try:
        sns_client = boto3.client('sns')
        response_sns = sns_client.publish(
            TopicArn = 'arn:aws:sns:us-east-1:267046291430:tema-nuevaCompra',
            Subject = f"Grcias por tu compra, {comprador}",
            Message = json.dumps(register),
            MessageAttributes = {
                'tenant_id': {'DataType': 'String', 'StringValue': tenant_id },
                'comprador': {'DataType': 'String', 'StringValue': comprador }
            }
        )
        
        
        return {
            'statusCode': 200,
            'body': json.dumps(response_sns)
        }
    
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': 'Error al insertar en DynamoDB: ' + str(e)
        }
