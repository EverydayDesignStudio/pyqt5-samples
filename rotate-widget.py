#!/usr/bin/env python3

# Basic rotation widgets

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
import time


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App 2")
        self.setGeometry(0, 0, 640, 480)  #posX, posY, w, h

        label = QLabel("Stack Overflow 4", alignment=Qt.AlignCenter)
        # label.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        # label.setAlignment(Qt.AlignCenter)

        graphicsview = QGraphicsView()
        scene = QGraphicsScene(graphicsview)
        graphicsview.setScene(scene)

        proxy = QGraphicsProxyWidget()
        proxy.setWidget(label)
        proxy.setTransformOriginPoint(proxy.boundingRect().center())
        scene.addItem(proxy)

        slider = QSlider(minimum=0, maximum=359, orientation=Qt.Horizontal)
        slider.valueChanged.connect(proxy.setRotation)

        label_text = QLabel(
            "{}°".format(slider.value()), alignment=Qt.AlignCenter
        )
        slider.valueChanged.connect(
            lambda value: label_text.setText("{}°".format(slider.value()))
        )

        slider.setValue(45)

        w = QWidget()
        lay = QVBoxLayout(w)
        lay.addWidget(graphicsview)
        lay.addWidget(slider)
        lay.addWidget(label_text)
        w.resize(640, 480)

        self.setCentralWidget(w)
        self.show()


app = QApplication([])  # Holds the event loop
window = MainWindow()
app.exec_()
