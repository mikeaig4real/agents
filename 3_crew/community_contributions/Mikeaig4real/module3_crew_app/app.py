"""Gradio UI for Module 3 crew workflows."""

import gradio as gr
from dotenv import load_dotenv

from orchestrator import run_crew

load_dotenv(override=True)


def run(selection: str, prompt: str) -> str:
    """Execute selected crew and return the response."""
    if not prompt.strip():
        return "Please provide a prompt."
    try:
        return run_crew(selection, prompt)
    except Exception as exc:
        return f"Execution failed: {exc}"


with gr.Blocks(theme=gr.themes.Default(primary_hue="indigo")) as ui:
    gr.Markdown("# Module 3 Crew App")
    selection = gr.Radio(
        choices=["Debate", "Engineering", "Financial"],
        value="Debate",
        label="Crew",
    )
    prompt = gr.Textbox(label="Prompt", placeholder="Example: Should we adopt RAG for support operations?")
    run_button = gr.Button("Run", variant="primary")
    output = gr.Markdown(label="Result")

    run_button.click(fn=run, inputs=[selection, prompt], outputs=output)
    prompt.submit(fn=run, inputs=[selection, prompt], outputs=output)


if __name__ == "__main__":
    ui.launch(inbrowser=True)
