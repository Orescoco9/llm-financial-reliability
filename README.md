## LLM Financial Risk Evaluation System

A local AI-powered system for evaluating financial risk using structured prompting, deterministic scoring, and automated evaluation of LLM outputs.

---

## Overview

This project explores how large language models behave in structured financial classification tasks. It uses a locally hosted LLM (via Ollama) to generate risk assessments from financial inputs and evaluates the consistency and reliability of its outputs.

The system focuses on **LLM reliability, structured output generation, and evaluation design**.

---

## System Architecture

Financial Data Input
↓
Prompt Engineering Layer
↓
Local LLM (Ollama - Llama 3.1)
↓
Structured JSON Output Parser
↓
Evaluation Engine (Scoring Logic)
↓
Accuracy + Results Report

---

## 📁 Project Structure

llm-financial-reliability/
│
├── data/
│ ├── test_cases.json # Input dataset
│ └── results.json # Generated outputs
│
├── src/
│ └── run_tests.py # Main evaluation pipeline
│
├── requirements.txt
└── README.md


---

## Features

- ✅ Fully local LLM execution (no API costs)
- ✅ Structured JSON output generation
- ✅ Automated evaluation pipeline
- ✅ Accuracy scoring system
- ✅ Confidence consistency checks
- ✅ Dataset-driven testing framework

---

## Tech Stack

- Python
- Ollama (Llama 3.1) 
- Requests
- Pandas

---

## ▶️ How to Run

 1. Install dependencies
pip install -r requirements.txt

2. Start local LLM (Ollama)
ollama run llama3.1

3. Run evaluation system
py src/run_tests.py

---
## 📊 Results

| Metric | Value |
|------|------|
| Accuracy | 80% – 100% (depending on dataset) |
| Model | Llama 3.1 (local via Ollama) |
| Evaluation Type | Rule-based + tolerance scoring |

---
## Key Findings

- LLM outputs vary on boundary conditions (e.g. debt_ratio = 0.7)
- Strict rule-based evaluation can misclassify borderline cases
- Model confidence does not always perfectly align with classification
- Evaluation design strongly impacts perceived model performance

---
## Why This Project Matters

Large Language Models can produce inconsistent outputs depending on prompt structure and edge cases.

This project demonstrates:
How to evaluate LLM reliability in structured tasks
How to design scoring systems for AI outputs
The gap between probabilistic reasoning and deterministic evaluation
Real-world challenges in AI system validation

This reflects core problems in AI engineering and LLM evaluation design.

---
## Author
Ore Adegbite
