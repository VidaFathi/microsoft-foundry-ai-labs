"""Exercise 2: Interactive chatbot with multi-turn conversation context."""
import os

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

BASE_URL = os.getenv(
    "AZURE_OPENAI_BASE_URL",
    "https://aividaproject.services.ai.azure.com/openai/v1/",
)
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.2")


def main() -> None:
    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(), "https://ai.azure.com/.default"
    )
    previous_response_id = None
    print("AI Assistant is ready! Type 'exit' to quit.")

    with OpenAI(base_url=BASE_URL, api_key=token_provider) as client:
        while True:
            question = input("\nYou: ").strip()
            if question.lower() == "exit":
                print("Goodbye!")
                break
            if not question:
                continue

            request = {"model": DEPLOYMENT_NAME, "input": question}
            if previous_response_id:
                request["previous_response_id"] = previous_response_id

            try:
                response = client.responses.create(**request)
            except Exception as error:
                print(f"Request failed: {error}")
                continue
            print(f"\nAI Assistant: {response.output_text}")
            previous_response_id = response.id


if __name__ == "__main__":
    main()
