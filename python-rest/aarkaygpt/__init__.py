import logging

import azure.functions as func
import openai
import os

secret_key=os.environ['openai_secret_key']
prompt= 'Tell me a story about yellowstone national park'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    # Give openAI secretq key to authenticate
    openai.api_key = secret_key
    
    # get variable from request body
    req_body = req.get_json()
    
    # call openAI completion function
    response = openai.Completion.create(
         model=req_body['model'],
        prompt=req_body['prompt'],
        max_tokens=req_body['max_tokens'],
        temperature=req_body['temperature']
    )
    
    output = response['choices'][0]['text']
    return func.HttpResponse(output, status_code=200)
    
 