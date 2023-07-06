import json
import boto3

def lambda_handler(event, context):
    # Entrada (json)

    print(event) # Revisar en CloudWatch

    archivo_json = json.loads(event['Records'][0]['Sns']['Message'])

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('proy_compras')

    message = {
        'tenant_id': archivo_json['tenant_id'],
        'user_id': archivo_json['user_id'],
        'info': archivo_json['info']
    }
    print(message) # Revisar en CloudWatch

    response = table.put_item(Item=message)

    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
