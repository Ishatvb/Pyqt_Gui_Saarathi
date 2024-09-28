import sys
import numpy as np
import random
import cv2
from PyQt5.QtCore import QTimer, QFile, QTextStream, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton, QLabel, QSizePolicy
import pyqtgraph as pg
from PyQt5.QtGui import QPixmap, QImage
from sidebar import Ui_MainWindow  

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.scada_btn_2.setChecked(True)

        self.connect_signals()
        
    def connect_signals(self):
        self.ui.scada_btn_1.toggled.connect(self.on_scada_btn_1_toggled)
        self.ui.scada_btn_2.toggled.connect(self.on_scada_btn_2_toggled)
        self.ui.luna_btn_1.toggled.connect(self.on_luna_btn_1_toggled)
        self.ui.luna_btn_2.toggled.connect(self.on_luna_btn_2_toggled)
        self.ui.hopper_btn_1.toggled.connect(self.on_hopper_btn_1_toggled)
        self.ui.hopper_btn_2.toggled.connect(self.on_hopper_btn_2_toggled)
        self.ui.head_btn_1.toggled.connect(self.on_head_btn_1_toggled)
        self.ui.head_btn_2.toggled.connect(self.on_head_btn_2_toggled)
        self.ui.tail_btn_1.toggled.connect(self.on_tail_btn_1_toggled)
        self.ui.tail_btn_2.toggled.connect(self.on_tail_btn_2_toggled)
        self.ui.search_btn.clicked.connect(self.on_search_btn_clicked)
        self.ui.user_btn.clicked.connect(self.on_user_btn_clicked)
        self.ui.search_btn.clicked.connect(self.on_search_btn_clicked)
        self.ui.user_btn.clicked.connect(self.on_user_btn_clicked)
        self.ui.stackedWidget.currentChanged.connect(self.on_stackedWidget_currentChanged)

    ## Function for searching
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)

    ## Function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):   
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                    + self.ui.full_menu_widget.findChildren(QPushButton)
        
        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)
            
    ## functions for changing menu page
    def on_scada_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_scada_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_luna_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_luna_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_hopper_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_hopper_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_head_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_head_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_tail_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_tail_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_power_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_power_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_history_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(8)

    def on_history_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(8)

    def on_stackedWidget_currentChanged(self, index):
        if index == 0:
            # Update SCADA page elements
            self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load style file
    style_file = QFile("style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

