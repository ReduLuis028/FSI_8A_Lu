**Challenge**
	
**Description**
	Why search for the flag when I can make a bookmarklet to print it for me?
	Browse [here](http://titan.picoctf.net:57396/), and find the flag!
	**Hints**
		1. A bookmarklet is a bookmark that runs JavaScript instead of loading a webpage.
		2. What happens when you click a bookmarklet?
		3. Web browsers have other ways to run JavaScript too.

**Solution**
	1. Una vez entrando al [sitio.](http://titan.picoctf.net:57396/)
		La pagina nos muestra lo siguiente [[Archivos 01/index.html]]
	2. En la caja de texto o el etiquetado `<textarea>` nos entrega el siguiente código [[Archivos 01/solve.js]]
		El cual solo hay que ejecutar para conseguir la bandera.
	3. Bandera: `picoCTF{p@g3_turn3r_18d2fa20}`.

**Notes**
	1. Un **bookmarklet** es código JavaScript que se ejecuta directamente en el navegador (normalmente desde la barra de favoritos).
	2. El reto no requiere explotar nada; solo **analizar el código del cliente (JavaScript)**.
	3. Siempre revisar:
	    - Código dentro de `<script>`
	    - Contenido de `<textarea>` (a veces esconden lógica ahí)
	4. El bookmarklet contenía:
	    - Un flag **cifrado**
	    - Una función para **descifrarlo con una clave (`picoctf`)**
	5. Problema común:
	    - **Errores de encoding (UTF-8 vs ANSI)** al copiar la cadena cifrada → produce flags incorrectos
	6. Lección clave:
	    - Muchas veces el flag está en el **frontend (JavaScript/HTML)** y solo hay que analizarlo, no atacar el servidor

**References**
	