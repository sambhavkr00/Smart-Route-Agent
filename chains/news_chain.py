import requests
from utils.api_keys import TAVILY_API_KEY

def get_recent_disruptions(source, destination, date):
    # Define target, context, and constraint for the query
    query = (
        f"Target: road transport disruptions between {source} and {destination}. "
        f"Context: recent news about protests, accidents, closures, or delays affecting delivery routes. "
        f"Constraint: on/around {date} from trusted news sources (bbc.com, reuters.com, cnn.com, thehindu.com, ndtv.com, indiatoday.in, timesofindia.indiatimes.com)."
    )
    url = "https://api.tavily.com/search"
    headers = {"Authorization": f"Bearer {TAVILY_API_KEY}"}
    payload = {
        "query": query,
        "search_depth": "advanced",
        "time_range": "week",
        "max_results": 20,
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        return "Error fetching news"

    results = response.json().get("results", [])
    # print([f"- {item['title']}: {item['url']}" for item in results])
    return "\n".join([f"- {item['title']}: {item['url']}" for item in results])


