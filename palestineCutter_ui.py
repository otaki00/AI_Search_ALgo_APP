# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\asus\Desktop\Term2\AI\Projects\project1\final_v\palestineCutter.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1220, 733)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.for_2 = QtWidgets.QWidget(self.centralwidget)
        self.for_2.setGeometry(QtCore.QRect(870, 0, 351, 711))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.for_2.setFont(font)
        self.for_2.setObjectName("for_2")
        self.welocomeMsg = QtWidgets.QLabel(self.for_2)
        self.welocomeMsg.setGeometry(QtCore.QRect(10, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.welocomeMsg.setFont(font)
        self.welocomeMsg.setLineWidth(2)
        self.welocomeMsg.setObjectName("welocomeMsg")
        self.widget = QtWidgets.QWidget(self.for_2)
        self.widget.setGeometry(QtCore.QRect(50, 100, 271, 121))
        self.widget.setObjectName("widget")
        self.comboBoxForSrcCity = QtWidgets.QComboBox(self.widget)
        self.comboBoxForSrcCity.setGeometry(QtCore.QRect(10, 80, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBoxForSrcCity.setFont(font)
        self.comboBoxForSrcCity.setObjectName("comboBoxForSrcCity")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget_2 = QtWidgets.QWidget(self.for_2)
        self.widget_2.setGeometry(QtCore.QRect(50, 250, 271, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.comboBoxDstCity = QtWidgets.QComboBox(self.widget_2)
        self.comboBoxDstCity.setGeometry(QtCore.QRect(10, 80, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.comboBoxDstCity.setFont(font)
        self.comboBoxDstCity.setObjectName("comboBoxDstCity")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.widget_3 = QtWidgets.QWidget(self.for_2)
        self.widget_3.setGeometry(QtCore.QRect(50, 420, 271, 171))
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.AStarAlgo = QtWidgets.QRadioButton(self.widget_3)
        self.AStarAlgo.setGeometry(QtCore.QRect(20, 60, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.AStarAlgo.setFont(font)
        self.AStarAlgo.setChecked(True)
        self.AStarAlgo.setObjectName("AStarAlgo")
        self.BFSAlgo = QtWidgets.QRadioButton(self.widget_3)
        self.BFSAlgo.setGeometry(QtCore.QRect(20, 110, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.BFSAlgo.setFont(font)
        self.BFSAlgo.setIconSize(QtCore.QSize(30, 30))
        self.BFSAlgo.setChecked(False)
        self.BFSAlgo.setObjectName("BFSAlgo")
        self.pushButton = QtWidgets.QPushButton(self.for_2)
        self.pushButton.setGeometry(QtCore.QRect(50, 600, 271, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.for_2)
        self.line.setGeometry(QtCore.QRect(-17, 0, 20, 681))
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.showGraph = QtWidgets.QPushButton(self.for_2)
        self.showGraph.setGeometry(QtCore.QRect(230, 650, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.showGraph.setFont(font)
        self.showGraph.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.showGraph.setObjectName("showGraph")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 871, 711))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.forMap = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.forMap.setContentsMargins(0, 0, 0, 0)
        self.forMap.setObjectName("forMap")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1220, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PalestineCutter"))
        self.welocomeMsg.setText(_translate("MainWindow", "Welcome To PalestineCutter"))
        self.label.setText(_translate("MainWindow", "Choose Source City :"))
        self.label_2.setText(_translate("MainWindow", "Choose Destination City :"))
        self.label_3.setText(_translate("MainWindow", "Choose Search Algorithm : "))
        self.AStarAlgo.setText(_translate("MainWindow", "A*"))
        self.BFSAlgo.setText(_translate("MainWindow", "Breadth first Search"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.showGraph.setText(_translate("MainWindow", "Show Graph"))
