# -*- coding: utf-8 -*-
import os
from PyQt5.QtWidgets import QMainWindow, QFileSystemModel
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from view import Ui_MainWindow
from ftplib import FTP


class function(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.model_01 = QFileSystemModel()
        self.model_01.setFilter(QDir.Dirs | QDir.NoDotAndDotDot)
        self.model_01.setRootPath('')
        self.treeView_Local.setModel(self.model_01)
        for col in range(3, 4):
            self.treeView_Local.setColumnHidden(col, True)

        # /DiskA/OpenCNC/NcFiles

    def Ftp_client(self):
        host = (self.IpAddressEdit.text()).strip()
        ftp = FTP(host)
        try:
            ftp.login('', '')
            ftp.encoding('ascii').decode('utf-8')
            # path = ftp.cwd('/')
            self.CNC_status.setText('连接成功')
            # self.model_03 = QFileSystemModel()
            # self.model_03.setFilter(QDir.Dirs | QDir.NoDotAndDotDot)
            # self.model_03.setRootPath(path)
            # self.CNC_ListView.setModel(self.model_03)
        except(UnicodeDecodeError):
            pass
