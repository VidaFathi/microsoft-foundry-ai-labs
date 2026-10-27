
# This application connects to Microsoft Foundry.
# It sends questions to the deployed GPT-5.2 model.
# It then displays the generated response.

#imports the python sdk used to communicate with the AI model.
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

#Identifies where to send API requests
endpoint = "https://aividaproject.services.ai.azure.com/openai/v1"

#selects your deployed model
deployment_name = "gpt-5.2"
token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)

# sends the question to GPT-5.2 and gets a resopnse
response = client.responses.create(
    model=deployment_name,
    input="What is the capital of France?",
)

print(f"answer: {response.output_text}")
