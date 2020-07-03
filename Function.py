# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow
from view import Ui_MainWindow

class function(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # /DiskA/OpenCNC/NcFiles

