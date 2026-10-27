#This is the foundation of an Interactive AI chatbot that handels ONE question per run:

# This application connects to Microsoft Foundry. It sends questions to the deployed GPT-5.2 model.
# It then displays the generated response.

#imports the python sdk used to communicate with the AI model.
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# A)) Configure Microsoft Foundry:
    #1.Identifies where to send API requests
endpoint = "https://aividaproject.services.ai.azure.com/openai/v1"

    #2.selects your deployed model
deployment_name = "gpt-5.2"

# B)) Authenticate using Microsoft Entra ID:
token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

# C)) Create an OpenAI client:
client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)

# sends the question to GPT-5.2 and gets a resopnse
# D)) Get a question from the user:
question = input("Ask your AI assistant a question: ")


# Send the question to GPT-5.2
response = client.responses.create(
    model=deployment_name,
    input=question
)

# Display the AI-generated answer
print(f"AI Assistant: {response.output_text}")
