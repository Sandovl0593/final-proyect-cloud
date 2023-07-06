import boto3
from botocore.exceptions import ClientError
from random import randint


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table_prod = dynamodb.Table('proy-productos')
    table_compra = dynamodb.Table('proy-compras')
    
    tenant_id = event['tenant_id']

    codigo_c = 'C' + str(randint(1, 90000))
    comprador = event['usuario_comprador']
    codigo_p = event['codigo_producto']
    vendedor = event['usuario_vendedor']

    try:
        # Actualiza el campo 'usuario_p' en la tabla 'producto'
        table_prod.update_item(
            Key={'codigo_p': codigo_p},
            UpdateExpression='SET username = :val',
            ExpressionAttributeValues={':val': comprador}
        )
        
        # Inserta una nueva compra en la tabla 'compra'
        table_compra.put_item(
            Item={
                "tenant_id": tenant_id,
                'username': comprador,
                'codigo_compra': codigo_c,
                'codigo_producto': codigo_p,
                'vendedor': vendedor
            }
        )
        
        return {
            'statusCode': 200,
            'body': 'Inserción exitosa en DynamoDB'
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': 'Error al insertar en DynamoDB: ' + str(e)
        }
