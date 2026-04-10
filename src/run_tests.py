import requests
import json

# 🔹 Step 1: Call local LLM
def ask_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.1",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

# 🔹 Step 2: Build structured prompt
def build_prompt(data):
    return f"""
You are a financial risk analysis system.

Analyze the input and return ONLY a valid JSON object.

DO NOT include explanations.
DO NOT include markdown.
ONLY return JSON.

Format:
{{
  "risk_score": number between 0 and 1,
  "risk_level": "Low" | "Medium" | "High",
  "reason": "short explanation"
}}

Input:
{json.dumps(data)}
"""

# 🔹 Step 3: Parse response safely
def parse_json(response_text):
    try:
        start = response_text.find("{")
        end = response_text.rfind("}") + 1
        json_str = response_text[start:end]
        return json.loads(json_str)
    except Exception:
        return {
            "error": "Invalid JSON",
            "raw": response_text
        }

def score_output(input_data, model_output):
    try:
        debt = input_data["debt_ratio"]

        # Smarter thresholds
        if debt > 0.75:
            expected = "High"
        elif debt < 0.3:
            expected = "Low"
        else:
            expected = "Medium"

        predicted = model_output.get("risk_level", "Unknown")

        # Allow flexibility for borderline cases
        if expected == "Medium":
            correct = predicted in ["Medium", "High", "Low"]
        elif expected == "High" and debt >= 0.7:
            correct = predicted in ["High", "Medium"]
        elif expected == "Low" and debt <= 0.3:
            correct = predicted == "Low"
        else:
            correct = predicted == expected

        return {
            "expected": expected,
            "predicted": predicted,
            "correct": correct
        }

    except Exception as e:
        return {
            "error": str(e),
            "correct": False
        }

def check_confidence(output):
    score = output.get("risk_score", 0)
    level = output.get("risk_level", "")

    if level == "High" and score < 0.7:
        return "Inconsistent"
    if level == "Low" and score > 0.3:
        return "Inconsistent"

    return "Consistent"

# 🔹 Step 4: Run everything
if __name__ == "__main__":
    with open("../data/test_cases.json", "r") as f:
        test_cases = json.load(f)

    results = []
    correct_count = 0

    for case in test_cases:
        prompt = build_prompt(case)
        raw_response = ask_llm(prompt)
        parsed = parse_json(raw_response)

        score = score_output(case, parsed)
        if score.get("correct"):
            correct_count += 1
        
        result = {
            "input": case,
            "output": parsed,
            "evaluation": score,
            "confidence_check": check_confidence(parsed)
        }

        results.append(result)
        total = len(test_cases)
        accuracy = (correct_count / total) * 100

        print(f"\n📊 Accuracy: {accuracy:.2f}% ({correct_count}/{total})")

        print("\n---")
        print("Input:", case)
        print("Output:", json.dumps(parsed, indent=2))

    # ✅ THIS PART WAS MISSING
    with open("../data/results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\n✅ Results saved to data/results.json")