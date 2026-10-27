"""Exercise 1: Send a single request to Microsoft Foundry GPT-5.2."""
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
    with OpenAI(base_url=BASE_URL, api_key=token_provider) as client:
        response = client.responses.create(
            model=DEPLOYMENT_NAME,
            input="What is the capital of France?",
        )
        print(f"answer: {response.output_text}")


if __name__ == "__main__":
    main()
