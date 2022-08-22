from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainCrypto(QWidget):
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
        label = QLabel("Cryptography portal")
        label.setStyleSheet("color: #999999; font-weight: bold; font-size: 30px; font-style: italic;")
        layout.addWidget(label)
        # Ceasar cipher
        self.ceasar = QPushButton("Ceasar cipher")
        self.ceasar.setStyleSheet(button_style)
        self.ceasar.clicked.connect(self.when_ceasar)
        layout.addWidget(self.ceasar)
        # Linear cipher
        self.linear = QPushButton("Linear cipher")
        self.linear.setStyleSheet(button_style)
        self.linear.clicked.connect(self.when_linear)
        layout.addWidget(self.linear)
        # Vigenere cipher
        self.vigenere = QPushButton("Vigenere cipher")
        self.vigenere.setStyleSheet(button_style)
        self.vigenere.clicked.connect(self.when_vigenere)
        layout.addWidget(self.vigenere)
        # Hill cipher
        self.hill = QPushButton("Hill cipher")
        self.hill.setStyleSheet(button_style)
        self.hill.clicked.connect(self.when_hill)
        layout.addWidget(self.hill)
        # RSA cipher
        self.rsa = QPushButton("RSA cipher")
        self.rsa.setStyleSheet(button_style)
        self.rsa.clicked.connect(self.when_rsa)
        layout.addWidget(self.rsa)
        # Hash algorithms
        self.hash = QPushButton("Hash algorithms")
        self.hash.setStyleSheet(button_style)
        self.hash.clicked.connect(self.when_hash)
        layout.addWidget(self.hash)
        # Home menu
        self.back = QPushButton("Back to Home")
        self.back.setStyleSheet(button_style)
        self.back.clicked.connect(self.when_back)
        layout.addWidget(self.back)

    def when_ceasar(self):
        self.upper.display_ceasar_crypto()

    def when_linear(self):
        self.upper.display_linear_crypto()

    def when_vigenere(self):
        self.upper.display_vigenere_crypto()

    def when_hill(self):
        self.upper.display_hill_crypto()

    def when_rsa(self):
        self.upper.display_rsa_crypto()

    def when_hash(self):
        self.upper.display_hash_crypto()

    def when_back(self):
        self.upper.display_home()
