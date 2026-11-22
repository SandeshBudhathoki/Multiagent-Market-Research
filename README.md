# Multi-Agent Market Research App

## Overview
This project is a simple AI-powered market research application built with Python and Streamlit. It takes a company or industry as input, searches the web for relevant information, and generates a market research report using multiple AI agents.
The main goal of this project is to understand how different AI agents can work together to complete a task.


## How It Works
The application uses four agents:
1.Orchestrator Agent – Manages the workflow and connects the other agents.
2.Researcher Agent – Searches the web and collects relevant information using Tavily.
3.Analyst Agent – Uses the collected research to prepare a structured market research report.
4.Critic Agent – Reviews the report and provides feedback if improvements are needed.

The workflow is:

User Input → Researcher → Analyst → Critic → Final Report

If the critic finds issues, the orchestrator asks the AI to revise the report once before returning the result.

## Features

- Research a company or industry.
- Collect information from web search results.
- Generate a structured market research report.
- Review the report and make one revision when needed.
- Display the report in the Streamlit interface.
- Download the report as a Markdown file.
- Clear the previous search and start a new one.

## Technologies Used
- Python
- Streamlit
- Groq API
- Tavily Search API
- OpenAI Python SDK
- python-dotenv

## Project Structure

AI Traineeship/
│
├── app.py
├── requirements.txt
├── README.md
├── sample_output.md
├── .env
├── .env.example
├── .gitignore
│
├── agents/
│   ├── __init__.py
│   ├── researcher.py
│   ├── analyst.py
│   ├── critic.py
│   └── orchestrator.py
│
├── services/
│   ├── __init__.py
│   ├── llm.py
│   └── web_search.py

```
## Setup and Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root directory and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-20b
TAVILY_API_KEY=your_tavily_api_key
```

You can use `.env.example` as a reference.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## Report Sections

The generated report includes:

- Market Overview
- Main Competitors (up to two, when relevant)
- Key Findings
- Sources
- Missing Information

## Notes
- The quality of the report depends on the information returned by the web search results.
- The critic reviews the report using the same collected research data. It does not independently verify information from external sources.
