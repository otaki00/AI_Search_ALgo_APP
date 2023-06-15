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
import os
import sys
from get_data import getData
from get_data import getGraph


CITIES = getData.get_cities()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        html_file = self.make_map_file()
        
        # call the method for create the UI and pass the html_file for map
        self.create_UI(html_file)
        
    
    def make_map_file(self):
        # now lets start by fisrt creating map, 
        
        # this initialize the map, and set initial postion to palestine map
        # by give the lat and lng values for palestine (center) 
        self.palestine_map = folium.Map(location=[31.9522, 35.2332], tiles='cartoDB Positron', zoom_start=8, max_bounds=True, min_zoom=7, max_zoom=15)
        
        for city in CITIES:
            marker = folium.Marker(
                location=[city['lat'], city['lng']],
                popup= city['name'],
                icon= folium.Icon(color='blue', icon='circle')
            )
            self.palestine_map.add_child(marker)
        
        
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
        self.web_view.load(QUrl.fromLocalFile(html_file))
        
        mapFrame.addWidget(self.web_view)
        
        self.make_select_options()
        
        
        self.pushButton.setStyleSheet("background-color:#1A1A1D; border-radius:5px;color:white;")
        self.pushButton.clicked.connect(self.doSearch)
        
        self.showGraph.setStyleSheet("background-color:#C3073F; border-radius:5px;color:white;")
        self.showGraph.clicked.connect(self.displayGraph)
    
    
    def drawLine(self, city1Cor, city2Cor):

        # Create a PolyLine between the two cities
        line = folium.PolyLine(locations=[city1Cor, city2Cor], color='blue', weight=3)

        # Add the PolyLine to the map
        line.add_to(self.palestine_map)
    
    def displayGraph(self) :
        getGraph.make_graph(getData)
    
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
        cityCor1 = []
        cityCor2 = []
        for value in CITIES:
            if value['name'] == srcCity:
                cityCor1 = [value['lat'], value['lng']]
            if value['name'] == dstCity:
                cityCor2 = [value['lat'], value['lng']]
        self.drawLine(cityCor1, cityCor2)
        self.palestine_map.save(self.html_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())