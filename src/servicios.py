#!/usr/bin/env python
from core.services.status import Services

def main():
    servicios = Services()
    print "El estado de apache es: %s" % servicios.apache()
    print "El estado de mysql es: %s" % servicios.mysql()
    print "El estado de postfix es: %s" % servicios.postfix()
    print "El estado de SSH es: %s" %servicios.ssh()
    print "El estado de PostgreSQL es: %s" %servicios.postgresql()

if __name__ == "__main__":
    main()
    