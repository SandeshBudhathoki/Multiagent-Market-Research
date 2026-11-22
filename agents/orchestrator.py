
from agents.analyst import analyst_agent
from agents.critic import critic_agent
from agents.researcher import researcher_agent
from services.llm import generate_response


def run_research(query: str) -> str:
    research = researcher_agent(query)
    report = analyst_agent(query, research)
    feedback = critic_agent(query, research, report)

    if feedback.strip().upper() != "APPROVED":
        prompt = (
            "Update the report based on feedback.\n\n"
            f"Report:\n{report}\n\n"
            f"Feedback:\n{feedback}\n\n"
            f"Research:\n{research}\n\n"
            "Include only information that is supported by the research data. "
            "Do not make up facts, numbers, or statistics that are not in the research."
            "Keep the exact same Markdown headings and formatting style (no tables, no <br> tags, no inline source labels, and no closing disclaimer at the end). "
        )

        report = generate_response(prompt)

    return report
