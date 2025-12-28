# Causal & Hallucination Probe for Biomedical LLMs

This project evaluates large language models on:
- Causal reasoning (causal vs correlation vs spurious)
- Hallucination detection via biomedical plausibility checks

## Features
- Synthetic benchmark scenarios
- Reproducible evaluation pipeline
- Interactive Gradio interface

## Run locally
```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your_key_here"
python3 app.py
