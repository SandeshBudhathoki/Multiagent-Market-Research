
from services.web_search import search_web

def researcher_agent(query: str) -> list:
    results = search_web(query)
    research = []
    for result in results:
        research.append({
            "title": result.get("title", ""),
            "content": result.get("content", ""),
            "url": result.get("url", "")
        })
    return research
