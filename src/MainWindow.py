# -*- coding: utf-8 -*-

from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QMessageBox
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
        self.connect(self.btnStopAll, SIGNAL("clicked()"), self.stop_all_services)
        self.connect(self.btnApacheStart, SIGNAL("clicked()"), self.start_apache)
        self.connect(self.btnApacheStop, SIGNAL("clicked()"), self.stop_apache)
        self.connect(self.btnMysqlStart, SIGNAL("clicked()"), self.start_mysql)
        self.connect(self.btnMysqlStop, SIGNAL("clicked()"), self.stop_mysql)
        self.connect(self.btnPostgreStart, SIGNAL("clicked()"), self.start_postgresql)
        self.connect(self.btnPostgreStop, SIGNAL("clicked()"), self.stop_postgresql)
        self.connect(self.btnSshStart, SIGNAL("clicked()"), self.start_ssh)
        self.connect(self.btnSshStop, SIGNAL("clicked()"), self.stop_ssh)
        self.connect(self.btnPostfixStart, SIGNAL("clicked()"), self.start_postfix)
        self.connect(self.btnPostfixStop, SIGNAL("clicked()"), self.stop_postfix)
        
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
        
    def stop_all_services(self):
        self.servicios.stop_all()
        QMessageBox.information(self, "Informacion", "Todos los servicios se han detenido correctamente!", buttons=QMessageBox.Ok, defaultButton=QMessageBox.Ok)
        self.btnApacheStart.setEnabled(True)
        self.btnApacheStop.setEnabled(False)
        self.btnMysqlStart.setEnabled(True)
        self.btnMysqlStop.setEnabled(False)
        self.btnPostgreStart.setEnabled(True)
        self.btnPostgreStop.setEnabled(False)
        self.btnPostfixStart.setEnabled(True)
        self.btnPostfixStop.setEnabled(False)
        
    def start_mysql(self):
        self.servicios.run_command('mysql', 'start')
        self.btnMysqlStart.setEnabled(False)
        self.btnMysqlStop.setEnabled(True)
        
    def stop_mysql(self):
        self.servicios.run_command('mysql', 'stop')
        self.btnMysqlStart.setEnabled(True)
        self.btnMysqlStop.setEnabled(False)
        
    def start_postgresql(self):
        self.servicios.run_command('postgresql', 'start')
        self.btnPostgreStart.setEnabled(False)
        self.btnPostgreStop.setEnabled(True)
        
    def stop_postgresql(self):
        self.servicios.run_command('postgresql', 'stop')
        self.btnPostgreStart.setEnabled(True)
        self.btnPostgreStop.setEnabled(False)
        
    def start_ssh(self):
        self.servicios.run_command('ssh', 'start')
        self.btnSshStart.setEnabled(False)
        self.btnSshStop.setEnabled(True)
        
    def stop_ssh(self):
        self.servicios.run_command('ssh', 'stop')
        self.btnSshStart.setEnabled(True)
        self.btnSshStop.setEnabled(False)
        
    def start_postfix(self):
        self.servicios.run_command('postfix', 'start')
        self.btnPostfixStart.setEnabled(False)
        self.btnPostfixStop.setEnabled(True)
        
    def stop_postfix(self):
        self.servicios.run_command('postfix', 'stop')
        self.btnPostfixStart.setEnabled(True)
        self.btnPostfixStop.setEnabled(False)
