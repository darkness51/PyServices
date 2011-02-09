PyServices
==========

Gestor de Servicios que todo desarrollador web tiene instalado en su equipo con linux.

![screenshot](http://1.bp.blogspot.com/__2VBN0q45xg/TVIk5QWTvEI/AAAAAAAAAHk/i4BZExpReK0/s320/pyservices.png)

De momento, es capaz de gestionar los siguientes servicios:

  - Apache 2
  - MySQL
  - PostgreSQL
  - SSH
  - Postfix
  
Si un servicio de los anteriores no se encuentra instalado, el programa deshabilita la pestaña. Además, permite para todos los servicios al mismo tiempo.

Lo primero que hay que hacer al clonar el repositorio es ingresar al directorio `src` y luego ejecutar el siguiente comando:

	./create_desktop_file.py
	
Con esto, tendremos fuera de la carpeta `src` un archivo llamado PyServices.desktop que nos servirá para ejecutar nuestra aplicación con los permisos necesarios para que funcione.