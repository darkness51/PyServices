# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import QDialog
from core.services.status import Services
from gui.Ui_MainWindow import Ui_Dialog

class MainWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.servicios = Services()
        self.check_apache_status()
        self.check_mysql_status()
        self.check_postfix_status()
        self.check_ssh_status()
        self.check_postgre_status()
        self.connect(self.btnStopAll, SIGNAL("clicked()"), self.servicios.stop_all)
        self.connect(self.btnApacheStart, SIGNAL("clicked()"), self.start_apache)
        self.connect(self.btnApacheStop, SIGNAL("clicked()"), self.stop_apache)
        
    def check_apache_status(self):
        estado = self.servicios.apache()
        if estado == 0:
            self.btnApacheStop.setEnabled(False)
        elif estado == 1:
            self.btnApacheStart.setEnabled(False)
        else:
            self.apacheTab.setEnabled(False)
            
    def check_mysql_status(self):
        estado = self.servicios.mysql()
        if estado == 0:
            self.btnMysqlStop.setEnabled(False)
        elif estado == 1:
            self.btnMysqlStart.setEnabled(False)
        else:
            self.mysqlTab.setEnabled(False)
            
    def check_postfix_status(self):
        estado = self.servicios.postfix()
        if estado == 0:
            self.btnPostfixStop.setEnabled(False)
        elif estado == 1:
            self.btnPostfixStart.setEnabled(False)
        else:
            self.postfixTab.setEnabled(False)
            
    def check_ssh_status(self):
        estado = self.servicios.ssh()
        if estado == 0:
            self.btnSshStop.setEnabled(False)
        elif estado == 1:
            self.btnSshStart.setEnabled(False)
        else:
            self.sshTab.setEnabled(False)
            
    def check_postgre_status(self):
        estado = self.servicios.postgresql()
        if estado == 0:
            self.btnPostgreStop.setEnabled(False)
        elif estado == 1:
            self.btnPostgreStart.setEnabled(False)
        else: 
            self.postgreTab.setEnabled(False)
            
    def start_apache(self):
        self.servicios.run_command('apache2', 'start')
        self.btnApacheStart.setEnabled(False)
        self.btnApacheStop.setEnabled(True)
        
    def stop_apache(self):
        self.servicios.run_command('apache2', 'stop')
        self.btnApacheStart.setEnabled(True)
        self.btnApacheStop.setEnabled(False)
