import requests
from utils.api_keys import TOMTOM_API_KEY

def geocode_address(address, api_key):
    url = f"https://api.tomtom.com/search/2/geocode/{address}.json"
    params = {"key": api_key}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None
    results = response.json().get("results", [])

    if not results:
        return None
    position = results[0]["position"]
    return position["lon"], position["lat"]

def get_traffic_data(source, destination):
    api_key = TOMTOM_API_KEY
    source_coords = geocode_address(source, api_key)
    dest_coords = geocode_address(destination, api_key)

    if not source_coords or not dest_coords:
        return "Error geocoding addresses"
    
    url = (
        f"https://api.tomtom.com/routing/1/calculateRoute/"
        f"{source_coords[1]},{source_coords[0]}:{dest_coords[1]},{dest_coords[0]}/json"
    )
    params = {
        "key": api_key,
        "traffic": "true"
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return "Error fetching route"
    
    data = response.json()
    if not data.get("routes"):
        return "No route available for the given source and destination."
    
    summary = data["routes"][0]["summary"]
    distance_km = summary["lengthInMeters"] / 1000
    travel_time_min = summary["travelTimeInSeconds"] / 60
    traffic_delay_min = summary.get("trafficDelayInSeconds", 0) / 60

    return (
        f"Distance: {distance_km:.1f} km, "
        f"Estimated Duration: {travel_time_min:.1f} min, "
        f"Traffic Delay: {traffic_delay_min:.1f} min"
    )
