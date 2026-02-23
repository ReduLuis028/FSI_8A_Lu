**Reto**
	
**Descripción**
	Can you find the robots?http://fickle-tempest.picoctf.net:6427

**Solución**
	1. Usando el navegador de Chrome
		El nombre del reto hace referencia a “robots”, lo cual sugiere revisar el archivo estándar: /robots.txt
		Se accede directamente desde el navegador: http://fickle-tempest.picoctf.net:64275/robots.txt
\
	2. Revisión del archivo robots.txt
		El contenido encontrado fue:
			User-agent: *  
			Disallow: /cc6b1.html
			
			Esto indica que existe un archivo oculto llamado: /cc6b1.html
\
	3. Acceso al recurso oculto
		Se accede directamente a: http://fickle-tempest.picoctf.net:64275/cc6b1.html
		En esa página se encuentra la flag del reto.
<html><head>

    <title>Where are the robots</title>

    <link href="https://fonts.googleapis.com/css?family=Monoton|Roboto" rel="stylesheet">

    <link rel="stylesheet" type="text/css" href="style.css">

  <link rel="stylesheet" href="chrome-extension://ihcjicgdanjaechkgeegckofjjedodee/app/content-style.css"></head>

  <body>

    <div class="container">

      <div class="content">

  <p>Guess you found the robots<br>

    <flag>picoCTF{ca1cu1at1ng_Mach1n3s_cc6b1}</flag></p>

      </div>

      <footer></footer>

</div></body></html>

**Notes**
	Se utilizó técnica de enumeración básica de archivos comunes.
	`robots.txt` es un archivo estándar que indica a los bots qué rutas no deben rastrear.
	En CTF es común que contenga rutas ocultas.

**Referencias**
	