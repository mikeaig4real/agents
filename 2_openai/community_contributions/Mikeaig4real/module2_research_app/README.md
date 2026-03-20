# Module 2 Research App

This implementation follows the deep-research module pattern:

- one sub-agent per file
- one converged lead agent
- one manager file that runs the lead agent
- one Gradio app file for UI

## Structure
- `sub_agents/planner_agent.py`
- `sub_agents/search_agent.py`
- `sub_agents/writer_agent.py`
- `sub_agents/email_agent.py`
- `lead_agent.py` (converged agent)
- `manager.py` (execution)
- `app.py` (Gradio interface)

## Run
```bash
python 2_openai/community_contributions/Mikeaig4real/module2_research_app/app.py
```
