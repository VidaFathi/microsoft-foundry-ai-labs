# Module 1 Study Notes — Plan and Prepare to Develop AI Solutions on Azure

**Track:** Microsoft Learn — Develop generative AI apps on Microsoft Foundry  
**Module:** Plan and prepare to develop AI solutions on Azure  
**Learning goal:** Understand the Azure AI development workspace and test an existing generative AI model.

## 1. What is Microsoft Foundry?

Microsoft Foundry is Azure's platform for organizing and developing AI apps and agents. Instead of managing each capability separately, developers can use a Foundry resource and projects to work with model deployments, tools, connected data, agents, and access settings.

**Simple example:** A company builds a pharmacy-policy assistant. Its Foundry project contains the AI configuration, relevant connections, and model deployment needed for development.

## 2. Resource vs. project

| Term | Plain English | Example |
|---|---|---|
| Azure resource group | Organizational container for Azure resources | `moduleone` (lab) |
| Foundry resource | Parent Azure resource supporting AI functionality and access | `AIVidaproject` (lab) |
| Foundry project | Workspace for a particular AI solution | `proj-default` (lab) |
| Model deployment | A configured, callable instance of a model | `gpt-5.2` deployment |
| Endpoint | Network address the application calls | Set in deployment/project details |

One Foundry resource can support multiple projects, and a project belongs to one parent Foundry resource. A deployment exposes an existing model for inference; it does not train the underlying model.

## 3. Portal vs. SDK vs. API vs. Toolkit

| Tool | What it is | When to use |
|---|---|---|
| **Foundry Portal** | Browser-based interface | Provision resources, compare/deploy models, test in playgrounds |
| **Foundry SDK** | Programming libraries | Build code that interacts with Foundry projects, agents, or assets |
| **OpenAI-compatible API/SDK** | Model request interface and convenience libraries | Send prompts and receive responses from a compatible deployment |
| **Foundry Tools SDKs** | Service-specific libraries | Speech, translation, extraction, and similar specialized features |
| **Foundry Toolkit for VS Code** | Editor extension | Explore Foundry resources and model playgrounds from VS Code |

**Memory trick:** Portal = click; SDK = write code; API = communication contract; endpoint = address; toolkit = development convenience.

## 4. Models vs. agents vs. tools vs. knowledge

- **Model:** Pretrained system that takes an input and produces an output.
- **Agent:** An application component combining a model, instructions, and optionally tools and workflow logic.
- **Tool:** External capability (for example, searching documents or calling an API) accessible to an agent.
- **Knowledge:** Data sources that provide relevant factual context. A model is not automatically connected to internal documents.

**Example:** A model can explain what an insurance claim is. A properly designed agent with authorized tools could locate a fictional claim, validate fields against policies, and ask a human to approve a decision.

## 5. How inference works

1. A user writes a question.
2. The app or playground packages the question and any relevant instructions.
3. It sends a request to the deployed model's endpoint.
4. Azure runs the pretrained model and returns generated text.
5. The application presents the response.

**Model inference is not model training.** Training changes model parameters; inference uses an existing model.

## 6. Instructions vs. user prompts

- **Instructions/system message:** Defines how the assistant should behave across user queries.
- **User input/prompt:** Contains a particular question or task.

Example:

```text
Instructions: You explain AI software concepts clearly. Avoid unsupported claims.
User: Explain the difference between an API and SDK in two sentences.
```

A good evaluation tests both the quality of the answer and whether it followed instructions.

## 7. Authentication basics

To call a model from a Python application, developers typically need:

1. The correct endpoint URL.
2. The **deployment name** used as the model identifier in requests.
3. A supported credential, ideally a Microsoft Entra ID identity in production.

Use environment variables, approved identity management, and least-privilege roles. **Never commit credentials or API keys to GitHub.** Being logged in to the portal or VS Code does not guarantee a standalone Python process is authenticated.

## 8. What did I do in Module 1?

**Completed in the cloud and editor:**

- Created the Azure Foundry project and parent resource.
- Deployed GPT-5.2 as a Global Standard model deployment.
- Tested the deployed model in the portal playground.
- Connected Foundry Toolkit in VS Code to the project.
- Selected GPT-5.2 in VS Code and generated a Python Agent Framework code sample.

**Not yet established by this lab:** successful independent execution of the generated Python integration, connection to real pharmacy data, retrieval-augmented generation, ML training, or production deployment.

## 9. Essential terms for AI-103

- **Deployment:** Configuring an existing model to serve requests.
- **Inference:** Asking the deployed model for an output.
- **Streaming:** Returning output incrementally as it is generated.
- **Global Standard:** A usage-based deployment type for supported models; check Azure prices, quotas, and processing-location rules.
- **SDK:** A set of libraries that simplify API access.
- **RBAC:** Role-based access control; controls what Azure identities can do.
- **Microsoft Entra ID:** Identity platform used for authentication and authorization.

## 10. Questions I should be able to answer

1. What is the difference between a Foundry resource and project?
2. How is a deployment different from training a model?
3. Why would a developer use the portal before an SDK?
4. Why does a Python program need an endpoint, deployment name, and identity?
5. Why is an agent with `tools=None` different from an agent that can call APIs?

## 11. Module 1 completion summary

This module established the environment and terminology for Azure AI development. The most useful professional takeaway is being able to navigate model deployments and playgrounds and understand how they connect to programmatic applications. The next portfolio milestone should demonstrate a verified Python API call and measurable model evaluation, not just course completion.

### Useful official links

- https://learn.microsoft.com/en-us/training/paths/develop-generative-ai-apps/
- https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/get-started-projects-vs-code
- https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview
