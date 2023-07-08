import json
import boto3

def lambda_handler(event, context):
    # Entrada (json)
    archivo_json = json.loads(event['Records'][0]['Sns']['Message'])

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table_compra = dynamodb.Table('proy_compras')
    table_prod = dynamodb.Table('proy_productos')

    tenant_id = archivo_json['tenant_id']
    codigo_c = archivo_json["codigo_c"]
    comprador = archivo_json['comprador']
    codigo_p = archivo_json['codigo_p']
    vendedor = archivo_json['vendedor']
    
    # Actualiza el poseedor del producto comprado
    table_prod.update_item(
            Key={'codigo_p': codigo_p},
            UpdateExpression='SET username = :val',
            ExpressionAttributeValues={':val': comprador}
    )
        
    register = {
        "tenant_id": tenant_id,
        'username': comprador,
        'codigo_compra': codigo_c,
        'codigo_producto': codigo_p,
        'vendedor': vendedor
    }

    # Inserta una nueva compra en la tabla 'compra'
    table_compra.put_item( Item=register )

    # Salida (json)
    return {
        'statusCode': 200,
        'response': json.dumps(register)
    }
