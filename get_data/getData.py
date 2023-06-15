# use panda library to read .csv files
import pandas as pd 

# return the list of cities that are stored in (assets/cities.csv)
def get_cities():
    CITIES = []
    cities = pd.read_csv('assets/cities.csv')
    
    # insert cities into CITIES list
    for i in range(len(cities)):
        new_city = {
            "name": cities['city'][i],
            "lat": cities['lat'][i],
            "lng": cities['lng'][i]
        }
        CITIES.append(new_city)
        
    return CITIES

def get_cities_names():
    names = []
    cities = pd.read_csv('assets/cities.csv')
    
    # insert cities into CITIES list
    for i in range(len(cities)):
        names.append(cities['city'][i])

        
    return names

# return the list of aerial distance that are stored in (assets/aerial_distances.csv)
def get_aerial_distacnes():
    
    AERIAL_DISTANCE = []
    
    arial_distance =pd.read_csv('assets/aerial_distances.csv')
    
    for i in range(len(arial_distance)):
        new_dis = {
            "city1": arial_distance['City 1'][i],
            "city2": arial_distance['City 2'][i],
            "aerial distance": arial_distance['Aerial Distance'][i],
        }
        AERIAL_DISTANCE.append(new_dis)
        
    return AERIAL_DISTANCE 



# return the list of road distance that are stored in (assets/road_distacne.csv)
def get_road_distacnes():
    
    ROAD_DISTANCE = []
    
    road_distance =pd.read_csv('assets/road_distacne.csv')
    
    for i in range(len(road_distance)):
        new_dis = {
            "city1": road_distance['City 1'][i],
            "city2": road_distance['City 2'][i],
            "road distance": road_distance['Road Distance'][i],
        }
        
        ROAD_DISTANCE.append(new_dis)
        
    return ROAD_DISTANCE

def connet_cities():
    connections = [
        ("Jerusalem", "Ramallah"),
        ("Jerusalem", "Jericho"),
        ("Jerusalem", "Bethlehem"),
        ("Jerusalem", "Qalqilya"),
        ("Jerusalem", "Gaza City"),
        ("Qalqilya", "Tulkarem"),
        ("Ramallah", "Nablus"),
        ("Nablus", "Jenin"),
        ("Nablus", "Tulkarem"),
        ("Ramallah", "Jericho"),
        ("Jericho", "Hebron"),
        ("Jericho", "Nablus"),
        ("Hebron", "Bethlehem"),
        ("Bethlehem", "Beit Jala"),
        ("Bethlehem", "Khan Yunis"),
        ("Gaza City", "Gaza Beach"),
        ("Gaza City", "Khan Yunis"),
        ("Gaza City", "Beit Lahia"),
        ("Khan Yunis", "Gaza Beach"),
        ("Khan Yunis", "Rafah"),
        ("Rafah", "Gaza Beach"),
    ]
    
    return connections