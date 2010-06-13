#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re

class Services ():
    def __init__(self):
        self.service_bin = '/usr/bin/service'
        self.services = ('apache2', 'mysql', 'postfix', 'ssh')
        
    def apache(self):
        apacheStatus = os.popen(self.service_bin + ' ' + self.services[0] + ' status').read()
        resultado = re.search('NOT running', apacheStatus)
        if resultado:
            return 'detenido'
        else:
            return 'ejecutandose'
        
    def mysql(self):
        mysqlStatus = os.popen(self.service_bin + ' ' + self.services[1] + ' status').read()
        resultado = re.search('stop/waiting', mysqlStatus)
        if resultado:
            return 'detenido'
        else:
            return 'ejecutandose'
        
    def postfix(self):
        postfixStatus = os.popen(self.service_bin + ' ' + self.services[2] + ' status').read()
        resultado = re.search('not running', postfixStatus)
        if resultado:
            return 'detenido'
        else:
            return 'ejecutandose'
        
    def ssh(self):
        sshStatus = os.popen(self.service_bin + ' ' + self.services[3] + ' status').read()
        resultado = re.search('stop/waiting', sshStatus)
        if resultado:
            return 'detenido'
        else:
            return 'ejecutandose'