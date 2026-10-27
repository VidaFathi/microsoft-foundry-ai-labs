# Module 3 — Building an AI Chatbot with Microsoft Foundry

## Project Overview

A hands-on Generative AI project demonstrating how to build Python applications using **Microsoft Foundry, GPT-5.2, and the OpenAI Responses API**.

This project is part of my Microsoft AI Engineering learning journey, progressing from basic model inference to interactive, multi-turn conversations.

### Technologies Used

- **Cloud Platform:** Microsoft Azure / Microsoft Foundry
- **AI Model:** GPT-5.2
- **Programming Language:** Python
- **API:** OpenAI Responses API
- **Authentication:** Microsoft Entra ID
- **Development Environment:** VS Code for the Web

---

## 1. Project Architecture

The application connects to a GPT-5.2 deployment hosted in Microsoft Foundry.

```mermaid
flowchart LR
    A[User] --> B[Python Chatbot]
    B --> C[OpenAI Responses API]
    C --> D[Microsoft Foundry]
    D --> E[GPT-5.2 Deployment]
    E --> D
    D --> C
    C --> B
    B --> A
```

**How it works:**

1. The user enters a question in the Python application.
2. The application authenticates with Microsoft Entra ID.
3. The Responses API sends the request to GPT-5.2.
4. The deployed model generates an answer.
5. The Python application displays the response.
6. In the multi-turn version, the previous response ID is reused to provide conversation context.

---

## 2. Python Exercises

The project contains three progressive exercises.

| File | Description |
|---|---|
| `run_model.py` | Connects to GPT-5.2 and sends a predefined question. |
| `interactive_chat_one_question.py` | Allows a user to enter a question and receive a response. |
| `interactive_chat_multiple_questions.py` | Supports multiple questions, follow-up context, and an exit command. |

### Exercise 1 — Basic Model Inference

**File:** `run_model.py`

Demonstrates the first successful Python API connection to Microsoft Foundry.

```python
response = client.responses.create(
    model=deployment_name,
    input="What is the capital of France?"
)

print(response.output_text)
```

**Observed output:**

```text
Paris.
```

### Exercise 2 — Interactive AI Assistant

**File:** `interactive_chat_one_question.py`

Improves the application by allowing the user to enter a question at runtime.

```python
question = input("Ask your AI assistant a question: ")

response = client.responses.create(
    model=deployment_name,
    input=question
)

print(response.output_text)
```

### Exercise 3 — Multi-Turn AI Chatbot

**File:** `interactive_chat_multiple_questions.py`

Extends the assistant with continuous interaction and conversation context.

Key features:

- Accepts multiple questions in one session.
- Maintains follow-up context using `previous_response_id`.
- Ignores empty questions.
- Allows users to type `exit` to end the conversation.

The previous response ID allows the model to reference an earlier exchange when supported by the Responses API.

---

## 3. Microsoft Foundry Playground

Deployed GPT-5.2 using the **Global Standard** deployment type and tested model responses through the Microsoft Foundry Playground.

![Microsoft Foundry GPT-5.2 Playground](foundry-gpt52-playground.png)

*Screenshot: GPT-5.2 deployment in Microsoft Foundry.*

---

## 4. Running the Project

### Prerequisites

- Python 3.10 or later
- An Azure subscription
- A Microsoft Foundry project
- Access to a deployed GPT-5.2 model
- Microsoft Entra ID authentication configured
- Required Python packages installed

### Install Dependencies

From the repository root:

```bash
python -m pip install -r module-3-chatbot/requirements.txt
```

### Run the Basic Model Example

```bash
python module-3-chatbot/run_model.py
```

### Run the Interactive Chatbot

```bash
python module-3-chatbot/interactive_chat_one_question.py
```

### Run the Multi-Turn Chatbot

```bash
python module-3-chatbot/interactive_chat_multiple_questions.py
```

Type `exit` to end the multi-turn conversation.

**Configuration:** The current scripts contain the endpoint and deployment name used in the learning exercises. To run them with another Microsoft Foundry resource, update those values in the Python files.

Authentication uses `DefaultAzureCredential`, so an appropriate Azure identity with model access is required.

---

## 5. Key Learning Outcomes

Through this project, I gained practical experience with:

- Deploying and testing a language model in Microsoft Foundry.
- Connecting Python applications to hosted AI models.
- Using the OpenAI Responses API.
- Authenticating applications with Microsoft Entra ID.
- Building interactive command-line AI applications.
- Managing multi-turn conversations using response IDs.
- Structuring and documenting Python applications for GitHub.

---

## 6. Current Project Status

| Component | Status |
|---|---|
| GPT-5.2 deployment | Completed |
| Foundry Playground testing | Completed |
| Successful Python API inference | Verified |
| Single-question chatbot | Developed |
| Multi-turn chatbot | Developed |
| Automated evaluation tests | Planned |
| Production deployment | Not implemented |

The exercises demonstrate foundational AI application development concepts. They are educational examples rather than production-ready applications.

## 7. Future Improvements

- Refactor the chatbot into reusable Python functions.
- Add automated unit tests.
- Improve exception handling and configuration management.
- Evaluate response quality, latency, and token usage.
- Add document retrieval using Retrieval-Augmented Generation (RAG).
- Build a web interface for the chatbot.

---

## 8. Security and Limitations

- API keys, access tokens, and confidential data must never be committed to GitHub.
- Azure model usage may incur charges.
- The examples do not contain real patient information or confidential employer documents.
- Conversation context depends on the Responses API; the project does not implement a persistent chat-history database.

---

## References

- [Microsoft Foundry](https://ai.azure.com/)
- [Microsoft Learn — Develop generative AI applications](https://learn.microsoft.com/en-us/training/paths/develop-generative-ai-apps/)
- [Azure OpenAI API version lifecycle](https://learn.microsoft.com/en-us/azure/foundry/openai/api-version-lifecycle)

---

**Project by Vida Fathi**

Data Engineer | Azure | Python | Applied AI