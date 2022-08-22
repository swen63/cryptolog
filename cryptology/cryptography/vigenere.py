from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class VigenereCrypto(QWidget):
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
        label = QLabel("Vigenere cipher algorithm")
        label.setStyleSheet("color: #999999; font-weight: bold; font-size: 30px; font-style: italic;")
        layout.addWidget(label, 0, 0)
        # Description
        label = QLabel("This is a description ...")
        label.setWordWrap(True)
        layout.addWidget(label, 2, 0)
        # Options
        label = QLabel("Encryption/Decryption key :")
        layout.addWidget(label, 3, 0)
        self.key = QLineEdit()
        self.key.setPlaceholderText("Enter key ...")
        layout.addWidget(self.key, 3, 1)
        # Text input
        self.textin = QTextEdit()
        self.textin.setReadOnly(False)
        self.textin.setPlaceholderText("Enter your text here ...")
        layout.addWidget(self.textin, 4, 0)
        # Validation
        self.encryptb = QPushButton("Encrypt")
        self.encryptb.clicked.connect(self.when_encrypt)
        layout.addWidget(self.encryptb, 4, 1)
        self.decryptb = QPushButton("Decrypt")
        self.decryptb.clicked.connect(self.when_decrypt)
        layout.addWidget(self.decryptb, 5, 1)
        # Output
        self.output = QLabel()
        layout.addWidget(self.output, 6, 1)
        # Cryptography portal
        self.portal = QPushButton("Back to portal")
        self.portal.setStyleSheet(button_style)
        self.portal.clicked.connect(self.when_portal)
        layout.addWidget(self.portal)
        # Home menu
        self.back = QPushButton("Back to Home")
        self.back.setStyleSheet(button_style)
        self.back.clicked.connect(self.when_back)
        layout.addWidget(self.back)

    def encrypt(self, text, key):
        text = text.lower().strip()
        key = key.lower().strip()
        vig = ""
        k = len(key)
        for j in range(len(text)):
            if ord(text[j]) in range(97, 123):
                x = (ord(text[j]) - 97) + (ord(key[j%k]) - 97)
                vig += chr((x%26) + 97)
            else:
                vig += text[j]
        return vig

    def decrypt(self, vig, key):
        vig = vig.lower().strip()
        key = key.lower().strip()
        text = ""
        k = len(key)
        for j in range(len(vig)):
            if ord(vig[j]) in range(97, 123):
                x = (ord(vig[j]) - 97) - (ord(key[j%k]) - 97)
                text += chr((x%26) + 97)
            else:
                text += vig[j]
        return text

    def when_encrypt(self):
        text = self.textin.toPlainText()
        key = self.key.text()
        crypted = self.encrypt(text, key)
        self.output.setText(crypted)

    def when_decrypt(self):
        text = self.textin.toPlainText()
        key = self.key.text()
        plain = self.decrypt(text, key)
        self.output.setText(plain)

    def when_portal(self):
        self.upper.display_crypto_main()

    def when_back(self):
        self.upper.display_home()
