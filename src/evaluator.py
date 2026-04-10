import json

def evaluate():
    with open("../results/output.json", "r") as f:
        data = json.load(f)

    correct = 0
    total = len(data)

    for item in data:
        expected = item["expected"].lower()
        answer = item["model_answer"].lower()

        if expected in answer:
            item["score"] = "correct"
            correct += 1
        else:
            item["score"] = "incorrect"

    accuracy = (correct / total) * 100

    print(f"Accuracy: {accuracy:.2f}%")

    with open("../results/evaluated.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    evaluate()