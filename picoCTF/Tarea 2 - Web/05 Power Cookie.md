**Reto**
	
**Descripción**
	Can you get the flag?Go to this [website](http://saturn.picoctf.net:63939/) and see what you can discover.

**Solución**
	1. Usando completamente el navegador más extensión Cookie editor
		1.1. http://saturn.picoctf.net:63939/
			<html lang="en"><head>
			    <meta charset="UTF-8">
			    <meta name="viewport" content="width=device-width, initial-scale=1.0">
			    <meta http-equiv="X-UA-Compatible" content="ie=edge">
			    <title>Secure Log In</title>
			  </head>
			  <body>
			    <script src="guest.js"></script>
			
			    <h1>Online Gradebook</h1>
			    <button type="button" onclick="continueAsGuest();">Continue as guest</button>
			</body></html>
		1.2. Una vez en el [website](http://saturn.picoctf.net:63939/) tenemos que existe un sitio llamado [guest.js](http://saturn.picoctf.net:63939/guest.js) donde nos da una pista del que hacer, editar la cookie isAdmin con la extensión, y recargar la misma pagina:
			<html><head><link rel="stylesheet" href="resource://content-accessible/plaintext.css"></head><body><pre>
				function continueAsGuest()
				{
				  window.location.href = '/check.php';
				  document.cookie = "isAdmin=0";
				}
			</pre></body></html>
		1.3. Y así obteniendo la bandera http://saturn.picoctf.net:55811/check.php
			<html><head></head><body>
			<p>picoCTF{gr4d3_A_c00k13_5d2505be}</p>
			</body></html>
	2. Usando completamente el navegador más Burpuite
		Previa  a esta solución hacer lo mismo hasta la inspección del sitio [guest.js](http://saturn.picoctf.net:63939/guest.js) usar Burpsuite para interceptar las solicitudes, y en esa solicitud del punto 1.1 cambiar el valor de la cookie de 0 a 1, asi obteniendo nuevamente la bandera con esta solución
			<html><head></head><body>
			<p>picoCTF{gr4d3_A_c00k13_5d2505be}</p>
			</body></html>

**Notes**
	
**Referencias**
	