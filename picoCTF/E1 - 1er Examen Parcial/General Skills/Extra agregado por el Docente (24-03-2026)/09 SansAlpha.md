**Challenge**
	
**Description**
	The Multiverse is within your grasp! Unfortunately, the server that contains the secrets of the multiverse is in a universe where keyboards only have numbers and (most) symbols.
	`ssh -p 55893 ctf-player@mimas.picoctf.net`
	Use password: `1db87a14`
	**Hints**
		1. Where can you get some letters?

**Solution**
	1. Obtención de la bandera:
		<script class = "CLI Command Prompt">
			C:\Users\luise>ssh -p 55893 ctf-player@mimas.picoctf.net
			ctf-player@mimas.picoctf.net's password:
			Permission denied, please try again.
			ctf-player@mimas.picoctf.net's password:
			Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.5.0-1016-aws x86_64)
			
			 * Documentation:  https://help.ubuntu.com
			 * Management:     https://landscape.canonical.com
			 * Support:        https://ubuntu.com/advantage
			
			This system has been minimized by removing packages and content that are
			not required on a system that users do not log into.
			
			To restore this content, you can run the 'unminimize' command.
			Last login: Fri Mar 27 22:24:00 2026 from 127.0.0.1
			SansAlpha$ /????/*
			bash: /home/ctf-player: Is a directory
			
			SansAlpha$ /????/??????????/*
			bash: /home/ctf-player/blargh: Is a directory
			
			SansAlpha$ /????/??????????/*/*
			bash: /home/ctf-player/blargh/flag.txt: Permission denied
			
			SansAlpha$ /???/???[!_]64 /????/??????????/*/*
			/bin/base64: extra operand ‘/home/ctf-player/blargh/flag.txt’
			Try '/bin/base64 --help' for more information.
			
			SansAlpha$ /???/???[!_]64 /????/??????????/??????/????????
			cmV0dXJuIDAgcGljb0NURns3aDE1X211MTcxdjNyNTNfMTVfbTRkbjM1NV80OTQ1NjMwYX0=
			
			SansAlpha$
			
			C:\Users\luise>
		</script>
	2. Comandos usados:
		1. `/????/*`
		2. `/????/??????????/*`
		3. `/????/??????????/*/*`
		4. `/???/???[!_]64 /????/??????????/*/*`
		5. `/???/???[!_]64 /????/??????????/??????/????????`
	3. Decodificación de la bandera:
		<script class = "CLI Powershell">
			PS C:\Users\luise> [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("cmV0dXJuIDAgcGljb0NURns3aDE1X211MTcxdjNyNTNfMTVfbTRkbjM1NV80OTQ1NjMwYX0="))
			return 0 picoCTF{7h15_mu171v3r53_15_m4dn355_4945630a}
			PS C:\Users\luise>
		</script>
	4. Bandera: `picoCTF{7h15_mu171v3r53_15_m4dn355_4945630a}`.

**Notes**
	El reto consiste en ejecutar comandos en un entorno donde **no se pueden usar letras**, por lo que se deben emplear **comodines del shell (`*` y `?`)** para construir rutas y comandos sin escribirlos directamente.
	A través de estas técnicas se logra:
		- Explorar directorios usando patrones como `/*` y `/????`.
		- Localizar binarios del sistema sin escribir sus nombres (ej. `/bin/base64`).
		- Ejecutar comandos de forma indirecta mediante expansión del shell.
		- Acceder a archivos restringidos (como `flag.txt`) a través de rutas construidas con patrones:
			- `./*/*`
		- Obtener la salida en formato **Base64** debido a las restricciones de ejecución.
	Finalmente, el contenido obtenido se decodifica fuera del servidor para revelar la bandera.

**References**
	