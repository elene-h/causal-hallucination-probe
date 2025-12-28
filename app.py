import os
import json
from openai import OpenAI
import gradio as gr

# Use your OpenAI API key from the environment
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


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


def parse_output(raw_text: str):
    """Try to extract and parse JSON from the model's output."""
    raw_text = raw_text.strip()
    start = raw_text.find("{")
    end = raw_text.rfind("}")
    if start != -1 and end != -1:
        raw_text = raw_text[start : end + 1]

    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError:
        data = {
            "causal_judgment": "unknown",
            "plausibility_judgment": "unknown",
            "explanation": f"Could not parse JSON. Raw output: {raw_text}",
        }
    return data


def analyze_scenario(text: str):
    """Main function called by the UI."""
    text = text.strip()
    if not text:
        return "–", "–", "Please enter a scenario.", ""

    if not os.environ.get("OPENAI_API_KEY"):
        return "–", "–", "Error: OPENAI_API_KEY is not set.", ""

    prompt = build_prompt(text)

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        raw = response.choices[0].message.content
        parsed = parse_output(raw)

        causal = parsed.get("causal_judgment", "unknown")
        plaus = parsed.get("plausibility_judgment", "unknown")
        expl = parsed.get("explanation", "")

        return causal, plaus, expl, raw

    except Exception as e:
        return "–", "–", f"Error while calling the model: {e}", ""


# ---- Gradio interface ----
with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Causal & Hallucination Probe for Biomedical LLMs

        Enter a biomedical / clinical scenario below.
        The model will classify:

        - **Causal judgment:** causal / correlation / spurious / not_applicable  
        - **Plausibility:** plausible vs impossible  
        - **Explanation:** short reasoning
        """
    )

    # Make input and outputs side-by-side
    with gr.Row():
        # Left column: user input + button
        with gr.Column(scale=1):
            scenario_in = gr.Textbox(
                label="Scenario",
                placeholder="Type or paste a clinical / biomedical scenario here...",
                lines=10,
            )
            analyze_btn = gr.Button("Analyze scenario")

        # Right column: model outputs
        with gr.Column(scale=1):
            causal_out = gr.Textbox(label="Causal judgment", interactive=False)
            plaus_out = gr.Textbox(label="Plausibility judgment", interactive=False)
            expl_out = gr.Textbox(
                label="Explanation (model)",
                lines=10,
                interactive=False,
            )
            raw_out = gr.Textbox(
                label="Raw model output (debug)",
                lines=6,
                interactive=False,
                visible=False,  # change to True if you want to see it
            )

    analyze_btn.click(
        fn=analyze_scenario,
        inputs=scenario_in,
        outputs=[causal_out, plaus_out, expl_out, raw_out],
    )

if __name__ == "__main__":
    demo.launch()
