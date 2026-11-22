from services.llm import generate_response


def analyst_agent(query: str, research: list) -> str:
    prompt = (
        f"Write a market research report on '{query}' using only the research provided below.\n\n"
        f"Research:\n{research}\n\n"
        "Use this exact Markdown structure:\n\n"
        f"# Market Research Report\n\n"
        f"Research Topic: {query}\n\n"
        "## 1. Market Overview\n"
        "Write one or two short paragraphs summarizing the market based on the research. "
        "Do not put source names or URLs inside this section.\n\n"
        "## 2. Main Competitors\n"
        "List up to two relevant competitors from the research using bullet points with bold names "
        "(for example: - **Competitor Name**: Short description). If none are named in the research, "
        "state that clearly in one sentence.\n\n"
        "## 3. Key Findings\n"
        "List 3 to 5 bullet points with bold topic labels (for example: - **Topic**: Finding with dates/numbers from the research).\n\n"
        "## 4. Sources\n"
        "Write one short intro line followed by a bullet list of only the URLs from the research.\n\n"
        "## 5. Missing Information\n"
        "Write one short intro line followed by a bullet list of what data is missing or unclear.\n\n"
        "Rules:\n"
        "Use only facts, numbers, and URLs from the research without making anything up.\n"
        "Include dates or time periods for numbers when stated in the sources.\n"
        "Do not use tables, HTML tags like <br>, inline citations like [Wikipedia], or any closing disclaimer at the end."
    )
    return generate_response(prompt)