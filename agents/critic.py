from services.llm import generate_response


def critic_agent(query: str, research: list, report: str) -> str:
    prompt = (
        f"Review this report for the topic '{query}' using only the provided research.\n\n"
        f"Research:\n{research}\n\n"
        f"Report:\n{report}\n\n"
        "Verify:\n"
        "1. All claims and numbers match the research data with accurate dates and context.\n"
        "2. Listed competitors (up to two) and source URLs come directly from the research.\n"
        "3. Missing information and data limitations are clearly pointed out.\n\n"
        "Reply with APPROVED if the report is accurate and well-supported. "
        "If not, give short, practical fixes using only the available research."
    )
    return generate_response(prompt)