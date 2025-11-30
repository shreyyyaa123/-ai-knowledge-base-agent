# 🤖 AI Knowledge Base Agent

## Overview
An intelligent AI agent that answers employee questions about company policies and benefits using natural language processing. Built for the 48-Hour AI Agent Development Challenge.

## Problem Statement
Employees often struggle to find quick answers to HR policy questions. This agent provides instant, accurate responses by searching through company documents.

## Features
- 🔍 Natural Language Search
- 📄 Source Citations  
- 💬 Conversational Interface
- ⚡ Fast Responses (Powered by Groq AI)

## Tech Stack
- **AI Model**: Groq (Llama 3.3 70B)
- **Framework**: Streamlit
- **Language**: Python 3.10+

## Installation

### Prerequisites
- Python 3.10+
- Groq API key

### Setup Steps
```bash
git clone https://github.com/shreyyyaa123/-ai-knowledge-base-agent.git
cd -ai-knowledge-base-agent
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env` file:
```
GROQ_API_KEY=your-key-here
```

Run the app:
```bash
streamlit run app.py
```

## Usage Examples
- "How many sick leave days do I get?"
- "What is the work from home policy?"
- "Tell me about health insurance benefits"

## Project Structure
```
-ai-knowledge-base-agent/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── documents/
    ├── company_policy.txt
    └── benefits.txt
```

## Current Limitations
- Only supports .txt files
- Requires internet connection
- English language only

## Future Enhancements
- Multi-format support (PDF, DOCX)
- Multi-language support
- Voice interface
- Analytics dashboard
- Vector database integration

## Developer Information
**Name**: Shreyaa  
**Challenge**: 48-Hour AI Agent Development Challenge  
**Category**: Knowledge Base Agent  
**Date**: November 2024

## Links
- **Demo**: [Will add after deployment]
- **GitHub**: https://github.com/shreyyyaa123/-ai-knowledge-base-agent

---

**Built with ❤️ for the AI Agent Development Challenge 2024**
