from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainAnalysis(QWidget):
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
        label = QLabel("Cryptanalysis portal")
        label.setStyleSheet("color: #999999; font-weight: bold; font-size: 30px; font-style: italic;")
        layout.addWidget(label)
        # Cryptography section
        self.ceasar = QPushButton("Break Ceasar cipher")
        self.ceasar.setStyleSheet(button_style)
        self.ceasar.clicked.connect(self.when_ceasar)
        layout.addWidget(self.ceasar)
        # Cryptanalysis section
        self.linear = QPushButton("Break Linear cipher")
        self.linear.setStyleSheet(button_style)
        self.linear.clicked.connect(self.when_linear)
        layout.addWidget(self.linear)
        # Steganography
        self.vigenere = QPushButton("Break Vigenere cipher")
        self.vigenere.setStyleSheet(button_style)
        self.vigenere.clicked.connect(self.when_vigenere)
        layout.addWidget(self.vigenere)
        # Peda-crypto
        self.rsa = QPushButton("Break RSA cipher")
        self.rsa.setStyleSheet(button_style)
        self.rsa.clicked.connect(self.when_rsa)
        layout.addWidget(self.rsa)
        # Home menu
        self.back = QPushButton("Back to Home")
        self.back.setStyleSheet(button_style)
        self.back.clicked.connect(self.when_back)
        layout.addWidget(self.back)

    def when_ceasar(self):
        pass

    def when_linear(self):
        pass

    def when_vigenere(self):
        pass

    def when_rsa(self):
        pass

    def when_back(self):
        self.upper.display_home()
