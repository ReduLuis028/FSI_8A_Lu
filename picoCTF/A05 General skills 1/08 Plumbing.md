**Reto
	
**Descripción
	Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag?Connect to fickle-tempest.picoctf.net 63055.

**Solución
	1. Usando terminal de picoCTF ```
		Lui5-picoctf@webshell:~$ nc fickle-tempest.picoctf.net 63055 | grep picoCTF
		picoCTF{digital_plumb3r_1eBfC512}
		```
**Notes
	2. Se usa el comando nc para obtener el archivo, después se redirige ('|') al comando grep para obtener l flag
	
**Referencias
	