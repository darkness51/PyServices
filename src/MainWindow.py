#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from gui.Ui_MainWindow import Ui_Dialog

class MainWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle('Monitor de Servicios')