import requests
from langchain.prompts import PromptTemplate
from utils.api_keys import GROQ_API_KEY

def summarize_all(disruptions, traffic, weather, source, destination, date):
    prompt = PromptTemplate.from_template(
    """
    === Disruptions ===
    {disruptions}
    
    === Traffic Info ===
    {traffic}
    
    === Weather Forecast ===
    {weather}
    
    Provide a very short delivery title in the format:
    "Delivery: {source} → {destination} | Distance: <distance> km | Usual Time: <usual_time> | Delay: <delay> | Weather: <weather_condition> on {date}"
    (Extract <distance> and <usual_time> from traffic info, <delay> from traffic or disruptions, and <weather_condition> from weather info for the delivery date.)
    
    Disruption/Risks in 3-4 lines, summarize any road disruptions and risks for this route and date. If there are no disruptions, mention that also.
    
    After that, provide:
    - Alternate route advice (if any in 2-3 lines)
    - Expected delays (in days or hours in 1-2 lines)
    - Concise summary (in 2-3 lines)
    """)

    full_prompt = prompt.format(
        source=source,
        destination=destination,
        date=date,
        disruptions=disruptions,
        traffic=traffic,
        weather=weather
    )

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "user", "content": full_prompt}
        ],
        "max_tokens": 1000
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        print(f"Groq LLM Error: {response.status_code} - {response.text}")
        return None