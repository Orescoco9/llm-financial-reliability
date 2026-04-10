# 💰 LLM Financial Risk Evaluation System

A local AI-powered system that evaluates financial risk using structured outputs and automated scoring.

## 🚀 Overview

This project uses a locally hosted LLM (via Ollama) to:
- Analyze financial data
- Generate structured risk assessments (JSON)
- Evaluate model accuracy against predefined rules

## 🧠 Features

- ✅ Local LLM (no API costs)
- ✅ Structured JSON outputs
- ✅ Automated evaluation pipeline
- ✅ Accuracy scoring system
- ✅ Confidence consistency checks

## 🛠 Tech Stack

- Python
- Ollama (Llama 3.1)
- Requests
- Pandas

## 📊 Results

| Metric | Value |
|------|------|
| Accuracy | 80% – 100% (depending on dataset) |
| Model | Llama 3.1 (local via Ollama) |
| Evaluation Type | Rule-based + tolerance scoring |

### Key Findings

- LLM outputs vary on boundary conditions (e.g. debt_ratio = 0.7)
- Strict rule-based evaluation underestimates model performance
- Confidence scores may not always align with classification (inconsistency observed)

This demonstrates the importance of **evaluation design in AI systems**, not just model quality.
