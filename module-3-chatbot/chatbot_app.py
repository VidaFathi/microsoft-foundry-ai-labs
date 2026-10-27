#This is the foundation of an Interactive AI chatbot that handels MULTIPLE question per run:

# This application connects to Microsoft Foundry.
# It sends questions to the deployed GPT-5.2 model.
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

# Store the previous response ID to maintain conversation history
previous_response_id = None

print("AI Assistant is ready! Type 'exit' to quit.")

while True:
    # Ask the user for a question
    question = input("\nYou: ").strip()

    # End the conversation
    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Ignore empty questions
    if not question:
        continue

    # Prepare the API request
    request = {
        "model": deployment_name,
        "input": question
    }

    # Include previous conversation context when available
    if previous_response_id:
        request["previous_response_id"] = previous_response_id

    # Send the request to GPT-5.2
    response = client.responses.create(**request)

    # Display the model's answer
    print(f"\nAI Assistant: {response.output_text}")

    # Save the response ID for the next question
    previous_response_id = response.id
