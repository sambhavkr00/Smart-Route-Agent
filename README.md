# Smart Route Agent

Smart Route Agent is a modular Python application (CLI and Streamlit frontend) that analyzes risks and disruptions for roadway delivery routes. It leverages real-time news, traffic, and weather data, and summarizes actionable recommendations using an LLM.

## Features

- **Input:** Source, destination, and delivery date
- **News Analysis:** Fetches recent disruptions from trusted news sources (Tavily API)
- **Traffic:** Real-time traffic and delay info (TomTom Routing API)
- **Weather:** Weather forecast for the delivery date (OpenWeatherMap)
- **Summarization:** Groq LLM generates a concise, actionable summary with risks, delays, and recommendations
- **Frontends:**
  - CLI orchestrator
  - Streamlit web app with modern UI
- **Error Handling:** Informs user if addresses are invalid or no route is available

## How It Works

1. **User provides** source, destination, and delivery date.
2. **News agent** fetches recent disruptions for the route.
3. **Traffic agent** gets real-time traffic and alternate routes (if available).
4. **Weather agent** fetches the forecast for the delivery date.
5. **Summarizer agent** (LLM) combines all data into a clear, actionable summary.

## Example Output

```
Delivery: New York → Boston | Main: 350 km, 210 min, Delay: 15 min | Alt: 360 km, 200 min, Delay: 5 min | Weather: Rainy on 2025-06-29

Disruptions/Risks: Minor roadwork on I-95, expect short delays. No major incidents reported.

- Alternate route advice: Alternate route is faster today due to less congestion.
- Expected delays: 5-15 min
- Concise summary: Delivery is feasible with minor delays. Consider alternate route for best timing.
```

## Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/sambhavkr00/Smart-Route-Agent.git
   cd Smart-Route-Agent
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure API keys:**
   - Copy `.env.example` to `.env` and add your API keys for Tavily, TomTom, OpenWeatherMap, and Groq.
4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

## API Keys Required

- [Tavily API](https://app.tavily.com/)
- [TomTom Routing API](https://developer.tomtom.com/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Groq LLM API](https://console.groq.com/)

## Project Structure

- `app.py` — Streamlit frontend
- `main.py` — CLI orchestrator
- `chains/` — Modular agent chains (news, traffic, weather, summarize)
- `utils/api_keys.py` — Loads API keys from `.env`
- `requirements.txt` — Python dependencies

## License

MIT
