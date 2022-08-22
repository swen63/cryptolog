import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainCryptolog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.title = "Cryptolog v0.1beta"
        self.left = 60
        self.top = 60
        self.width = 1200
        self.height = 600
        self.toolbar_icon_size = 30
        self.init_ui()

        # Related sub windows
        self.win1 = Window1(self)
        self.win2 = Window2(self)
        self.windows = QStackedWidget()
        self.windows.addWidget(self.win1)
        self.windows.addWidget(self.win2)
        self.setCentralWidget(self.windows)

    def init_ui(self, parent=None):
        self.setWindowTitle(self.title)

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

        new_submenu = QMenu('New Sth', self)
        new_doc_action = QAction(QtGui.QIcon("img/icon.png"), "New Document", self)
        new_pic_action = QAction(QtGui.QIcon("img/icon.png"), "New Picture", self)
        new_submenu.addAction(new_doc_action)
        new_submenu.addAction(new_pic_action)

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
        file_menu.addMenu(new_submenu)
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
        self.statusBar().showMessage("This is a status bar")

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
        #self.toolbar.addAction(disposition_action)
        self.toolbar.setStyleSheet("background-color: rgb(250, 250, 250)")
        self.toolbar.setIconSize(QSize(self.toolbar_icon_size, self.toolbar_icon_size))

        # Create Vertical Layout for MenuBar
        self.mb_vboxlayout = QVBoxLayout(self)
        self.mb_hboxlayout = QHBoxLayout()

        # Add Menu Bar to Vertical Layout
        self.mb_hboxlayout.addWidget(menu)
        self.mb_vboxlayout.addLayout(self.mb_hboxlayout)

        self.show()

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
    # function for Sub-Window 1
    def display_window1(self):
        self.windows.setCurrentWidget(self.win1)

    # function for Sub-Window 2
    def display_window2(self):
        self.windows.setCurrentWidget(self.win2)


class Window1(QWidget):
    def __init__(self, window):
        QWidget.__init__(self)
        self.upper = window
        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel("Text label")
        layout.addWidget(label)
        self.msg = QLineEdit()
        self.msg.setPlaceholderText("Enter your msg ...")
        layout.addWidget(self.msg)
        self.button = QPushButton("Change to window 2")
        self.button.setWhatsThis("Press here !")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.when_press)

    def when_press(self):
        self.upper.win2.msgLabel.setText(self.msg.text())
        self.button.clicked.connect(self.upper.display_window2)


class Window2(QWidget):
    def __init__(self, window, msg="nothing"):
        QWidget.__init__(self)
        self.upper = window
        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel("Text label from window 2")
        layout.addWidget(label)
        self.msgLabel = QLabel(msg)
        layout.addWidget(self.msgLabel)
        self.button = QPushButton("Change to window 1")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.upper.display_window1)


app = QApplication(sys.argv)
main_window = MainCryptolog()
sys.exit(app.exec_())
