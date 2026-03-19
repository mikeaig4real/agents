"""Orchestration layer for Module 3 crew app."""

from crews import build_debate_crew, build_engineering_crew, build_financial_crew


def run_crew(selection: str, prompt: str) -> str:
    """Route user prompt to the selected crew and return output."""
    selection = selection.strip().lower()

    if selection == "debate":
        crew = build_debate_crew(prompt)
    elif selection == "engineering":
        crew = build_engineering_crew(prompt)
    elif selection == "financial":
        crew = build_financial_crew(prompt)
    else:
        raise ValueError("Unsupported crew selection. Use Debate, Engineering, or Financial.")

    result = crew.kickoff()
    return str(result)
