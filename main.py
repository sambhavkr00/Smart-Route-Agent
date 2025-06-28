from chains.news_chain import get_recent_disruptions
from chains.traffic_chain import get_traffic_data
from chains.weather_chain import get_weather_forecast
from chains.summarize_chain import summarize_all

def run_agent(source, destination, date):
    print("Collecting news...")
    disruptions = get_recent_disruptions(source, destination, date)

    print("Checking traffic...")
    traffic = get_traffic_data(source, destination)

    print("Fetching weather...")
    weather = get_weather_forecast(destination, date)

    print("Generating summary...")
    summary = summarize_all(disruptions, traffic, weather, source, destination, date)

    print("\nFinal Output:\n")
    print(summary)

# if __name__ == "__main__":
#     source = input("Enter Source Address: ")
#     destination = input("Enter Destination Address: ")
#     date = input("Enter Date of Delivery (YYYY-MM-DD): ")
    # run_agent(source, destination, date)
