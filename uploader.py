# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import QTranslator, Qt
from PyQt5.QtWidgets import QApplication
from Function import function


class show_func(function):
    def __init__(self):
        function.__init__(self)
        self.setWindowTitle("NC-UpLoader")
        self.connectBtn.clicked.connect(self.Ftp_client)


def translate():
    translateLoad = QTranslator()
    translateLoad.load('./res/qt_zh_CN.qm')
    return translateLoad


if __name__ == '__main__':
    app = QApplication([])
    translateInstall = translate()
    app.installTranslator(translateInstall)
    win = show_func()
    win.show()
    sys.exit(app.exec_())
