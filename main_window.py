import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from home import *

from cryptology.cryptography.main_crypto import *
from cryptology.cryptography.ceasar import *
from cryptology.cryptography.linear import *
from cryptology.cryptography.vigenere import *
from cryptology.cryptography.hill import *
from cryptology.cryptography.rsa import *
from cryptology.cryptography.hash import *

from cryptology.cryptanalysis.main_analysis import *
from cryptology.steganography.main_stegano import *

from cryptology.encodings.main_encodings import *
from cryptology.encodings.binary import *
from cryptology.encodings.morse import *
from cryptology.encodings.color import *
from cryptology.encodings.qrcode import *

from cryptology.pedacrypto.main_peda import *


class MainCryptolog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.title = "Cryptolog v0.1beta"
        self.left = 60
        self.top = 60
        self.width = 1100
        self.height = 600
        self.toolbar_icon_size = 30
        self.init_ui()

        # Related sub windows
        self.windows = QStackedWidget()
        self.home = Home(self)
        self.windows.addWidget(self.home)

        # Main portals
        self.crypto_main = MainCrypto(self)
        self.windows.addWidget(self.crypto_main)
        self.analysis_main = MainAnalysis(self)
        self.windows.addWidget(self.analysis_main)
        self.stegano_main = MainStegano(self)
        self.windows.addWidget(self.stegano_main)
        self.encoding_main = MainEncoding(self)
        self.windows.addWidget(self.encoding_main)
        self.peda_main = MainPeda(self)
        self.windows.addWidget(self.peda_main)

        # Cryptographic algorithms
        self.ceasar_crypto = CeasarCrypto(self)
        self.windows.addWidget(self.ceasar_crypto)
        self.linear_crypto = LinearCrypto(self)
        self.windows.addWidget(self.linear_crypto)
        self.vigenere_crypto = VigenereCrypto(self)
        self.windows.addWidget(self.vigenere_crypto)
        self.hill_crypto = HillCrypto(self)
        self.windows.addWidget(self.hill_crypto)
        self.rsa_crypto = RSACrypto(self)
        self.windows.addWidget(self.rsa_crypto)
        self.hash_crypto = HashCrypto(self)
        self.windows.addWidget(self.hash_crypto)

        # Data encoding systems
        self.binary_code = BinaryCode(self)
        self.windows.addWidget(self.binary_code)
        self.morse_code = MorseCode(self)
        self.windows.addWidget(self.morse_code)
        self.color_code = ColorCode(self)
        self.windows.addWidget(self.color_code)
        self.qr_code = QRCode(self)
        self.windows.addWidget(self.qr_code)

        self.setCentralWidget(self.windows)

    def init_ui(self, parent=None):
        # General layout
        self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)
        self.setMinimumWidth(self.width)
        self.setMinimumHeight(self.height)

        # Create a menu bar
        menu = self.menuBar()

        # Create a root menu
        file_menu = menu.addMenu('File')
        edit_menu = menu.addMenu('Edit')
        crypt_menu = menu.addMenu('Operator')
        algorithms_menu = menu.addMenu('Teacher')
        about_menu = menu.addMenu('About')

        """ Create actions for file menu """
        new_action = QAction(QtGui.QIcon("img/icon.png"), "New", self)
        new_action.setShortcut('Ctrl+N')
        new_action.setStatusTip('New sheet')
        new_action.triggered.connect(self.new_file)

        open_action = QAction(QtGui.QIcon("img/icon.png"), "Open sheet", self)
        open_action.setShortcut("Ctrl+O")
        open_action.setStatusTip("Open sheet")

        save_action = QAction(QtGui.QIcon("img/icon.png"), "Save sheet", self)
        save_action.setShortcut("Ctrl+S")
        save_action.setStatusTip("Save sheet")

        quit_action = QAction(QtGui.QIcon("img/icon.png"), "Quit", self)
        quit_action.setShortcut("Ctrl+Q")
        quit_action.setStatusTip("Quit")
        quit_action.triggered.connect(self.quit)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(quit_action)

        """ Create actions for edit menu """
        undo_action = QAction(QtGui.QIcon("img/icon.png"), "Undo", self)
        undo_action.setShortcut("Ctrl+Z")
        undo_action.setStatusTip("Undo")

        redo_action = QAction(QtGui.QIcon("img/icon.png"), "Redo", self)
        redo_action.setShortcut("Ctrl+Shift+Z")
        redo_action.setStatusTip("Redo")

        preferences = QAction(QtGui.QIcon("img/icon.png"), "Preferences", self)
        preferences.setShortcut("Ctrl+P")
        preferences.setStatusTip("Preferences")

        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)
        edit_menu.addAction(preferences)

        #Create a statusbar
        self.statusBar().showMessage("Status Bar")

        # Create Tool Bar
        self.toolbar = self.addToolBar("ToolBar")

        # Add The Actions To Tool Bar
        self.toolbar.addAction(new_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(open_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(save_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(undo_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(redo_action)
        self.toolbar.addSeparator()
        self.toolbar.setStyleSheet("background-color: rgb(250, 250, 250)")
        self.toolbar.setIconSize(QSize(self.toolbar_icon_size, self.toolbar_icon_size))

        # Create Vertical Layout for MenuBar
        self.mb_vboxlayout = QVBoxLayout(self)
        self.mb_hboxlayout = QHBoxLayout()

        # Add Menu Bar to Vertical Layout
        self.mb_hboxlayout.addWidget(menu)
        self.mb_vboxlayout.addLayout(self.mb_hboxlayout)

        self.showMaximized()

    ##### Menu functions #####
    # function for new file
    def new_file(self):
        print("New file function called !")

    # function to quit the GUI
    def quit(self):
        if QMessageBox.question(self,"Cryptolog", "Do you want to exit?",
                                QMessageBox.No | QMessageBox.Yes) == QMessageBox.Yes:
            self.close()

    ##### Sub windows #####
    # display home menu
    def display_home(self):
        self.setWindowTitle(self.title)
        self.windows.setCurrentWidget(self.home)

    # display cryptography portal
    def display_crypto_main(self):
        self.windows.setCurrentWidget(self.crypto_main)

    # display cryptanalysis portal
    def display_analysis_main(self):
        self.windows.setCurrentWidget(self.analysis_main)

    # display steganography portal
    def display_stegano_main(self):
        self.windows.setCurrentWidget(self.stegano_main)

    # display encodings portal
    def display_encoding_main(self):
        self.windows.setCurrentWidget(self.encoding_main)

    # display peda-crypto portal
    def display_peda_main(self):
        self.windows.setCurrentWidget(self.peda_main)

    # display ceasar crypto section
    def display_ceasar_crypto(self):
        self.setWindowTitle(self.ceasar_crypto.title)
        self.windows.setCurrentWidget(self.ceasar_crypto)

    # display linear crypto section
    def display_linear_crypto(self):
        self.windows.setCurrentWidget(self.linear_crypto)

    # display vigenere crypto section
    def display_vigenere_crypto(self):
        self.windows.setCurrentWidget(self.vigenere_crypto)

    # display hill crypto section
    def display_hill_crypto(self):
        self.windows.setCurrentWidget(self.hill_crypto)

    # display rsa crypto section
    def display_rsa_crypto(self):
        self.windows.setCurrentWidget(self.rsa_crypto)

    # display hash crypto section
    def display_hash_crypto(self):
        self.windows.setCurrentWidget(self.hash_crypto)

    # display binary code section
    def display_binary_code(self):
        self.windows.setCurrentWidget(self.binary_code)

    # display morse code section
    def display_morse_code(self):
        self.windows.setCurrentWidget(self.morse_code)

    # display color code section
    def display_color_code(self):
        self.windows.setCurrentWidget(self.color_code)

    # display QR code section
    def display_qr_code(self):
        self.windows.setCurrentWidget(self.qr_code)


app = QApplication(sys.argv)
main_window = MainCryptolog()
sys.exit(app.exec_())
