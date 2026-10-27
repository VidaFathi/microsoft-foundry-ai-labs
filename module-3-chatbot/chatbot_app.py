"""Exercise 3: Modular chatbot using Microsoft Foundry Responses API."""
import os

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

BASE_URL = os.getenv(
    "AZURE_OPENAI_BASE_URL",
    "https://aividaproject.services.ai.azure.com/openai/v1/",
)
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.2")


def create_client() -> OpenAI:
    """Authenticate with Microsoft Entra ID and create the API client."""
    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(), "https://ai.azure.com/.default"
    )
    return OpenAI(base_url=BASE_URL, api_key=token_provider)


def ask_ai(
    client: OpenAI,
    question: str,
    previous_response_id: str | None = None,
):
    """Send a question, including prior response context when available."""
    question = question.strip()
    if not question:
        raise ValueError("Question cannot be empty")

    request = {"model": DEPLOYMENT_NAME, "input": question}
    if previous_response_id:
        request["previous_response_id"] = previous_response_id
    return client.responses.create(**request)


def main() -> None:
    """Run a multi-turn command-line chatbot until the user exits."""
    previous_response_id = None
    print("Welcome to the AI Assistant! Type 'exit' to quit.")

    with create_client() as client:
        while True:
            question = input("\nYou: ").strip()
            if question.lower() == "exit":
                print("Goodbye!")
                break
            if not question:
                continue
            try:
                response = ask_ai(client, question, previous_response_id)
            except Exception as error:
                print(f"Request failed: {error}")
                continue

            print(f"\nAI: {response.output_text}")
            previous_response_id = response.id


if __name__ == "__main__":
    main()
