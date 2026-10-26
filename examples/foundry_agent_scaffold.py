"""Learning scaffold generated from Foundry Toolkit and sanitized for sharing.

Status: not yet confirmed to run successfully with the selected SDK version.
Do not publish credentials. May require additional configuration or SDK updates.
"""

import asyncio
import os

from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient
from azure.identity.aio import DefaultAzureCredential

ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "")
MODEL_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.2")

AGENT_INSTRUCTIONS = "You are a helpful AI software development assistant."
USER_INPUTS = ["Explain the difference between a model and an agent."]


async def main() -> None:
    if not ENDPOINT:
        raise RuntimeError("Set AZURE_OPENAI_ENDPOINT in your environment first")

    async with DefaultAzureCredential() as credential:
        async with Agent(
            client=OpenAIChatClient(
                azure_endpoint=ENDPOINT,
                model=MODEL_DEPLOYMENT_NAME,
                credential=credential,
            ),
            name="module-1-demo-agent",
            instructions=AGENT_INSTRUCTIONS,
            tools=None,
        ) as agent:
            for question in USER_INPUTS:
                print(f"Question: {question}")
                async for chunk in agent.run([question], stream=True):
                    if chunk.text:
                        print(chunk.text, end="", flush=True)
                print()


if __name__ == "__main__":
    asyncio.run(main())
