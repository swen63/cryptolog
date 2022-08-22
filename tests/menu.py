'''
- Trying to alter the window's content
- Conserving the same menu bar
'''

import sys
from PyQt5.QtWidgets import *

class SubWindow1(object):
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(400, 450)
        MainWindow.setWindowTitle("Sub Window 1")
        self.centralwidget = QWidget(MainWindow)
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        self.goto2 = QPushButton('GoTo Win2', self.centralwidget)
        self.goto2.move(50, 350)
        MainWindow.setCentralWidget(self.centralwidget)

class SubWindow2(object):
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(400, 450)
        MainWindow.setWindowTitle("Sub Window 2")
        self.centralwidget = QWidget(MainWindow)
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        self.goto1 = QPushButton('GoTo Win1', self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Cryptolog")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.window1 = SubWindow1()
        self.window2 = SubWindow2()

    def init_ui(self, parent=None):
        # Create a menu bar
        menu = self.menuBar()

        # Create a root menu
        file_menu = menu.addMenu('File')
        edit_menu = menu.addMenu('Edit')
        about_menu = menu.addMenu('About')

        """ Create actions for file menu """
        new_action = QAction(QtGui.QIcon("Icons/new.png"), 'New', self)
        new_action.setShortcut('Ctrl+N')
        new_action.setStatusTip('New document')
        new_action.triggered.connect(self.new_file)

        recent_action = QAction('Recent', self)
        recent_action.setShortcut('Ctrl+R')

        save_action = QAction(QtGui.QIcon("Icons/save.ico"), 'Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save file')

        open_action = QAction(QtGui.QIcon("Icons/Open_file.png"), 'Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open file')
        open_action.triggered.connect(self.file_open)

        quit_action = QAction(QtGui.QIcon("Icons/quit.ico"), 'Quit', self)
        quit_action.setShortcut('Ctrl+Q')

        # Add action to file menu
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(recent_action)
        file_menu.addAction(save_action)
        file_menu.addAction(quit_action)

        # create undo & redo
        undo_action = QAction(QtGui.QIcon("Icons/undo.ico"), 'Undo', self)
        undo_action.setShortcut('Ctrl+Z')
        redo_action = QAction(QtGui.QIcon("Icons/redo.ico"), 'Redo', self)
        redo_action.setShortcut('Ctrl+Shift+Z')

        # create preferences
        preferences_action = QAction(QtGui.QIcon("Icons/preference.png"), 'Preferences', self)
        preferences_action.setShortcut('Ctrl+P')
        preferences_action.setStatusTip('Set up your own preferences')

        # Add action to edit menu
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)
        edit_menu.addAction(preferences_action)

        # Create action for about menu
        developers_action = QAction(QtGui.QIcon("Icons/about.png"), 'Developers', self)
        version_action = QAction(QtGui.QIcon("Icons/about.png"), 'Version', self)
        libraries_action = QAction(QtGui.QIcon("Icons/help.png"), 'Libraries', self)
        shortcuts_action = QAction(QtGui.QIcon("Icons/help.png"), 'Shortcuts', self)

        # Add action to about menu
        about_menu.addAction(developers_action)
        about_menu.addAction(version_action)
        about_menu.addAction(libraries_action)
        about_menu.addAction(shortcuts_action)

        # Add Menu Bar to Vertical Layout
        self.mb_hboxlayout.addWidget(menu)
        self.mb_vboxlayout.addLayout(self.mb_hboxlayout)

        #Create a statusbar
        self.statusBar().showMessage("This is a status bar")

        self.setWindowTitle(self.title)
        self.show()

    def startWindow1(self):
        self.window1.goto2.clicked.connect(self.startWindow2)
        self.show()

    def startWindow2(self):
        self.window1.goto1.clicked.connect(self.startWindow1)
        self.show()
