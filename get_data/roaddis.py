import requests
import csv

# Replace 'YOUR_API_KEY' with your actual OpenRouteService API key
API_KEY = '5b3ce3597851110001cf6248bb5f92e13ea8484a8170c48106b7e823'

# Define the list of cities and their names
cities = [
        {"name": "Jerusalem", "lat": 31.7683, "lon": 35.2137},
        {"name": "Gaza City", "lat": 31.5224, "lon": 34.4538},
        {"name": "Ramallah", "lat": 31.8980, "lon": 35.2041},
        {"name": "Hebron", "lat": 31.5326, "lon": 35.0998},
        {"name": "Nablus", "lat": 32.2226, "lon": 35.2628},
        {"name": "Bethlehem", "lat": 31.7054, "lon": 35.2024},
        {"name": "Jenin", "lat": 32.4616, "lon": 35.2956},
        {"name": "Tulkarm", "lat": 32.3136, "lon": 35.0289},
        {"name": "Jericho", "lat": 31.8592, "lon": 35.4398},
        {"name": "Rafah", "lat": 31.2930, "lon": 34.2358},
        {"name": "Khan Yunis", "lat": 31.3373, "lon": 34.3134},
        {"name": "Beit Lahia", "lat": 31.5381, "lon": 34.5032},
        {"name": "Beit Jala", "lat": 31.7133, "lon": 35.2064},
        {"name": "Qalqilya", "lat": 32.1973, "lon": 34.9932},
        {"name": "Gaza Beach", "lat": 31.5221, "lon": 34.4314},
    ]

# Calculate the road distance between two cities using the OpenRouteService API
def calculate_road_distance(city1, city2):
    url = f"https://api.openrouteservice.org/v2/matrix/driving-car"
    params = {
        "locations": [[city1['lon'], city1['lat']], [city2['lon'], city2['lat']]],
        "metrics": ["distance"],
    }
    headers = {
        "Authorization": API_KEY
    }
    response = requests.post(url, json=params, headers=headers)
    data = response.json()
    distance = data['distances'][0][1]  # Distance from city1 to city2
    return distance / 1000  # Convert distance from meters to kilometers

# Calculate and save the road distances between all cities in a CSV file
with open('road_distances.csv', 'w', newline='') as csvfile:
    fieldnames = ['City 1', 'City 2', 'Road Distance (km)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(7,len(cities)):
        for j in range(i+1, len(cities)):
            city1 = cities[i]
            city2 = cities[j]
            road_distance = calculate_road_distance(city1, city2)

            writer.writerow({
                'City 1': city1['name'],
                'City 2': city2['name'],
                'Road Distance (km)': road_distance
            })
