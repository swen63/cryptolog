from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class LinearCrypto(QWidget):
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
        label = QLabel("Linear cipher algorithm")
        label.setStyleSheet("color: #999999; font-weight: bold; font-size: 30px; font-style: italic;")
        layout.addWidget(label)
        # Description
        label = QLabel("This is a description ...")
        label.setWordWrap(True)
        layout.addWidget(label, 2, 0)
        # Options
        label = QLabel("Encryption/Decryption key :")
        layout.addWidget(label, 3, 0)
        # setting space
        label = QLabel()
        layout.addWidget(label, 3, 1)
        # Key A
        label = QLabel("a = ")
        layout.addWidget(label, 4, 0)
        self.keya = QSpinBox()
        #self.keya.setRange(0, 25)
        self.keya.setValue(5)
        layout.addWidget(self.keya, 4, 1)
        # Key B
        label = QLabel("b = ")
        layout.addWidget(label, 5, 0)
        self.keyb = QSpinBox()
        #self.keyb.setRange(0, 25)
        self.keyb.setValue(2)
        layout.addWidget(self.keyb, 5, 1)
        # Text input
        self.textin = QTextEdit()
        self.textin.setReadOnly(False)
        self.textin.setPlaceholderText("Enter your text here ...")
        layout.addWidget(self.textin, 6, 0)
        # Validation
        self.encrypt = QPushButton("Encrypt")
        self.encrypt.clicked.connect(self.when_encrypt)
        layout.addWidget(self.encrypt, 6, 1)
        self.decrypt = QPushButton("Decrypt")
        self.decrypt.clicked.connect(self.when_decrypt)
        layout.addWidget(self.decrypt, 7, 1)
        # Output
        self.output = QLabel()
        layout.addWidget(self.output, 8, 1)
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

    def crypt(self, text, keya, keyb, decrypt=False):
        text = text.lower().strip()
        keya = int(keya)
        keyb = int(keyb)
        #if decrypt:
        #    key = (26-key) % 26
        out = ""
        for i in range(len(text)):
            if ord(text[i]) in range(97, 123):
                x = ord(text[i])-97
                x = ((x*keya) + keyb) % 26
                x = chr(x+97)
                out += x
            else:
                out += text[i]
        return out

    def when_encrypt(self):
        text = self.textin.toPlainText()
        keya = self.keya.value()
        keyb = self.keyb.value()
        crypted = self.crypt(text, keya, keyb)
        self.output.setText(crypted)

    def when_decrypt(self):
        text = self.textin.toPlainText()
        keya = self.keya.value()
        keyb = self.keyb.value()
        plain = self.crypt(text, keya, keyb, True)
        self.output.setText(plain)

    def when_portal(self):
        self.upper.display_crypto_main()

    def when_back(self):
        self.upper.display_home()
