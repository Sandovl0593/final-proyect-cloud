import json
import boto3

def lambda_handler(event, context):
    # Entrada (json)
    video_dir:str = event['Records'][0]['s3']['object']['key']
    # user_videos/ 
    tenant_id = video_dir.split('/')[1]                         # usuario <-> tenant_id en los dynamodb
    name_video = video_dir.split('/')[2][:-4]                   # nombre del video

    archivo_last_modified = event['Records'][0]['eventTime']
    archivo_size = event['Records'][0]['s3']['object']['size']
    archivo = {
        'tenant_id': tenant_id,
        'video_dir': video_dir,
        'archivo_datos': {
            'last_modified': archivo_last_modified,
            'size': archivo_size,
        }    
    }
    # Cliente de Transacribe
    transcribe_client = boto3.client('transcribe')
    output_key = video_dir[:-4] + '.json'
    
    # Configura los parámetros para la solicitud de transcripción
    transcribe_job_name = f'subtitled-{name_video}'             # Nombre de la transcripcion
    language_code = 'es-US'                                     # Código de idioma (español de Estados Unidos)
    
    # Crea una solicitud de transcripción
    response = transcribe_client.start_transcription_job(
        TranscriptionJobName=transcribe_job_name,
        LanguageCode=language_code,
        Media={
            'MediaFileUri': f's3://{video_dir}'
        },
        OutputBucketName=f'subtitle-{name_video}',
        OutputKey=output_key
    )
    return {
        'statusCode': 200,
        'body': response
    }