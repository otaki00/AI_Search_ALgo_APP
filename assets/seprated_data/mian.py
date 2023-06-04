import pandas as pd


file_paths = ['road_distances_p1.csv', 'road_distances_p2.csv', 'road_distances_p3.csv']

data = []


for file_path in file_paths:
    df = pd.read_csv(file_path)
    data.append(df)


all_data = pd.concat(data, ignore_index=True)

all_data.to_csv('road_distance.csv', index=False)