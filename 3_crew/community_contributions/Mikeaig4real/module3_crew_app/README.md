# Module 3 Crew App

This implementation uses the same modular strategy:

- one role agent factory per file in `sub_agents/`
- crew convergence in `crews.py`
- routing/execution in `orchestrator.py`
- UI in `app.py`

## Structure
- `sub_agents/*.py` (single-role files)
- `crews.py` (converges sub-agents)
- `orchestrator.py` (single run entry)
- `app.py` (Gradio interface)

## Run
```bash
python 3_crew/community_contributions/Mikeaig4real/module3_crew_app/app.py
```
