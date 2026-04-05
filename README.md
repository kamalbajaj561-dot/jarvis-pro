# JARVIS PRO

A modular Python assistant for voice control, automation, coding support, and startup strategy workflows.

## Core pipeline

`Voice → Command → Rule-based intent override → AI intent fallback → Action router → Execution → Smart response`

## Key improvements

- Hybrid intent detection with hard-rule priority and AI fallback
- Action modules for apps, web, system control, WhatsApp, coding and business
- Explicit confirmation gate for risky actions
- Lightweight conversation memory

## Project structure

```text
jarvis/
├── main.py
├── voice/
├── ai/
├── actions/
├── config/
└── utils/
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Optional env vars:

```bash
export GROQ_API_KEY="your_key"
export GROQ_MODEL="llama-3.3-70b-versatile"
export INRT_WALLET_PATH="$HOME/projects/INRT-Wallet"
```

## Usage

```bash
python main.py --mode cli --command "open my project"
python main.py --mode voice
```
