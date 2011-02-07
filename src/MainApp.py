#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
#from PyQt4.QtCore import
from PyQt4.QtGui import QApplication

from MainWindow import MainWindow

def main():
    app = QApplication(sys.argv)
    mainApp = MainWindow()
    mainApp.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()