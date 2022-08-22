from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainEncoding(QWidget):
    def __init__(self, window):
        QWidget.__init__(self)
        self.upper = window
        # Set background
        #self.setStyleSheet("background-image: url(img/bg3.jpeg); background-position: center center;")
        # Content
        layout = QGridLayout()
        self.setLayout(layout)
        layout.setHorizontalSpacing(15)
        layout.setVerticalSpacing(10)
        button_style = "QPushButton {border: 2px solid #8f8f91; border-radius: 6px; " +\
        "background-color: #446d91; color: #20cde8;" +\
        "font-size: 30px; font-weight: bold; padding: 12px;} " +\
        "QPushButton::pressed {background-color: #2b455c;}"
        # Widget title
        label = QLabel("Data encoding portal")
        label.setStyleSheet("color: #999999; font-weight: bold; font-size: 30px; font-style: italic;")
        layout.addWidget(label)
        # Binary code section
        self.binary = QPushButton("Binary code")
        self.binary.setStyleSheet(button_style)
        self.binary.clicked.connect(self.when_binary)
        layout.addWidget(self.binary)
        # Morse code section
        self.morse = QPushButton("Morse code")
        self.morse.setStyleSheet(button_style)
        self.morse.clicked.connect(self.when_morse)
        layout.addWidget(self.morse)
        # Color code section
        self.color = QPushButton("Color code")
        self.color.setStyleSheet(button_style)
        self.color.clicked.connect(self.when_color)
        layout.addWidget(self.color)
        # QR code section
        self.qr = QPushButton("QR code")
        self.qr.setStyleSheet(button_style)
        self.qr.clicked.connect(self.when_qr)
        layout.addWidget(self.qr)
        # Home menu
        self.back = QPushButton("Back to Home")
        self.back.setStyleSheet(button_style)
        self.back.clicked.connect(self.when_back)
        layout.addWidget(self.back)

    def when_binary(self):
        self.upper.display_binary_code()

    def when_morse(self):
        self.upper.display_morse_code()

    def when_color(self):
        self.upper.display_color_code()

    def when_qr(self):
        self.upper.display_qr_code()

    def when_back(self):
        self.upper.display_home()
