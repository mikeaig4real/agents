"""Crew factories that converge single-purpose sub-agents."""

from crewai import Crew, Process, Task

from sub_agents.debate_pro_agent import build_debate_pro_agent
from sub_agents.debate_con_agent import build_debate_con_agent
from sub_agents.debate_moderator_agent import build_debate_moderator_agent
from sub_agents.engineering_architect_agent import build_engineering_architect_agent
from sub_agents.engineering_qa_agent import build_engineering_qa_agent
from sub_agents.engineering_delivery_agent import build_engineering_delivery_agent
from sub_agents.financial_market_agent import build_financial_market_agent
from sub_agents.financial_fundamental_agent import build_financial_fundamental_agent
from sub_agents.financial_reviewer_agent import build_financial_reviewer_agent


def build_debate_crew(topic: str) -> Crew:
    """Converge debate sub-agents into one crew."""
    pro = build_debate_pro_agent(topic)
    con = build_debate_con_agent(topic)
    judge = build_debate_moderator_agent()

    pro_task = Task(description="Provide 5 concise pro points.", expected_output="5 pro bullet points.", agent=pro)
    con_task = Task(description="Provide 5 concise risk points.", expected_output="5 risk bullet points.", agent=con)
    judge_task = Task(
        description="Write a final decision memo with recommendation and 3 safeguards.",
        expected_output="Decision memo under 250 words.",
        agent=judge,
        context=[pro_task, con_task],
    )

    return Crew(
        agents=[pro, con, judge],
        tasks=[pro_task, con_task, judge_task],
        process=Process.sequential,
        verbose=False,
    )


def build_engineering_crew(problem: str) -> Crew:
    """Converge engineering sub-agents into one crew."""
    architect = build_engineering_architect_agent(problem)
    qa = build_engineering_qa_agent()
    planner = build_engineering_delivery_agent()

    design_task = Task(
        description="Write architecture outline, modules, APIs, and deployment considerations.",
        expected_output="Architecture plan with module list and interfaces.",
        agent=architect,
    )
    qa_task = Task(
        description="Write acceptance criteria and top 10 high-priority QA scenarios.",
        expected_output="Acceptance and QA checklist.",
        agent=qa,
        context=[design_task],
    )
    plan_task = Task(
        description="Produce a 2-sprint plan with owners, dependencies, and risks.",
        expected_output="Execution plan with milestones.",
        agent=planner,
        context=[design_task, qa_task],
    )

    return Crew(
        agents=[architect, qa, planner],
        tasks=[design_task, qa_task, plan_task],
        process=Process.sequential,
        verbose=False,
    )


def build_financial_crew(universe: str) -> Crew:
    """Converge financial sub-agents into one crew."""
    researcher = build_financial_market_agent(universe)
    analyst = build_financial_fundamental_agent()
    reviewer = build_financial_reviewer_agent()

    market_task = Task(
        description="Summarize environment and sector trends that matter now.",
        expected_output="Macro + sector bullet summary.",
        agent=researcher,
    )
    compare_task = Task(
        description="Compare core names in the universe using transparent assumptions.",
        expected_output="Comparison table with caveats.",
        agent=analyst,
        context=[market_task],
    )
    decision_task = Task(
        description="Provide one recommendation with risks and position sizing guidance.",
        expected_output="Recommendation memo.",
        agent=reviewer,
        context=[market_task, compare_task],
    )

    return Crew(
        agents=[researcher, analyst, reviewer],
        tasks=[market_task, compare_task, decision_task],
        process=Process.sequential,
        verbose=False,
    )
