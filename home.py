from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Home(QWidget):
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
        label = QLabel("Cryptolog v0.1-beta - Home")
        label.setStyleSheet("color: #999999; font-weight: bold; font-size: 30px; font-style: italic;")
        #label.setAlignment(Qt.AlignHCenter)
        layout.addWidget(label)
        # Cryptography section
        self.crypto = QPushButton("Cryptography")
        self.crypto.setStyleSheet(button_style)
        self.crypto.clicked.connect(self.when_crypto)
        layout.addWidget(self.crypto)
        # Cryptanalysis section
        self.analysis = QPushButton("Cryptanalysis")
        self.analysis.setStyleSheet(button_style)
        self.analysis.clicked.connect(self.when_analysis)
        layout.addWidget(self.analysis)
        # Steganography
        self.stegano = QPushButton("Steganography")
        self.stegano.setStyleSheet(button_style)
        self.stegano.clicked.connect(self.when_stegano)
        layout.addWidget(self.stegano)
        # Encodings
        self.encoding = QPushButton("Data encoding")
        self.encoding.setStyleSheet(button_style)
        self.encoding.clicked.connect(self.when_encoding)
        layout.addWidget(self.encoding)
        # Peda-crypto
        self.peda = QPushButton("Peda-crypto")
        self.peda.setStyleSheet(button_style)
        self.peda.clicked.connect(self.when_peda)
        layout.addWidget(self.peda)
        # Close software
        self.quit = QPushButton("Quit")
        self.quit.setStyleSheet(button_style)
        self.quit.clicked.connect(self.when_quit)
        layout.addWidget(self.quit)

    def when_crypto(self):
        self.upper.display_crypto_main()

    def when_analysis(self):
        self.upper.display_analysis_main()

    def when_stegano(self):
        self.upper.display_stegano_main()

    def when_encoding(self):
        self.upper.display_encoding_main()

    def when_peda(self):
        self.upper.display_peda_main()

    def when_quit(self):
        self.upper.quit()
