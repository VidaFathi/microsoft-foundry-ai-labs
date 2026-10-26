# Module 1 Lab Journal

## Objective
Create an Azure-based AI development environment and verify model inference in the portal and VS Code playground.

## Lab details

| Item | Value |
|---|---|
| Azure resource group | `moduleone` |
| Foundry resource | `AIVidaproject` |
| Project | `proj-default` |
| Region | Canada Central |
| Model | GPT-5.2 |
| Deployment type | Global Standard |
| IDE | Visual Studio Code with Foundry Toolkit |

## Completed milestones

- [x] Created a Foundry resource/project through the portal.
- [x] Fixed the relevant Foundry project role assignment issue.
- [x] Deployed a GPT-5.2 model.
- [x] Used a model playground to test prompt instructions and responses.
- [x] Installed the Foundry Toolkit extension and connected the Azure project in VS Code.
- [x] Used the VS Code model playground with GPT-5.2.
- [x] Generated a Python Agent Framework code sample from the editor.
- [ ] Verified running the Python code independently and receiving a remote model response.

## Technical observations

- Using a portal or VS Code playground is not the same as shipping an app.
- A deployed model can be accessed using an endpoint, deployment name, and valid credential.
- Agent configuration with no external tools is effectively a model-based chat assistant, not a fully integrated business workflow.
- A public repository should contain sanitized source and screenshots, not keys or confidential data.

## Reflection

The exercise connected familiar engineering tools (VS Code, Git, Python, Azure) to a generative AI platform. My next engineering deliverable should demonstrate a fully tested model API call, automation, and evaluation with measurable acceptance criteria.
