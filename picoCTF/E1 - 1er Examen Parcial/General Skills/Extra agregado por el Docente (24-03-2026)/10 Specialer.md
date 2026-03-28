**Challenge**
	
**Description**
	Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we took out spell checker because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most. Please start an instance to test your very own copy of Specialer.
	`ssh -p 60787 ctf-player@saturn.picoctf.net`.
	The password is `3f39b042`
	**Hints**
		1. What programs do you have access to?

**Solution**
	1. Obtención de la bandera:
		<script class = "CLI Command Prompt">
			C:\Users\luise>ssh -p 60787 ctf-player@saturn.picoctf.net
			The authenticity of host '[saturn.picoctf.net]:60787 ([13.59.203.175]:60787)' can't be established.
			ED25519 key fingerprint is SHA256:lMXKIC17ONzyUJx7ZYBY5VSwoxCz20uq5/Nm+IhXKew.
			This host key is known by the following other names/addresses:
			    C:\Users\luise/.ssh/known_hosts:8: [saturn.picoctf.net]:58635
			Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
			Warning: Permanently added '[saturn.picoctf.net]:60787' (ED25519) to the list of known hosts.
			ctf-player@saturn.picoctf.net's password:
			Specialer$ /*/*
			/home/ctf-player: /home/ctf-player: Is a directory
			Specialer$ ./???/*
			-bash: ./ala/kazam.txt: Permission denied
			Specialer$ echo /*/*
			/bin/bash /home/ctf-player /lib/terminfo /lib/x86_64-linux-gnu /lib64/ld-linux-x86-64.so.2
			Specialer$ echo /*
			/bin /home /lib /lib64
			Specialer$ echo /home/*
			/home/ctf-player
			Specialer$ echo /home/ctf-player/*
			/home/ctf-player/abra /home/ctf-player/ala /home/ctf-player/sim
			Specialer$ echo /home/ctf-player/ala/*
			/home/ctf-player/ala/kazam.txt /home/ctf-player/ala/mode.txt
			Specialer$ echo "$(</home/ctf-player/ala/mode.txt)"
			Yummy! Ice cream!
			Specialer$ echo "$(</home/ctf-player/ala/kazam.txt)"
			return 0 picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_811ae7e9}
			Specialer$
		</script>
	2. Comandos usados:
		1. `/*/*`
		2. `./???/*`
		3. `echo /*/*`
		4. `echo /*`
		5. `echo /home/*`
		6. `echo /home/ctf-player/*`
		7. `echo /home/ctf-player/ala/*`
		8. `echo "$(</home/ctf-player/ala/mode.txt)"`
		9. `echo "$(</home/ctf-player/ala/kazam.txt)"`
	3. Bandera: `picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_811ae7e9}`.

**Notes**
	1. El reto se basa en un _shell restringido_ donde muchas herramientas básicas (como `ls` o `cat`) no están disponibles, por lo que el objetivo es aprovechar las capacidades propias de Bash:
		1. Uso de **expansión de comodines** (`*` y `?`) para explorar el sistema sin conocer nombres exactos de archivos o directorios.  
			- `/*/*
			- `./???/*`
		2. Enumeración indirecta del contenido del sistema mediante `echo` en lugar de `ls`.
			- `echo /*`
			- `echo /home/*`
			- `echo /home/ctf-player/*`
		3. Localización de archivos relevantes recorriendo rutas con patrones, hasta encontrar el archivo objetivo:
		    - `/home/ctf-player/ala/kazam.txt`
		4. Lectura de archivos mediante **expansión de comando en Bash**, evitando `cat`:
		    - `echo "$(<ruta/del/archivo)"`
			    - `< archivo` lee el contenido del archivo.
				- `$(...)` ejecuta esa lectura dentro de `echo`.
				- `echo` muestra el contenido en pantalla.
		5. Aprovechamiento de rutas absolutas para evitar errores por directorio actual.
		6. Identificación de archivos útiles dentro de subdirectorios accesibles y lectura directa de su contenido.
	3. En este tipo de entornos:
		1. No se depende de comandos clásicos.
		2. Se explora el sistema usando únicamente capacidades internas del shell.
		3. La clave es combinar **globbing + redirección de entrada (`<`)** para acceder a información restringida.
	4. Finalmente, el uso correcto de la ruta completa permitió leer el archivo y obtener la bandera.

**References**
	