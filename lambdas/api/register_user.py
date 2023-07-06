import json
import boto3

def lambda_handler(event, context):
    # Entrada (json)
    tenant_id = event['tenant_id']
    user_id = event['user_id']
    user_profile = event['user_profile']

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('proy_users')
    alumno = {
        'tenant_id': tenant_id,
        'user_id': user_id,
        'user_profile': user_profile
    }
    response = table.put_item(Item=alumno)

    # Publicar en SNS
    sns_client = boto3.client('sns')
    response_sns = sns_client.publish(
    	TopicArn = 'arn:aws:sns:us-east-1: ....',
    	Subject = f'Bienvenido User {user_id}',
        Message = json.dumps(alumno),
        MessageAttributes = {
            'tenant_id': {'DataType': 'String', 'StringValue': tenant_id }
        }
    )
    print(response_sns)

    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }