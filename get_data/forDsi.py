import math
import csv

# Define the list of cities and their coordinates
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

# Calculate the aerial distance between two points using the Haversine formula
def calculate_aerial_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers

    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Calculate the differences in latitude and longitude
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Apply the Haversine formula
    a = math.sin(delta_lat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c

    return distance

# Calculate and save the aerial distances between all cities in a CSV file
with open('aerial_distances.csv', 'w', newline='') as csvfile:
    fieldnames = ['City 1', 'City 2', 'Aerial Distance (km)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            city1 = cities[i]
            city2 = cities[j]
            aerial_distance = calculate_aerial_distance(city1['lat'], city1['lon'], city2['lat'], city2['lon'])

            writer.writerow({
                'City 1': city1['name'],
                'City 2': city2['name'],
                'Aerial Distance (km)': aerial_distance
            })
