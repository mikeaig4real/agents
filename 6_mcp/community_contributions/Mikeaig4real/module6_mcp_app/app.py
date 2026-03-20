"""Gradio app for Module 6 MCP exercise."""

import asyncio
import gradio as gr
from dotenv import load_dotenv

from client_agent import run_mcp_prompt

load_dotenv(override=True)


def run_sync(prompt: str) -> str:
    """Sync wrapper for MCP async runner."""
    return asyncio.run(run_mcp_prompt(prompt))


with gr.Blocks(theme=gr.themes.Default(primary_hue="violet")) as ui:
    gr.Markdown("# Module 6 MCP App")
    prompt = gr.Textbox(label="Prompt", placeholder="Give me a headline about AI infrastructure today")
    button = gr.Button("Run MCP agent", variant="primary")
    output = gr.Markdown(label="Result")
    button.click(fn=run_sync, inputs=prompt, outputs=output)
    prompt.submit(fn=run_sync, inputs=prompt, outputs=output)

if __name__ == "__main__":
    ui.launch(inbrowser=True)
