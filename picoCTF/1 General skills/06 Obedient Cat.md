**Reto
	
**Descripción
	This file has a flag in plain sight (aka "in-the-clear").[flag](https://challenge-files.picoctf.net/c_wily_courier/1a44abd1b8ea719b212d4645d5e9805a9db2e9062845609829d5d15e8e7d578c/flag)
	
**Solución
	1. Usando la terminal y comandos de Windows ```
		C:\Users\luise\Downloads>type flag
		picoCTF{s4n1ty_v3r1f13d_9b8fa0bc}
		```
	2. Usando código Python en terminal de Windows
		C:\Users\luise\Downloads>python
		Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
		Type "help", "copyright", "credits" or "license" for more information.
		```print(open("flag").read())
		picoCTF{s4n1ty_v3r1f13d_9b8fa0bc} ```

	3. Usando terminal de picoCTF
```
		Lui5-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_wily_courier/1a44abd1b8ea719b212d4645d5e9805a9db2e9062845609829d5d15e8e7d578c/flag
		--2026-02-09 18:45:58--  https://challenge-files.picoctf.net/c_wily_courier/1a44abd1b8ea719b212d4645d5e9805a9db2e9062845609829d5d15e8e7d578c/flag
		Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.64, 3.160.5.18, 3.160.5.95, ...
		Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.64|:443... connected.
		HTTP request sent, awaiting response... 200 OK
		Length: 34 [application/octet-stream]
		Saving to: 'flag'
		
		flag                  100%[=======================>]      34  --.-KB/s    in 0s      
		
		2026-02-09 18:45:58 (21.4 MB/s) - 'flag' saved [34/34]
		
		Lui5-picoctf@webshell:~$ cat flag
		picoCTF{s4n1ty_v3r1f13d_9b8fa0bc}
		Lui5-picoctf@webshell:~$ 
```

**Notes
	4. Solucion de terminal de Windows
		`type` es un comando de Windows que **muestra el contenido de un archivo de texto** en pantalla.  
		El reto dice que la flag está “en claro”, así que basta con leer el archivo
	5. Solucion en Python
		- `open("flag")` → abre el archivo
		- `.read()` → lee todo el contenido
		- `print()` → lo muestra en pantalla

**Referencias
	