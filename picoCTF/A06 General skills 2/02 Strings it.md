**Reto**
	
**Descripción**
	Can you find the flag in [file](https://challenge-files.picoctf.net/c_fickle_tempest/285538e2710605958a055500d6573657fcafea6308545cecfabb34462199cfd5/strings) without running it?
	
**Solución**
	1. Usando terminal ed picoCTF
		 Lui5-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_fickle_tempest/285538e2710605958a055500d6573657fcafea6308545cecfabb34462199cfd5/strings
		--2026-02-11 18:23:58--  https://challenge-files.picoctf.net/c_fickle_tempest/285538e2710605958a055500d6573657fcafea6308545cecfabb34462199cfd5/strings
		Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.18, 3.160.5.40, 3.160.5.64, ...
		Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.18|:443... connected.
		HTTP request sent, awaiting response... 200 OK
		Length: 784424 (766K) [application/octet-stream]
		Saving to: 'strings'
		
		strings                     100%[===========================================>] 766.04K  1.83MB/s    in 0.4s    
		
		2026-02-11 18:23:59 (1.83 MB/s) - 'strings' saved [784424/784424]
		
		Lui5-picoctf@webshell:~$ 
		Lui5-picoctf@webshell:~$ strings strings | grep picoCTF
		picoCTF{5tRIng5_1T_1067EC4c}
		Lui5-picoctf@webshell:~$ 

**Notes**
	1. `wget` permite descargar archivos desde una URL directamente en la terminal.
	2. `strings archivo` extrae todas las cadenas de texto legibles dentro de un binario o archivo ejecutable.
	3. El operador `|` (pipe) pasa la salida de un comando como entrada de otro.
	4. `grep 'texto'` busca líneas que contengan un patrón específico dentro de la entrada recibida.
	5. Combinando `strings` y `grep` se puede localizar la flag dentro de un archivo sin ejecutarlo.
	6. Esta técnica es útil para analizar binarios o archivos grandes de forma segura.

**Referencias**