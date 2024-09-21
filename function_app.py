import azure.functions as func
import logging
import os
from dotenv import load_dotenv
import json
import openai

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        input = req_body.get('input')
    except ValueError:
        input = None

    if input:
        load_dotenv()

        # Initialize OpenAI variables
        AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
        AZURE_OPENAI_ADA_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT")
        AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
        AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
        AZURE_OPENAI_MAX_RESPONSE = int(os.getenv("AZURE_OPENAI_MAX_RESPONSE"))
        AZURE_OPENAI_VERSION = os.getenv("AZURE_OPENAI_VERSION")
        
        # Initialize the OpenAI client
        openai_client = openai.AzureOpenAI(
            api_version=AZURE_OPENAI_VERSION,
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_KEY,)

        
        SYSTEM_MESSAGE = """You are a travel agent that answers question."""

        USER_MESSAGE = input

        # Generate a response using the OpenAI model
        response = openai_client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            temperature=0.0,
            max_tokens=AZURE_OPENAI_MAX_RESPONSE,
            messages=[
                {"role": "system", "content": SYSTEM_MESSAGE},
                {"role": "user", "content": USER_MESSAGE},
            ],
            top_p=0.5
        )
        answer = response.choices[0].message.content

        # Return the response as a JSON object
        response = {
            "output": answer
        }
        return func.HttpResponse(
            json.dumps(response),
            mimetype="application/json"
        )
    
    else:
        return func.HttpResponse(
             "Please pass an input in the request body",
             status_code=400
        )