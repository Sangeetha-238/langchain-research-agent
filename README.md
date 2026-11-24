# LangChain Research Agent

A hands-on project for learning LangChain, tool calling, agents, RAG, and LangGraph by progressively building an AI research assistant.

## Project Goal

The goal of this project is to learn how to build production-style LLM applications rather than simply calling a language model.

The project will evolve from a basic LangChain pipeline into an agent capable of:

- Using multiple tools
- Calling external APIs
- Performing calculations
- Retrieving information from documents
- Using Retrieval-Augmented Generation (RAG)
- Producing structured outputs
- Maintaining workflow state
- Running multi-step workflows with LangGraph

## Current Architecture

Lesson 1 introduces a basic LangChain pipeline:

```text
User Input
    ↓
Prompt Template
    ↓
Chat Model
    ↓
AI Response
```

In LangChain code:

```python
chain = prompt | model
```

## Current Features

- OpenAI model integration through LangChain
- Environment-variable configuration
- Reusable prompt templates
- LangChain Runnable composition
- Interactive command-line interface
- Basic error handling

## Project Roadmap

### Phase 1 — LangChain Fundamentals

- [x] Project setup
- [x] Virtual environment
- [x] Model invocation
- [x] Prompt templates
- [x] Basic chains
- [ ] Messages
- [ ] Structured output

### Phase 2 — Tools and Agents

- [ ] Create custom tools
- [ ] Tool calling
- [ ] Multiple tools
- [ ] Agent creation
- [ ] External API integration

### Phase 3 — RAG

- [ ] Document loading
- [ ] Text splitting
- [ ] Embeddings
- [ ] Vector stores
- [ ] Retrievers
- [ ] Retrieval-Augmented Generation

### Phase 4 — Agentic RAG

- [ ] Combine agents and retrieval
- [ ] Dynamic tool selection
- [ ] Research workflow

### Phase 5 — LangGraph

- [ ] State management
- [ ] Nodes and edges
- [ ] Conditional routing
- [ ] Loops
- [ ] Multi-step workflows

### Phase 6 — Portfolio Version

- [ ] Web interface
- [ ] Improved error handling
- [ ] Logging
- [ ] Source citations
- [ ] Deployment
- [ ] Architecture documentation

## Project Structure

```text
langchain-research-agent/
├── .env.example
├── .gitignore
├── LEARNING.md
├── README.md
├── TASKS.md
├── main.py
└── requirements.txt
```

## Requirements

- Python 3.10+
- Git
- OpenAI API key

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd langchain-research-agent
```

Create a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Copy:

```text
.env.example
```

to:

```text
.env
```

Then provide your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4.1-mini
```

Never commit the `.env` file.

## Running the Application

Run:

```bash
python main.py
```

Example:

```text
==================================================
LangChain Learning Assistant
==================================================
Topic: RAG
Level (beginner/intermediate/advanced): beginner
```

The application asks the model to respond with:

```text
Definition:
Analogy:
Example:
Quiz Question:
```

## LangChain Concepts Used

### Chat Model

The chat model represents the LLM used by the application.

```python
model = ChatOpenAI(...)
```

### Prompt Template

Prompt templates allow prompts to contain dynamic values.

```python
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} to a {level} learner."
)
```

### Invoke

`invoke()` executes a LangChain component once.

```python
response = chain.invoke(...)
```

### Chain

LangChain components can be connected using the pipe operator:

```python
chain = prompt | model
```

Conceptually:

```text
input → prompt → model → output
```

## Why This Project Exists

This repository is intentionally being built incrementally.

Instead of following isolated tutorials, each lesson adds another capability to the same application. The final result will demonstrate practical experience with modern LLM application architecture.

## Future Architecture

The final system is expected to resemble:

```text
                    User
                      ↓
                  AI Agent
                      ↓
          ┌───────────┼───────────┐
          ↓           ↓           ↓
       Search     Calculator     RAG
        Tool         Tool        Tool
          ↓           ↓           ↓
          └───────────┼───────────┘
                      ↓
                  LangGraph
                      ↓
             Structured Report
```

## Status

🚧 Work in progress — currently completing LangChain Lesson 1.