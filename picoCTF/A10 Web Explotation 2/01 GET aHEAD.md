**Reto**
	
**Descripción**
	Find the flag being held on this server to get ahead of the competition http://wily-courier.picoctf.net:61164/

**Solución**
	1. Usando el navegador Firefox
		Esta solución consiste en realizar llamadas a los métodos POST y GET donde muestran respectivamente Rojo Y Azul, al presionarlos, pero una forma como indica la pista del reto, es usando HEAD donde reenviando una de las solicitudes previas modificandola, es decir, en vez de usar POST(Rojo) o GET(Azul), usaremos HEAD y así el navegador enviará la bandera.
			picoCTF{r3j3ct_th3_du4l1ty_8b13f07}
	2. Usando terminal de Kali Linux
		┌──(kali㉿kali)-[~]
		└─$ curl -s -I HEAD http://wily-courier.picoctf.net:61164/index.php
		HTTP/1.1 200 OK
		Date: Wed, 25 Feb 2026 18:22:13 GMT
		Server: Apache/2.4.38 (Debian)
		X-Powered-By: PHP/7.2.34
		flag: picoCTF{r3j3ct_th3_du4l1ty_8b13f07}
		Content-Type: text/html; charset=UTF-8
		
		                                                                             
		┌──(kali㉿kali)-[~]
		└─$ 

**Notes**
	1. El servidor maneja diferentes métodos HTTP (GET y POST) asociados a los botones Azul y Rojo.
	2. La pista sugiere no limitarse a la “dualidad” GET/POST.
	3. El método **HEAD** devuelve solo los encabezados HTTP, sin el cuerpo de la respuesta.
	4. En este reto, la bandera se encuentra en un encabezado personalizado llamado `flag`.
	5. Al modificar la solicitud y usar el método HEAD, el servidor responde con la bandera en los headers.
	6. Herramientas útiles:
	    6.1. Navegador (modificando método desde DevTools → Network).
	    6.2. `curl` con la opción `-I` para obtener encabezados.
			6.2.1. En curl la opcion `-I` hace que solo se muestren los **encabezados**, sin el HTML.
			6.2.2. En curl la opcion `-S` **Modo silencioso** significa que el programa **no muestra mensajes adicionales en pantalla**
	7. Concepto clave: entender cómo funcionan los métodos HTTP y cómo inspeccionar respuestas del servidor.

**Referencias**
	