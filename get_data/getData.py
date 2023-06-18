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
    
    road_distance =pd.read_csv('assets/road_distance.csv')
    
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
        ("Qalqilya", "Tulkarm"),
        ("Ramallah", "Nablus"),
        ("Nablus", "Jenin"),
        ("Nablus", "Tulkarm"),
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

def get_graph_edges_values_road_distance():
    
    road_distance_for_all = get_road_distacnes()
    connections = connet_cities()
    road_distance_for_graph_nodes =[]
    i = 0
    j = 0
    
    while j < len(connections) and i < len(road_distance_for_all):
        if (road_distance_for_all[i]['city1'] == connections[j][0] and road_distance_for_all[i]['city2'] == connections[j][1]) or (road_distance_for_all[i]['city1'] == connections[j][1] and road_distance_for_all[i]['city2'] == connections[j][0]):
            
            # print(road_distance_for_all[i]['city1'],road_distance_for_all[i]['city2'],road_distance_for_all[i]['road distance'])
            # road_distance_for_graph_nodes.append(1)
            road_distance_for_graph_nodes.append((road_distance_for_all[i]['city1'],road_distance_for_all[i]['city2'],road_distance_for_all[i]['road distance']))
            j+=1
            i = 0
        else:
            i+=1        
    return road_distance_for_graph_nodes

# print(get_graph_edges_values_road_distance())

def get_graph_edges_values_aerial_distance():
    
    aerial_distance_for_all = get_aerial_distacnes()
    connections = connet_cities()
    aerial_distance_for_graph_nodes =[]
    
    i = 0
    j = 0
    
    while j < len(connections) and i < len(aerial_distance_for_all):
        if (aerial_distance_for_all[i]['city1'] == connections[j][0] and aerial_distance_for_all[i]['city2'] == connections[j][1]) or (aerial_distance_for_all[i]['city1'] == connections[j][1] and aerial_distance_for_all[i]['city2'] == connections[j][0]):
            
            aerial_distance_for_graph_nodes.append((aerial_distance_for_all[i]['city1'],aerial_distance_for_all[i]['city2'],aerial_distance_for_all[i]['aerial distance']))
            j+=1
            i = 0
        else:
            i+=1        
    return aerial_distance_for_graph_nodes


# this function return list of each city and the aerial distance 
# between itslef and dest
def get_heuristic_data(destenation):
    data = {destenation: 0}
    connection = connet_cities()
    aerial_data = get_aerial_distacnes()
    
    for item in connection:
        if item[0] == destenation or item[1] == destenation:
            for city_data in aerial_data:
                if city_data['city2'] == destenation :
                    data[city_data['city1']] = city_data["aerial distance"]
                elif city_data['city1'] == destenation :
                    data[city_data['city2']] = city_data["aerial distance"]
                else:
                    continue
    
    return data

