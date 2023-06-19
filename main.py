# imoprt libraries that i will use
# pyqt5 for GUI
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QComboBox,  QSizePolicy, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtWebEngineWidgets import  QWebEngineView
# this for get the path of html file(for map) and display it inside the widget
from PyQt5.QtCore import QUrl
from PyQt5 import uic
# for display the map that i will use
# its an extrenal library that used for crate and display interactive maps
import folium 
from folium.features import DivIcon
from folium.plugins import MeasureControl
import os
import sys
from get_data import getData
from get_data import getGraph
from get_data import bfs
from get_data import aStar
from timeit import default_timer as timeir
import random


CITIES = getData.get_cities()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1220, 733)  # Set the fixed size of the window
        
        html_file = self.make_map_file()
        
        # call the method for create the UI and pass the html_file for map
        self.create_UI(html_file)
        
    
    def add_markers_to_map(self):
        for city in CITIES:
            marker = folium.Marker(
                location=[city['lat'], city['lng']],
                popup= city['name'],
                icon= folium.Icon(color='blue', icon='circle')
            )
            self.palestine_map.add_child(marker)
    
    def make_map_file(self):
        # now lets start by fisrt creating map, 
        
        # this initialize the map, and set initial postion to palestine map
        # by give the lat and lng values for palestine (center) 
        self.palestine_map = folium.Map(location=[31.9522, 35.2332], tiles='cartoDB Positron', zoom_start=8, max_bounds=True, min_zoom=7, max_zoom=15)
        
        
        self.add_markers_to_map()
        
        # now lets ave the map in html file
        self.palestine_map.save('map.html')
        
        # get the path for the html file
        curr_path = os.path.dirname(os.path.abspath(__file__))
        self.html_file = os.path.join(curr_path, "map.html")
        
        return self.html_file
    
    # this method is used for create the main UI for app
    def create_UI(self, html_file):
        # create view for the map
        
        # load ui from file 
        uic.loadUi("palestineCutter.ui", self)
        self.setWindowTitle("PalestineCutter")
        self.show()
        
        
        self.welocomeMsg.setStyleSheet("color:#950740;font-weight:400;")
        
        # get element 
        mapFrame = self.forMap
        
        self.web_view = QWebEngineView()
        self.web_view.setFixedSize(869, 711)
        self.web_view.load(QUrl.fromLocalFile(html_file))
        
        
        
        mapFrame.addWidget(self.web_view)
        
        self.make_select_options()
        
        
        self.pushButton.setStyleSheet("background-color:#1A1A1D; border-radius:5px;color:white;")
        self.pushButton.clicked.connect(self.doSearch)
        
        self.showGraph.setStyleSheet("background-color:#C3073F; border-radius:5px;color:white;")
        self.showGraph.clicked.connect(self.displayGraphRoad)
        
        self.showGraph_2.setStyleSheet("background-color:#D12122; border-radius:5px;color:white;")
        self.showGraph_2.clicked.connect(self.displayGraphAerial)
    
    def drawLine(self, path):
        
        cor_path = []
        i = 0
        j = 0
        
        while i < len(path): 
            if j == len(CITIES):
                j = 0 
            elif path[i] == CITIES[j]['name']:
                cor_path.append((CITIES[j]['lat'], CITIES[j]['lng']))
                i+=1
                j =0
            else:
                j+=1
        print(cor_path)
        # Generate a random color
        color = '#{:06x}'.format(random.randint(0, 256**3))
        for i in range(len(cor_path) - 1):
            start_city = cor_path[i]
            end_city = cor_path[i + 1]
            start_city_name = path[i]
            end_city_name = path[i+1]
            
            # Get the coordinates of the start and end cities
            start_coords = (start_city[0], start_city[1])
            end_coords = (end_city[0], end_city[1])
            
            
            distance = self.get_distance(start_city_name, end_city_name)
            # distance = 32.21
            
            line = folium.PolyLine(locations=[start_coords, end_coords], color=color, weight=3)
            
            # Calculate the midpoint of the line
            midpoint_coords = [(start_coords[0] + end_coords[0]) / 2, (start_coords[1] + end_coords[1]) / 2]
            
            # Add a label with the distance on the line
            folium.Marker(
                location=midpoint_coords,
                icon=folium.DivIcon(html=f'<div style="font-size: 13px; color: black;">{distance:.2f} km</div>')
            ).add_to(self.palestine_map)
            
            # Add the PolyLine to the map
            line.add_to(self.palestine_map)
            self.palestine_map.save(self.html_file)
        
        
        self.create_UI(self.html_file)
    
    def get_distance(self, city1, city2):
        cities_distances = getData.get_road_distacnes()
        
        for data in cities_distances:
            # print(data, city1, city2)
            if (data['city1'] == city1 and data['city2'] == city2) or (data['city2'] == city1 and data['city1'] == city2):
                return data['road distance']
        return 0
        
    
    def displayGraphRoad(self) :
        getGraph.make_graph_with_road_distance(getData)
    
    def displayGraphAerial(self) :
        getGraph.make_graph_with_aerial_distance(getData)
    
    # this method for make selection field, and will selection feild
    def make_select_options(self):
        
        self.src_combo = self.comboBoxForSrcCity
        self.dst_combo = self.comboBoxDstCity
        
        for value in CITIES:
            self.src_combo.addItem(value['name'])
            self.dst_combo.addItem(value['name'])
    
    def doSearch(self):
        srcCity = self.src_combo.currentText()
        dstCity = self.dst_combo.currentText()
        if srcCity == dstCity: 
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setWindowTitle("Same Cities !!")
            message_box.setText("The source City is the same as destination City !")
            message_box.exec_()
            return
        # print(srcCity, dstCity)
        
        message_box = QMessageBox()
        message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        if self.AStarAlgo.isChecked():
            start = timeir()
            result = aStar.AStar(start=srcCity, goal=dstCity, getData=getData, getGraph=getGraph)
            end = timeir()
            time = (end-start) * 1000
            if result != None:
                print(result)
                self.drawLine(result)
                self.palestine_map.save(self.html_file)
                message_box.setIcon(QMessageBox.Information)
                message_box.setWindowTitle("the Path was Found")
                result_msg = "the path is => \n"
                for i in result:
                    result_msg = result_msg + " , "+i
                message_box.setText(result_msg+"\n\n\n the function takes  "+ str(time)+"mS to execute with A*")
                message_box.exec_()
                
        else:
            start = timeir()
            result = bfs.BFS(start=srcCity, goal=dstCity, getData=getData, getGraph=getGraph)
            end = timeir()
            time = (end-start) * 1000
            if result != None:
                self.drawLine(result)
                self.palestine_map.save(self.html_file)
                message_box.setIcon(QMessageBox.Information)
                message_box.setWindowTitle("the Path was Found")
                result_msg = "the path is => \n"
                for i in result:
                    result_msg = result_msg + " , "+i
                message_box.setText(result_msg+"\n\n\n the function takes  "+ str(time)+"mS to execute with BFS")
                message_box.exec_()
                
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())