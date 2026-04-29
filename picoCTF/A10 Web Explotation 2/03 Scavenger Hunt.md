**Reto**
	
**Descripción**
	There is some interesting information hidden around this site. Can you find it? http://wily-courier.picoctf.net:64034/

**Solución**
	1. Usando cualquier navegador, pero en este caso Firefox
		Navegando manualmente por distintas rutas del sitio, tanto visibles como ocultas, inspeccionando el código fuente de la página, revisando archivos estáticos como CSS y accediendo directamente a rutas comunes del servidor (por ejemplo `robots.txt`, `.htaccess` o `.DS_Store`), con el objetivo de identificar información expuesta que no aparece directamente en la interfaz principal.
		
		Parte 1 (http://wily-courier.picoctf.net:64034/): <!-- Here's the first part of the flag: picoCTF{t -->
		Parte 2 (http://wily-courier.picoctf.net:64034/mycss.css): /* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
		Parte 3 (http://wily-courier.picoctf.net:64034/robots.txt): t_0f_pl4c
		Parte 4 (http://wily-courier.picoctf.net:64034/.htaccess) .htaccess: 3s_2_lO0k
		Parte 5 (http://wily-courier.picoctf.net:64034/.DS_Store): Congrats! You've completed the scavenger hunt! Part 5: _9588550}
		picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_9588550}

**Notes**
	1. El reto consiste en una búsqueda de información oculta (scavenger hunt) dentro del sitio web.
	2. La bandera está dividida en varias partes distribuidas en distintos recursos del servidor.
	3. Ver el código fuente HTML (comentarios <!-- -->).
	4. Revisar archivos CSS.
	5. Consultar archivos comunes del servidor como:
		***robots.txt*** → indica rutas que los bots no deberían indexar.
		***.htaccess*** → archivo de configuración de Apache.
		***.DS_Store*** → archivo generado por macOS que puede exponer información.
	6. No hubo explotación compleja, sino reconocimiento y enumeración de archivos comunes.
	7. Es un ejemplo de:
	8. Information Disclosure
	9. Mala configuración del servidor
	10. Exposición de archivos sensibles
	11. Conceptos clave
		11.1. Reconocimiento (Reconnaissance): buscar archivos y rutas interesantes.
		11.2. Archivos ocultos pueden contener información sensible si el servidor no los restringe.
		11.3. Muchos retos web se resuelven revisando:
			Código fuente
			Archivos estáticos
			Rutas típicas del sistema

**Referencias**
	