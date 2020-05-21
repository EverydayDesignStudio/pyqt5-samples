#!/usr/bin/env python3

# Basic rotation widgets

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
import time

class RotatableContainer(QGraphicsView):
    def __init__(self, widget: QWidget, degree: float):
        super(QGraphicsView, self).__init__()

        scene = QGraphicsScene(self)
        self.setScene(scene)

        self.proxy = QGraphicsProxyWidget()
        self.proxy.setWidget(widget)
        self.proxy.setTransformOriginPoint(self.proxy.boundingRect().center())
        scene.addItem(self.proxy)

    def rotate(self, degree: float):
        self.proxy.setRotation(degree)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome Rotating Widget")
        self.setGeometry(0, 0, 640, 480)  #posX, posY, w, h

        # Widget you want to rotate
        label = QLabel("Stack Overflow", alignment=Qt.AlignCenter)
        # Container you place the widget in
        container = RotatableContainer(label, 90)

        # Create slider and connect to the rotate method in the container
        slider = QSlider(minimum=0, maximum=359, orientation=Qt.Horizontal)
        # slider.valueChanged.connect(proxy.setRotation)
        slider.valueChanged.connect(container.rotate)

        label_text = QLabel("{}°".format(slider.value()), alignment=Qt.AlignCenter)
        slider.valueChanged.connect(lambda value: label_text.setText("{}°".format(slider.value())))
        slider.setValue(45)

        # Display the widgets
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.addWidget(container)
        lay.addWidget(slider)
        lay.addWidget(label_text)
        w.resize(640, 480)

        self.setCentralWidget(w)
        self.show()


app = QApplication([])  # Holds the event loop
window = MainWindow()
app.exec_()
