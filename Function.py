# -*- coding: utf-8 -*-
import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTreeWidgetItem
from view import Ui_MainWindow
from ftplib import FTP


class function(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # /DiskA/OpenCNC/NcFiles

    def msg_box(self, msg):
        msgBox = QMessageBox()
        msgBox.question(self, 'NcUpLoader', msg, msgBox.Ok)

    def Ftp_client(self, device):
        host = device.strip()
        ftp = FTP(host)
        try:
            ftp.login('', '')
            self.CNC_status.setText('连接成功')
            return ftp
        except(UnicodeDecodeError):
            pass

    def Ftp_Path_list(self, host):
        ftp = self.Ftp_client(host)
        path = ftp.nlst('/')
        print(path)

    def btnFunc(self):
        device = self.IpAddressEdit.text()
        if device != '':
            self.Ftp_Path_list(device)

        else:
            msg = "设备IP地址为空，请填入设备IP地址！   "
            self.msg_box(msg)
