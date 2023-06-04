# imoprt libraries that i will use
# pyqt5 for GUI
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtWebEngineWidgets import  QWebEngineView
# this for get the path of html file(for map) and display it inside the widget
from PyQt5.QtCore import QUrl
# for display the map that i will use
# its an extrenal library that used for crate and display interactive maps
import folium 
import os
import sys
from get_data import getData


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # now lets start by fisrt creating map, 
        
        # this initialize the map, and set initial postion to palestine map
        # by give the lat and lng values for palestine (center) 
        palestine_map = folium.Map(location=[31.9522, 35.2332], tiles='cartoDB Positron', zoom_start=8, max_bounds=True, min_zoom=7, max_zoom=12)
        
        cities = getData.get_cities()
        
        # print(cities)
        
        for city in cities:
            marker = folium.Marker(
                location=[city['lat'], city['lng']],
                popup= city['name'],
                icon= folium.Icon(color='blue', icon='circle')
            )
            palestine_map.add_child(marker)
        
        
        # now lets ave the map in html file
        palestine_map.save('map.html')
        
        # get the path for the html file
        curr_path = os.path.dirname(os.path.abspath(__file__))
        html_file = os.path.join(curr_path, "map.html")
        
        # create view for the map
        # initialize the webView
        self.web_view = QWebEngineView()
        self.web_view.load(QUrl.fromLocalFile(html_file))
        
        # creating layout that will contains the map 
        
        # map_layout.addWidget(self.web_view)
        
        central_widget = QWidget(self)
        central_widget.setStyleSheet("background-color: white;")
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)
        
        leftSide = QWidget()
        leftSide.setFixedWidth(400)
        
        
        leftSideContainer = QVBoxLayout(leftSide)
        
        # start left side 
        WelcomeMsg = QLabel("Welcome to PalestineCutter App")
        WelcomeMsg.setStyleSheet("color: #161853; font-weight:500; font-size: 24px")
        

        
        leftSideContainer.addWidget(WelcomeMsg)
        # creating the widget that will hold the map layout and other widgets
        
        layout.addWidget(self.web_view)
        layout.addWidget(leftSide)
        
        self.setGeometry(100, 100, 1300, 800)
        self.setWindowTitle("Palestine Cutter")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())