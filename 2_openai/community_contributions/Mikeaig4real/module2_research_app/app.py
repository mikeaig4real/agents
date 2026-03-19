"""Gradio UI for the Module 2 research app."""

import gradio as gr
from dotenv import load_dotenv

from manager import ResearchManager

load_dotenv(override=True)


async def run_research(query: str):
    """Stream progress messages and final report."""
    async for message in ResearchManager().run(query):
        yield message


with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Module 2 Deep Research App")
    query_box = gr.Textbox(label="Research topic", placeholder="Example: Compare SOC2 automation platforms")
    run_button = gr.Button("Run research", variant="primary")
    output = gr.Markdown(label="Progress and report")

    run_button.click(fn=run_research, inputs=query_box, outputs=output)
    query_box.submit(fn=run_research, inputs=query_box, outputs=output)


if __name__ == "__main__":
    ui.launch(inbrowser=True)
