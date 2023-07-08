import json
import boto3

def lambda_handler(event, context):
    # Entrada (json)

    print(event) # Revisar en CloudWatch

    archivo_json = json.loads(event['Records'][0]['Sns']['Message'])

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('proy_users')

    tenant_id = archivo_json["tenant_id"]

    username = archivo_json['nombre_usuario']
    name = archivo_json['nombre']
    phone = archivo_json['telefono']
    address = archivo_json['direccion']
    email = archivo_json['email']
    password = archivo_json['contrasenha']

    message = {
        'tenant_id': tenant_id,
        'username': username,
        'name': name,
        'phone': phone,
        'address': address,
        'email': email,
        'password': password
    }

    response = table.put_item(Item=message)

    # Salida (json)
    return {
        'statusCode': 200,
        'response': json.dumps(response)
    }