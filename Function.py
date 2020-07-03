# -*- coding: utf-8 -*-
import os
from PyQt5.QtWidgets import QMainWindow, QFileSystemModel
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from view import Ui_MainWindow

class function(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.model_01 = QFileSystemModel()
        self.model_01.setFilter(QDir.Dirs|QDir.NoDotAndDotDot)
        self.model_01.setRootPath('')
        self.treeView_Local.setModel(self.model_01)
        for col in range(1, 4):
            self.treeView_Local.setColumnHidden(col, True)
        self.treeView_Local.clicked.connect(self.listViewLocal)
        self.model_02 = QStandardItemModel()
        self.listView_Local.setModel(self.model_02)
        # /DiskA/OpenCNC/NcFiles

    def listViewLocal(self, Qmodelidx):
        self.model_02.clear()
        PathData = []
        filePath = self.model_01.filePath(Qmodelidx)
        PathDataName = self.model_02.invisibleRootItem()
        PathDataSet = os.listdir(filePath)
        PathDataSet.sort()
        for Data in range(len(PathDataSet)):
            if os.path.isdir(filePath + '\\' + PathDataSet[Data]) == False:
                PathData.append(PathDataSet[Data])
            elif os.path.isdir(filePath + '\\' + PathDataSet[Data]) == True:
                print('2')
        for get in range(len(PathData)):
            gosData = QStandardItem(PathData[get])
            PathDataName.setChild(get, gosData)
