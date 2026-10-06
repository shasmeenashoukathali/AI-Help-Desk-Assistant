# AI Employee Helpdesk Assistant

An AI-powered IT helpdesk assistant built with Python, Streamlit, and Ollama using a locally running Llama 3.2 model.

The application allows employees to describe IT problems in natural language, including spelling mistakes, abbreviations, and informal sentences. The local LLM interprets the issue and provides structured troubleshooting guidance.

## Features

- Accepts IT problems in natural language
- Understands basic spelling mistakes and informal user input
- Identifies the problem category and priority
- Suggests possible causes
- Generates step-by-step troubleshooting guidance
- Advises when the issue should be escalated to IT support
- Uses a locally running LLM through Ollama
- Does not require a cloud AI API key

## Technologies Used

- Python
- Streamlit
- Ollama
- Llama 3.2 3B
- Local LLM inference

## How It Works

1. The employee enters an IT-related problem.
2. The application sends the problem with structured instructions to the locally running LLM.
3. The LLM interprets the user's description.
4. The assistant returns the problem category, priority, possible cause, troubleshooting steps, and escalation guidance.

## Run Locally

Install the required Python packages:

```bash
pip install -r requirements.txt