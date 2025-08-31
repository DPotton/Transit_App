from requests import get
import json

API_KEY = '2RFzx-wwIqd0j-FpGcum'

def main():
    # Portage & Main
    # lat = 49.895
    # lon = -97.139
    
    # U of W (Downtown) 
    # lat = 49.749
    # lon = -97.135
    
    # U of M
    # lat = 49.807
    # lon = -97.134
    
    # Polo Park
    lat = 49.884
    lon = -97.192
    distance = 250  # in meters
    
    url = f"https://api.winnipegtransit.com/v3/stops.json?lon={lon}&lat={lat}&distance={distance}&api-key={API_KEY}"
    print("DEBUG: Attempting to fetch URL:", url)
    
    # data is pulling from the url
    response = get(url)
    print("DEBUG: HTTP Status Code:", response.status_code)
    
    data = response.json() 
    stops = data.get('stops', [])
    
    if not stops:
        print("No stops found within the specified distance.")
        return
    
    length = len(stops)
    print(f"Found {length} stops within {distance} meters of ({lat}, {lon}):")
    for stop in stops:
        stop_name = stop.get('name', 'Unknown')
        stop_id = stop.get('key', 'Unknown')
        print(f"Stop Name: {stop_name}, Stop ID: {stop_id}")
        
if __name__ == "__main__":
    main()

    
    
