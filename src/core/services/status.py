#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re, os
#from subprocess import Popen, PIPE
from pprint import pprint
from PyQt4.QtCore import QProcess, SIGNAL

class Services ():
    def __init__(self):
        self.service_bin = '/usr/bin/service'
        self.services = ('apache2', 'mysql', 'postfix', 'ssh', 'postgresql')
        self.initd = "/etc/init.d/"
        self.proceso = QProcess()
        self.proceso.connect(self.proceso, SIGNAL("readyReadStandardOutput()"), self.readStdout)
        self.installed_services = []
        for serv in self.services:
            if os.path.isfile(self.initd + serv):
                self.installed_services.append(serv)
        
    def readStdout(self):
        self.mensaje = self.proceso.readAllStandardOutput()
        
    def apache(self):
        status = None
        run = False
        
        if not os.path.isfile(self.initd + self.services[0]):
            status = 2
        else:
            run = True
            
        if run:
            #apacheStatus = Popen(self.service_bin + ' ' + self.services[0] + ' status', stdout=PIPE, shell=True).communicate()[0]
            self.run_command(self.services[0], 'status')
            apacheStatus = self.mensaje
            resultado = re.search('NOT running', apacheStatus)
            if resultado:
                status = 0
            else:
                status = 1
        
        return status
        
    def mysql(self):
        status = None
        run = False
        
        if not os.path.isfile(self.initd + self.services[1]):
            status = 2
        else:
            run = True
            
        if run:
            #mysqlStatus = Popen(self.service_bin + ' ' + self.services[1] + ' status', stdout=PIPE, shell=True).communicate()[0]
            self.run_command(self.services[1], 'status')
            mysqlStatus = self.mensaje
            resultado = re.search('stop/waiting', mysqlStatus)
            if resultado:
                status = 0
            else:
                status = 1
            
        return status
        
    def postfix(self):
        status = None
        run = False
        
        if not os.path.isfile(self.initd + self.services[2]):
            status = 2
        else:
            run = True
            
        if run: 
            #postfixStatus = Popen(self.service_bin + ' ' + self.services[2] + ' status', stdout=PIPE, shell=True).communicate()[0]
            self.run_command(self.services[2], 'status')
            postfixStatus = self.mensaje
            resultado = re.search('not running', postfixStatus)
            if resultado:
                status = 0
            else:
                status = 1
                
        return status
        
    def ssh(self):
        status = None
        run = False
        
        if not os.path.isfile(self.initd + self.services[3]):
            status = 2
        else:
            run = True
            
        if run:
            #sshStatus = Popen(self.service_bin + ' ' + self.services[3] + ' status', stdout=PIPE, shell=True).communicate()[0]
            self.run_command(self.services[3], 'status')
            sshStatus = self.mensaje
            resultado = re.search('stop/waiting', sshStatus)
            if resultado:
                status = 0
            else:
                status = 1
            
        return status
    
    def postgresql(self):
        status = None
        run = False
        
        if not os.path.isfile(self.initd + self.services[4]):
            status = 2
        else:
            run = True
            
        if run:
            #postgreStatus = Popen(self.service_bin + ' ' + self.services[4] + ' status', stdout=PIPE, shell=True).communicate()[0]
            self.run_command(self.services[4], 'status')
            postgreStatus = self.mensaje
            resultado = re.search('8.4/main', postgreStatus)
            if not resultado:
                status = 0
            else:
                status = 1
            
        return status
    
    def stop_all(self):
        for servicio in self.installed_services:
            self.run_command(servicio, 'stop')
            
    def run_command(self, servicio, accion):
        self.proceso.start(self.service_bin + ' ' + servicio + ' ' + accion)
        self.proceso.waitForFinished()
        