import json, csv, os
from scenarios import SCENARIOS
from openai import OpenAI

# Uses your OPENAI_API_KEY from the environment
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def call_model(prompt: str) -> str:
    """Call the OpenAI chat model and return its text output."""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content

def build_prompt(text: str) -> str:
    """Build the instruction prompt for a given scenario."""
    return (
        "You are a biomedical reasoning assistant.\n\n"
        "1. Classify the MAIN relationship as one of: "
        '"causal", "correlation", "spurious", or "not_applicable".\n'
        "2. Classify the OVERALL scenario as either: "
        '"plausible" or "impossible" given current biomedical knowledge.\n\n'
        "Return your answer STRICTLY as a JSON object with exactly these keys:\n"
        '- "causal_judgment"\n'
        '- "plausibility_judgment"\n'
        '- "explanation"\n\n'
        "Scenario:\n"
        f'\"\"\"{text}\"\"\"'
    )

def parse(json_raw: str):
    """Try to extract and parse JSON from the model's output."""
    try:
        start = json_raw.find("{")
        end = json_raw.rfind("}")
        json_clean = json_raw[start:end+1]
        return json.loads(json_clean)
    except Exception:
        return {
            "causal_judgment": "unknown",
            "plausibility_judgment": "unknown",
            "explanation": json_raw,
        }

def main():
    rows = []
    for s in SCENARIOS:
        prompt = build_prompt(s["text"])
        raw = call_model(prompt)
        parsed = parse(raw)

        row = {
            "id": s["id"],
            "text": s["text"],
            "causal_label": s["causal_label"],
            "plausibility_label": s["plausibility_label"],
            "causal_judgment": parsed.get("causal_judgment", "unknown"),
            "plausibility_judgment": parsed.get("plausibility_judgment", "unknown"),
            "explanation": parsed.get("explanation", "")
        }
        rows.append(row)

    if rows:
        fieldnames = list(rows[0].keys())
    else:
        fieldnames = []

    with open("results.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        if rows:
            w.writerows(rows)

    print("Done! Results saved to results.csv")

if __name__ == "__main__":
    main()
