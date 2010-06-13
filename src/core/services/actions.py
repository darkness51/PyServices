#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

import os

class ServicesActions():
    def __init__(self):
        self.service_bin = '/usr/bin/service'
        self.services = ('apache2', 'mysql', 'postfix', 'ssh')
        
    def run_command (self, service_id, action):
        msg = os.popen(self.service_bin + ' ' + self.services[service_id] + ' ' + action).read()        
