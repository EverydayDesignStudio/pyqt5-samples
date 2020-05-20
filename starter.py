#!/usr/bin/env python3

# Basic starter Qt class

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
import time


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("My Awesome App")
        self.setGeometry(350, 100, 1280, 720)  #posX, posY, w, h

        # Layout
        layout = QVBoxLayout()

        self.label = QLabel("Center")
        self.label.setAlignment(Qt.AlignCenter)
        button = QPushButton("Button!")
        button.pressed.connect(self.button_press)

        layout.addWidget(self.label)
        layout.addWidget(button)

        # Widget
        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        # Show the Qt app
        self.show()

        # self.timer = QTimer()
        # self.timer.setInterval(1000)
        # self.timer.timeout.connect(self.recurring_timer)
        # self.timer.start()

    def button_press(self):
        # Pass in the function
        print('this is a button press')


app = QApplication([])  # Holds the event loop
window = MainWindow()
app.exec_()
