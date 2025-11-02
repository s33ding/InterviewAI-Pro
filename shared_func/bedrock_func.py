import boto3
import json

def run_bedrock(prompt, model_id="anthropic.claude-3-sonnet-20240229-v1:0"):
    """Run prompt through AWS Bedrock"""
    client = boto3.client('bedrock-runtime')
    
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [{"role": "user", "content": prompt}]
    })
    
    response = client.invoke_model(
        body=body,
        modelId=model_id,
        contentType="application/json"
    )
    
    result = json.loads(response['body'].read())
    return result['content'][0]['text']
