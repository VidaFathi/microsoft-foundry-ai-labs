"""Module 1 local exercise: build structured messages without making API calls."""

import json
from typing import TypedDict


class Message(TypedDict):
    role: str
    content: str


def build_messages(instructions: str, question: str) -> list[Message]:
    """Build a system message and a user message for an AI chat request."""
    if not instructions.strip() or not question.strip():
        raise ValueError("Instructions and question cannot be empty")
    return [
        {"role": "system", "content": instructions.strip()},
        {"role": "user", "content": question.strip()},
    ]


if __name__ == "__main__":
    messages = build_messages(
        "You explain AI engineering concepts simply and accurately.",
        "What is the difference between a Foundry portal and SDK?",
    )
    print(json.dumps(messages, indent=2))
    print("\nThis exercise structures a prompt. No API request was sent.")
