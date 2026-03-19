"""Crew factories for Module 3 app."""

from crewai import Agent, Crew, Process, Task


def build_debate_crew(topic: str) -> Crew:
    """Create a debate crew for a given topic."""
    pro = Agent(
        role="Pro Analyst",
        goal=f"Argue in favor of: {topic}",
        backstory="You prioritize practical upside and delivery outcomes.",
        verbose=False,
    )
    con = Agent(
        role="Con Analyst",
        goal=f"Argue against premature adoption of: {topic}",
        backstory="You identify operational and strategic risk early.",
        verbose=False,
    )
    judge = Agent(
        role="Moderator",
        goal="Synthesize both sides and provide a balanced recommendation.",
        backstory="You produce concise decision memos for leaders.",
        verbose=False,
    )

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
    """Create an engineering planning crew for a feature request."""
    architect = Agent(
        role="Software Architect",
        goal=f"Design a robust implementation for: {problem}",
        backstory="You design practical systems with clear boundaries.",
        verbose=False,
    )
    qa = Agent(
        role="QA Lead",
        goal="Define acceptance criteria and key edge cases.",
        backstory="You prevent production regressions with precise test planning.",
        verbose=False,
    )
    planner = Agent(
        role="Delivery Manager",
        goal="Create a sprint-ready delivery plan.",
        backstory="You convert technical plans into actionable milestones.",
        verbose=False,
    )

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
    """Create a financial research crew for a ticker universe."""
    researcher = Agent(
        role="Market Researcher",
        goal=f"Summarize macro and sector context for: {universe}",
        backstory="You produce concise market context with caveats.",
        verbose=False,
    )
    analyst = Agent(
        role="Fundamental Analyst",
        goal="Compare growth, profitability, and valuation tradeoffs.",
        backstory="You prioritize transparent assumptions.",
        verbose=False,
    )
    reviewer = Agent(
        role="Portfolio Reviewer",
        goal="Give a balanced recommendation and risk controls.",
        backstory="You avoid overconfident conclusions.",
        verbose=False,
    )

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
