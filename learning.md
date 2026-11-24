# LangChain Learning Notes

This file tracks the concepts learned while building the LangChain Research Agent.

# Lesson 1 — Models, Prompts, and Chains

## 1. What is LangChain?

LangChain is a framework for building applications around language models.

It helps connect LLMs with:

- Prompts
- Tools
- External APIs
- Databases
- Documents
- Retrieval systems
- Application logic

A useful mental model is:

```text
LLM = brain

Tools = capabilities

LangChain = framework connecting the pieces
```

---

## 2. Chat Model

A chat model represents the language model our application communicates with.

Example:

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-4.1-mini"
)
```

Conceptually:

```text
Python Application
       ↓
   ChatOpenAI
       ↓
   OpenAI API
       ↓
      LLM
```

`ChatOpenAI` is not itself the language model.

It is LangChain's interface for communicating with an OpenAI chat model.

---

## 3. `invoke()`

`invoke()` runs a LangChain component once.

Example:

```python
response = model.invoke(
    "Explain what an API is."
)
```

Conceptually:

```text
input
  ↓
invoke()
  ↓
model
  ↓
response
```

The returned value is normally a message object rather than a plain Python string.

The text can be accessed with:

```python
response.content
```

---

## 4. Prompt Templates

Hard-coded prompts are difficult to reuse.

Instead of:

```python
model.invoke(
    "Explain Python to a beginner."
)
```

we can create a reusable template:

```python
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} to a {level} learner."
)
```

Variables can then be provided dynamically:

```python
{
    "topic": "Python",
    "level": "beginner"
}
```

This allows the same prompt structure to work with many inputs.

---

## 5. Chains

LangChain components can be connected together.

Example:

```python
chain = prompt | model
```

The `|` operator can be read as:

> Take the output from the component on the left and pass it to the component on the right.

Conceptually:

```text
input
  ↓
prompt
  ↓
model
  ↓
response
```

Example:

```python
response = chain.invoke(
    {
        "topic": "RAG",
        "level": "beginner"
    }
)
```

---

## 6. Runnables

Many LangChain components behave as Runnables.

A Runnable is something that can receive input, perform some operation, and return output.

Examples include:

```text
Prompt
Model
Retriever
Output parser
Chain
```

This common interface is what allows components to be connected.

---

## 7. Environment Variables

Secrets such as API keys should not be written directly into Python source code.

Bad:

```python
api_key = "sk-secret-key"
```

Better:

```text
.env
```

containing:

```text
OPENAI_API_KEY=...
```

Python can load these environment variables using `python-dotenv`.

The `.env` file must be included in `.gitignore`.

---

## 8. `.env.example`

`.env.example` documents the environment variables required by the application without exposing actual secrets.

Example:

```text
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4.1-mini
```

This file can safely be committed.

---

## 9. Virtual Environments

A Python virtual environment keeps dependencies isolated from other projects.

Create one with:

```bash
python -m venv .venv
```

This creates:

```text
project/
└── .venv/
```

The `.venv` directory should not be committed to Git.

---

# Lesson 1 Mental Model

Our current application is:

```text
User
 ↓
Python input()
 ↓
Dictionary
 ↓
Prompt Template
 ↓
ChatOpenAI
 ↓
OpenAI Model
 ↓
AIMessage
 ↓
response.content
 ↓
Terminal
```

The most important line currently is:

```python
chain = prompt | model
```

---

# Questions I Should Be Able to Answer

## What is `ChatOpenAI`?

A LangChain integration that lets our application communicate with OpenAI chat models.

## What does `invoke()` do?

Runs a LangChain component once with the supplied input.

## Why use a prompt template?

It allows prompts to be reusable and accept dynamic variables.

## What does `prompt | model` mean?

Take the output produced by the prompt component and pass it into the model.

## Why use `.env`?

To keep secrets such as API keys outside source code.

## Why use `.gitignore`?

To prevent secrets, virtual environments, caches, and other unwanted files from being committed.

## Why use a virtual environment?

To isolate this project's Python dependencies.

---

# New Vocabulary

- LLM
- LangChain
- Chat model
- Prompt template
- Runnable
- Chain
- `invoke()`
- Environment variable
- Virtual environment

---

# Current Architecture

```text
Input
  ↓
Prompt
  ↓
Model
  ↓
Output
```

In future lessons this will evolve into:

```text
                 Agent
                   ↓
        ┌──────────┼──────────┐
        ↓          ↓          ↓
      Search    Calculator    RAG
        ↓          ↓          ↓
        └──────────┼──────────┘
                   ↓
                Answer
```