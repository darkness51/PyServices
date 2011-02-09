#!/usr/bin/env python

import os, re

def main():
    contenido = ''
       
    try:
        f = open("../template.txt", 'r')
        d = open("../PyServices.desktop", 'w+')
    except IOError:
        print "Error al leer el fichero"
        
    for line in f:
        r = re.search('Exec', line)
        if r:
            contenido += "Exec=" + os.getcwd() + '/MainApp.py\n'
        else:
            contenido += line
    
    d.write(contenido)
    f.close()
    d.close()    
    
if __name__ == "__main__":
    main()
    