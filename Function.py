# -*- coding: utf-8 -*-
import os
from PyQt5.QtWidgets import QMainWindow, QFileSystemModel, QFileDialog, QMessageBox
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from view import Ui_MainWindow
from ftplib import FTP


class function(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.getcwd = os.getcwd()
        # /DiskA/OpenCNC/NcFiles

    def msg_box(self, msg):
        msgBox = QMessageBox()
        msgBox.Question(self, 'NcUpLoader', msg, msgBox.Ok)


    def choice_Files(self):
        dir_choice = QFileDialog.getExistingDirectory(self, "选择文件夹", self.getcwd)
        if dir_choice == '':
            return
        else:
            self.LocalPath.setText(dir_choice)

    def Ftp_client(self):
        device = self.IpAddressEdit.text()
        if device != '':
            host = device.strip()
            ftp = FTP(host)
            try:
                ftp.login('', '')
                self.CNC_status.setText('连接成功')
            except(UnicodeDecodeError):
                pass
        elif device == '':
            self.msg_box("设备IP地址为空，请填入设备IP!")

