from requests import get
import json

API_KEY = '2RFzx-wwIqd0j-FpGcum'

class Colors:
    YELLOW = '\033[93m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    ORANGE = '\033[33m'
    PINK = '\033[95m'
    END = '\033[0m'
    BOLD = '\033[1m'

def main():
    # Portage & Main
    lat = 49.895
    lon = -97.139
    
    # Random Distance
    # lat = 50.892
    # lon = -98.153
    
    # U of W (Downtown) 
    # lat = 49.749
    # lon = -97.135
    
    # U of M
    # lat = 49.807
    # lon = -97.134
    
    # Polo Park
    # lat = 49.884
    # lon = -97.192
    distance = 250  # in meters
    
    url = f"https://api.winnipegtransit.com/v3/stops.json?lon={lon}&lat={lat}&distance={distance}&api-key={API_KEY}"
    print("DEBUG: Attempting to fetch URL:", url)
    
    # url to request stops
    url_stops = f"https://api.winnipegtransit.com/v3/stops/10541/schedule?max-results-per-route=2&api-key={API_KEY}"

    # request bus stops nearby
    resp_stops = get(url_stops)
    
    # data is pulling from the url
    response = get(url)
    print("DEBUG: HTTP Status Code:", response.status_code)
    
    data = response.json() 
    stops = data.get('stops', [])
    
    if not stops:
        print(f"{Colors.PINK}No stops found within the specified distance.{Colors.END}")
        return
    
    length = len(stops)
    
    # Title with formatting
    print(f"\n{Colors.BOLD}{Colors.YELLOW}╔{'═' * 70}╗{Colors.END}")
    print(f"{Colors.BOLD}{Colors.YELLOW}║{'WINNIPEG TRANSIT STOPS NEARBY':^70}║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.YELLOW}╠{'═' * 70}╣{Colors.END}")
    print(f"{Colors.BOLD}{Colors.YELLOW}║ {Colors.CYAN}Location: {Colors.ORANGE}Portage & Main ({lat}, {lon}){Colors.YELLOW}{' ':>28}║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.YELLOW}║ {Colors.CYAN}Search Radius: {Colors.ORANGE}{distance} meters{Colors.YELLOW}{' ':>45}║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.YELLOW}║ {Colors.CYAN}Stops Found: {Colors.ORANGE}{length}{Colors.YELLOW}{' ':>50}║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.YELLOW}╠{'═' * 70}╣{Colors.END}")
    
    # Header for stops list
    print(f"{Colors.BOLD}{Colors.YELLOW}║ {Colors.PURPLE}{'STOP NAME':<50} {Colors.PURPLE}{'STOP ID':<8} {Colors.YELLOW}║{Colors.END}")
    print(f"{Colors.BOLD}{Colors.YELLOW}╠{'═' * 70}╣{Colors.END}")
    
    # List all stops
    for i, stop in enumerate(stops, 1):
        stop_name = stop.get('name', 'Unknown')
        stop_id = stop.get('key', 'Unknown')
        
        # Alternate colors for rows
        color = Colors.CYAN if i % 2 == 0 else Colors.ORANGE
        
        print(f"{Colors.BOLD}{Colors.YELLOW}║ {color}{stop_name:<50} {stop_id:<8} {Colors.YELLOW}║{Colors.END}")
    
    # Footer
    print(f"{Colors.BOLD}{Colors.YELLOW}╚{'═' * 70}╝{Colors.END}\n")
        
if __name__ == "__main__":
    main()