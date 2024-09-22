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
        input1 = req_body.get('Value Proposition')
        input2 = req_body.get('Customer Segment')
        input3 = req_body.get('Channels')
        input4 = req_body.get('Revenue Streams')
        input5 = req_body.get('Key Activities')
        input6 = req_body.get('Risk Factors')
        
    except ValueError:
        input1 = None
        input2 = None
        input3 = None
        input4 = None
        input5 = None
        input6 = None

    if input1 and input2 and input3 and input4 and input5 and input6:
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

        #input 1
        SYSTEM_MESSAGE1 = """You are a travel agent that answers question."""
        USER_MESSAGE1 = input1
        # Generate a response using the OpenAI model
        response1 = openai_client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            temperature=0.0,
            max_tokens=AZURE_OPENAI_MAX_RESPONSE,
            messages=[
                {"role": "system", "content": SYSTEM_MESSAGE1},
                {"role": "user", "content": USER_MESSAGE1},
            ],
            top_p=0.5
        )
        answer1 = response1.choices[0].message.content

        #input 2
        SYSTEM_MESSAGE2 = """You are a travel agent that answers question."""
        USER_MESSAGE2 = input2
        # Generate a response using the OpenAI model
        response2 = openai_client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            temperature=0.0,
            max_tokens=AZURE_OPENAI_MAX_RESPONSE,
            messages=[
                {"role": "system", "content": SYSTEM_MESSAGE2},
                {"role": "user", "content": USER_MESSAGE2},
            ],
            top_p=0.5
        )
        answer2 = response2.choices[0].message.content

        #input 3
        SYSTEM_MESSAGE3 = """You are a travel agent that answers question."""
        USER_MESSAGE3 = input3
        # Generate a response using the OpenAI model
        response3 = openai_client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            temperature=0.0,
            max_tokens=AZURE_OPENAI_MAX_RESPONSE,
            messages=[
                {"role": "system", "content": SYSTEM_MESSAGE3},
                {"role": "user", "content": USER_MESSAGE3},
            ],
            top_p=0.5
        )
        answer3 = response3.choices[0].message.content

        #input 4
        SYSTEM_MESSAGE4 = """You are a travel agent that answers question."""
        USER_MESSAGE4 = input4
        # Generate a response using the OpenAI model
        response4 = openai_client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            temperature=0.0,
            max_tokens=AZURE_OPENAI_MAX_RESPONSE,
            messages=[
                {"role": "system", "content": SYSTEM_MESSAGE4},
                {"role": "user", "content": USER_MESSAGE4},
            ],
            top_p=0.5
        )
        answer4 = response4.choices[0].message.content

        #input 5
        SYSTEM_MESSAGE5 = """You are a travel agent that answers question."""
        USER_MESSAGE5 = input5
        # Generate a response using the OpenAI model
        response5 = openai_client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            temperature=0.0,
            max_tokens=AZURE_OPENAI_MAX_RESPONSE,
            messages=[
                {"role": "system", "content": SYSTEM_MESSAGE5},
                {"role": "user", "content": USER_MESSAGE5},
            ],
            top_p=0.5
        )
        answer5 = response5.choices[0].message.content

        #input 6
        SYSTEM_MESSAGE6 = """You are a travel agent that answers question."""
        USER_MESSAGE6 = input6
        # Generate a response using the OpenAI model
        response6 = openai_client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            temperature=0.0,
            max_tokens=AZURE_OPENAI_MAX_RESPONSE,
            messages=[
                {"role": "system", "content": SYSTEM_MESSAGE6},
                {"role": "user", "content": USER_MESSAGE6},
            ],
            top_p=0.5
        )
        answer6 = response6.choices[0].message.content

        #input 7
        SYSTEM_MESSAGE7 = """You will summarize all the answers provided to you. Each answer is separated by *****"""
        USER_MESSAGE7 = answer1 + "*****" + answer2 + "*****" + answer3 + "*****" + answer4 + "*****" + answer5 + "*****" + answer6
        # Generate a response using the OpenAI model
        response7 = openai_client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            temperature=0.0,
            max_tokens=AZURE_OPENAI_MAX_RESPONSE,
            messages=[
                {"role": "system", "content": SYSTEM_MESSAGE7},
                {"role": "user", "content": USER_MESSAGE7},
            ],
            top_p=0.5
        )
        answer7 = response7.choices[0].message.content


        # Return the response as a JSON object
        response = {
            "Value Proposition Score": answer1,
            "Customer Segement Score": answer2,
            "Channels Score": answer3,
            "Revenue Streams Score": answer4,
            "Key Activities Score": answer5,
            "Risk Factors Score": answer6,
            "Summary": answer7
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