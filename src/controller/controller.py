from PyQt5.QtWidgets import QApplication
from src.view import View
import sys


class Controller:
    def __init__(self):
        app = QApplication(sys.argv)

        # Here is an example on how to get screen resolution
        # (this is probably useless but sill...)
        # screen_resolution = app.desktop().screenGeometry()
        # width, height = screen_resolution.width(), screen_resolution.height()

        width, height = 1200, 768

        window = View.MyWindow(width, height)



        sys.exit(app.exec_())
