# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from treeView import TreeView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 400)
        MainWindow.setMinimumSize(QtCore.QSize(640, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DeviceIpLabel = QtWidgets.QLabel(self.centralwidget)
        self.DeviceIpLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.DeviceIpLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.DeviceIpLabel.setFont(font)
        self.DeviceIpLabel.setObjectName("DeviceIpLabel")
        self.horizontalLayout.addWidget(self.DeviceIpLabel)
        self.IpAddressEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IpAddressEdit.setMinimumSize(QtCore.QSize(222, 30))
        self.IpAddressEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.IpAddressEdit.setFont(font)
        self.IpAddressEdit.setObjectName("IpAddressEdit")
        self.horizontalLayout.addWidget(self.IpAddressEdit)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.connectBtn = QtWidgets.QPushButton(self.centralwidget)
        self.connectBtn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.connectBtn.setFont(font)
        self.connectBtn.setObjectName("connectBtn")
        self.horizontalLayout_2.addWidget(self.connectBtn)
        self.UpLoaderBtn = QtWidgets.QPushButton(self.centralwidget)
        self.UpLoaderBtn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.UpLoaderBtn.setFont(font)
        self.UpLoaderBtn.setObjectName("UpLoaderBtn")
        self.horizontalLayout_2.addWidget(self.UpLoaderBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.DeviceManageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DeviceManageBtn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.DeviceManageBtn.setFont(font)
        self.DeviceManageBtn.setObjectName("DeviceManageBtn")
        self.horizontalLayout_2.addWidget(self.DeviceManageBtn)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Local = QtWidgets.QLabel(self.centralwidget)
        self.label_Local.setMinimumSize(QtCore.QSize(50, 0))
        self.label_Local.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_Local.setFont(font)
        self.label_Local.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Local.setObjectName("label_Local")
        self.horizontalLayout_3.addWidget(self.label_Local)
        self.LocalPath = QtWidgets.QLineEdit(self.centralwidget)
        self.LocalPath.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.LocalPath.setFont(font)
        self.LocalPath.setObjectName("LocalPath")
        self.horizontalLayout_3.addWidget(self.LocalPath)
        self.ChoiceFileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ChoiceFileBtn.setMinimumSize(QtCore.QSize(50, 30))
        self.ChoiceFileBtn.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.ChoiceFileBtn.setFont(font)
        self.ChoiceFileBtn.setObjectName("ChoiceFileBtn")
        self.horizontalLayout_3.addWidget(self.ChoiceFileBtn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_CNC = QtWidgets.QLabel(self.centralwidget)
        self.label_CNC.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_CNC.setFont(font)
        self.label_CNC.setAlignment(QtCore.Qt.AlignCenter)
        self.label_CNC.setObjectName("label_CNC")
        self.horizontalLayout_4.addWidget(self.label_CNC)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        # self.treeView_Local = TreeView()
        self.treeView_Local = QtWidgets.QTreeView(self.centralwidget)
        self.treeView_Local.setMinimumSize(QtCore.QSize(0, 0))
        self.treeView_Local.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.treeView_Local.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.treeView_Local.setObjectName("treeView_Local")
        self.verticalLayout.addWidget(self.treeView_Local)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.Local_status = QtWidgets.QLabel(self.centralwidget)
        self.Local_status.setObjectName("Local_status")
        self.horizontalLayout_7.addWidget(self.Local_status)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CNC_ListView = TreeView()
        # self.CNC_ListView = QtWidgets.QListView(self.centralwidget)
        self.CNC_ListView.setMinimumSize(QtCore.QSize(0, 0))
        self.CNC_ListView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CNC_ListView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.CNC_ListView.setObjectName("CNC_ListView")
        self.verticalLayout_2.addWidget(self.CNC_ListView)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.CNC_status = QtWidgets.QLabel(self.centralwidget)
        self.CNC_status.setObjectName("CNC_status")
        self.horizontalLayout_5.addWidget(self.CNC_status)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DeviceIpLabel.setText(_translate("MainWindow", "设备IP:"))
        self.connectBtn.setText(_translate("MainWindow", "连接设备"))
        self.UpLoaderBtn.setText(_translate("MainWindow", "程序上传"))
        self.DeviceManageBtn.setText(_translate("MainWindow", "设备管理"))
        self.label_Local.setText(_translate("MainWindow", "本地:"))
        self.ChoiceFileBtn.setText(_translate("MainWindow", "选择"))
        self.label_CNC.setText(_translate("MainWindow", "CNC设备目录"))
        self.Local_status.setText(_translate("MainWindow", "TextLabel"))
        self.CNC_status.setText(_translate("MainWindow", "TextLabel"))

