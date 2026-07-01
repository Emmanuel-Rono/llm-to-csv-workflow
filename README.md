# LLM CSV Workflow

`llm-csv-workflow` is a small but intentional Applied AI engineering project focused on one core idea: build LLM-powered workflows with clean software design from day one.

This project is the first step in a broader journey toward becoming an Applied AI Engineer. Instead of starting with heavy frameworks, it starts with the fundamentals:

- loading configuration safely
- isolating external API dependencies
- calling an LLM through the OpenAI Python SDK
- keeping the codebase simple, readable, and extensible

## Why this project exists

Many early AI projects become hard to maintain because they mix secrets, business logic, and vendor-specific code in one file. This project takes the opposite approach.

The goal is to practice:

- clean project structure
- separation of concerns
- configuration management
- API integration discipline
- early SOLID-oriented thinking

It is intentionally small now so that the design stays understandable while the project grows.

## Current functionality

The current version:

- loads `OPENAI_API_KEY` from a local `.env` file
- validates that the API key exists before running
- creates an OpenAI client explicitly with the loaded key
- sends a test request using the Responses API
- prints the model output to the terminal

## Project structure

```text
llm-csv-workflow/
├── .env
├── .gitignore
├── README.md
├── data/
├── outputs/
├── src/
│   ├── config.py
│   └── main.py
└── tests/
```

## Design decisions

### `src/config.py`

Responsible for:

- loading the `.env` file
- reading environment variables
- validating required configuration

This keeps configuration concerns out of the application entrypoint.

### `src/main.py`

Responsible for:

- starting the application
- creating the OpenAI client
- sending the request
- displaying the response

This keeps the entrypoint focused and easy to reason about.

## Engineering principles

This project is being built with the following principles in mind:

- **Single Responsibility**: each file should have one clear purpose
- **Dependency Awareness**: vendor-specific SDK usage should stay isolated
- **Explicit Configuration**: secrets should come from environment variables, not hardcoded values
- **Incremental Design**: start simple, then refactor as responsibilities become clearer
- **Learn by Building**: understand each layer instead of hiding complexity behind frameworks too early

## Tech stack

- `Python`
- `OpenAI Python SDK`
- `python-dotenv`

## Setup

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install openai python-dotenv
```

### 3. Create a `.env` file

Add this in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

## Run the project

From the project root:

```powershell
python src/main.py
```

## Current limitations

This is still an early foundation project. It does not yet include:

- CSV input/output processing
- structured response validation
- error handling for API failures
- tests
- domain models
- a dedicated client abstraction

Those are planned next as the project evolves into a stronger engineering artifact.

## Planned evolution

Next steps for this project:

- read prompts from a CSV file
- write outputs back to CSV
- introduce response schemas and validation
- separate LLM client logic into its own module
- add tests for configuration and workflow behavior
- compare raw SDK usage with a more abstracted design

## Portfolio value

This project represents an important part of my Applied AI engineering journey:

- starting with fundamentals instead of shortcuts
- prioritizing code quality alongside AI capability
- building systems that are understandable, testable, and maintainable
- learning AI integration as a software engineering discipline

It is a small project by scope, but an intentional one by design.
