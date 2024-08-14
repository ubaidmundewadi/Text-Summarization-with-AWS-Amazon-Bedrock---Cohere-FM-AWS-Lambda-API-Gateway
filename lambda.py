import json
import boto3

#1 Import boto3 and create client connection with bedrock

client = boto3.client('bedrock-runtime')
def lambda_handler(event, context):
    
    user_prompt=event["prompt"]
    
    response = client.invoke_model(
        body=json.dumps({"prompt": user_prompt,"temperature": 0.9,"max_tokens": 20,}),
        contentType='application/json',
        accept='application/json',
        modelId='cohere.command-text-v14',
        )
    
    response_byte = response['body'].read()
    response_string = json.loads(response_byte)


    return {
        'statusCode': 200,
        'body': response_string
    }
