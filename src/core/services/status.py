#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re, os
from subprocess import Popen, PIPE
from pprint import pprint
from PyQt4.QtCore import QProcess, SIGNAL

class Services ():
    def __init__(self):
        self.service_bin = '/usr/bin/service'
        self.services = ('apache2', 'mysql', 'postfix', 'ssh', 'postgresql')
        self.initd = "/etc/init.d/"
        self.proceso = QProcess()
        self.proceso.connect(self.proceso, SIGNAL("readyReadStandardOutput()"), self.readStdout)
        
    def readStdout(self):
        self.mensaje = self.proceso.readAllStandardOutput()
        
    def apache(self):
        status = None
        run = False
        
        if not os.path.isfile(self.initd + self.services[0]):
            status = "No Instalado"
        else:
            run = True
            
        if run:
            #apacheStatus = Popen(self.service_bin + ' ' + self.services[0] + ' status', stdout=PIPE, shell=True).communicate()[0]
            self.proceso.start(self.service_bin + ' ' + self.services[0] + ' status')
            self.proceso.waitForFinished()
            apacheStatus = self.mensaje
            resultado = re.search('NOT running', apacheStatus)
            if resultado:
                status = 'detenido'
            else:
                status = 'ejecutandose'
        
        return status
        
    def mysql(self):
        status = None
        run = False
        
        if not os.path.isfile(self.initd + self.services[1]):
            status = "No Instalado"
        else:
            run = True
            
        if run:
            #mysqlStatus = Popen(self.service_bin + ' ' + self.services[1] + ' status', stdout=PIPE, shell=True).communicate()[0]
            self.proceso.start(self.service_bin + ' ' + self.services[1] + ' status')
            self.proceso.waitForFinished()
            mysqlStatus = self.mensaje
            resultado = re.search('stop/waiting', mysqlStatus)
            if resultado:
                status = 'detenido'
            else:
                status = 'ejecutandose'
            
        return status
        
    def postfix(self):
        status = None
        run = False
        
        if not os.path.isfile(self.initd + self.services[2]):
            status = "No Instalado"
        else:
            run = True
            
        if run: 
            #postfixStatus = Popen(self.service_bin + ' ' + self.services[2] + ' status', stdout=PIPE, shell=True).communicate()[0]
            self.proceso.start(self.service_bin + ' ' + self.services[2] + ' status')
            self.proceso.waitForFinished()
            postfixStatus = self.mensaje
            resultado = re.search('not running', postfixStatus)
            if resultado:
                status = 'detenido'
            else:
                status = 'ejecutandose'
                
        return status
        
    def ssh(self):
        status = None
        run = False
        
        if not os.path.isfile(self.initd + self.services[3]):
            status = "No Instalado"
        else:
            run = True
            
        if run:
            #sshStatus = Popen(self.service_bin + ' ' + self.services[3] + ' status', stdout=PIPE, shell=True).communicate()[0]
            self.proceso.start(self.service_bin + ' ' + self.services[3] + ' status')
            self.proceso.waitForFinished()
            sshStatus = self.mensaje
            resultado = re.search('stop/waiting', sshStatus)
            if resultado:
                status = 'detenido'
            else:
                status = 'ejecutandose'
            
        return status
    
    def postgresql(self):
        status = None
        run = False
        
        if not os.path.isfile(self.initd + self.services[4]):
            status = "No Instalado"
        else:
            run = True
            
        if run:
            #postgreStatus = Popen(self.service_bin + ' ' + self.services[4] + ' status', stdout=PIPE, shell=True).communicate()[0]
            self.proceso.start(self.service_bin+ ' ' + self.services[4] + ' status')
            self.proceso.waitForFinished()
            postgreStatus = self.mensaje
            resultado = re.search('stop/waiting', postgreStatus)
            if resultado:
                status = 'detenido'
            else:
                status = 'ejecutandose'
            
        return status