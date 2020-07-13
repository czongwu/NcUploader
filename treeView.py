# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QTreeWidget


class TreeView(QTreeWidget):
    def __init__(self):
        super(QTreeWidget, self).__init__()
        self.setColumnCount(3)
        self.setHeaderLabels(['名称', '大小', '类型'])