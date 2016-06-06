from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QMessageBox, QDesktopWidget, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import os


class MyWindow(QMainWindow):
    def __init__(self, width, height):  # Should define attributes here
        super().__init__()
        self.insets = Inset()
        self.initUI(width, height)

    def initUI(self, width, height):  # Initialize the window
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        icon = QIcon(os.getcwd() + "/img/fichier_icone_GS.gif")
        btn.setIconSize(QSize(50, 50))
        btn.setIcon(icon)
        btn.move(50, 50)
        btn.clicked.connect(self.close)

        self.setGeometry(self.insets.left(), self.insets.top(),
                         width - (self.insets.left() + self.insets.right()),
                         height - (self.insets.top() + self.insets.bottom()))
        self.setWindowTitle('Graphsound')
        self.setWindowIcon(QIcon(os.getcwd() + '/img/fichier_icone_GS.gif'))

        self.statusBar().showMessage('This is the status bar, we can show logs here')

        exitAction = QAction(QIcon('img/exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        file = open("conf/basicTheme.conf")
        self.styleConf = file.read()
        self.setStyleSheet(self.styleConf)

        self.center()
        self.showMaximized()

    def clickManager(self):
        print("Omfg, so simple")

    def closeEvent(self, event):
        msgBox = QMessageBox()
        msgBox.setStyleSheet(self.styleConf)

        reply = msgBox.question(self, 'Message',
                                     "Are you sure you want to quit?", msgBox.Yes |
                                     msgBox.No, msgBox.No)

        if reply == msgBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


###################################################################
# The border around the window                                    #
###################################################################
class Inset:
    def __init__(self, aTop=31, aLeft=8, aBottom=8, aRight=8):  # Default values for Windows 8.1
        self._top = aTop
        self._left = aLeft
        self._bottom = aBottom
        self._right = aRight

    def top(self):
        return self._top

    def left(self):
        return self._left

    def bottom(self):
        return self._bottom

    def right(self):
        return self._right
