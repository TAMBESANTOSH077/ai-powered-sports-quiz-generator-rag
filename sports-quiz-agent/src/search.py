from duckduckgo_search import DDGS


def get_live_news(sport):
    """
    Fetch recent sports news using DuckDuckGo.
    """

    query = f"{sport} latest news tournament winners championship 2026"

    snippets = []

    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=5)

            for item in results:
                title = item.get("title", "")
                body = item.get("body", "")

                snippets.append(
                    f"Title: {title}\nSummary: {body}"
                )

    except Exception as e:
        return f"Unable to fetch live news.\nError: {str(e)}"

    if not snippets:
        return "No recent news found."

    return "\n\n".join(snippets)