**Challenge**
	
**Description**
	Welcome to the challenge! In this challenge, you will explore a web application and find an endpoint that exposes a file containing a hidden flag.
	The application is a simple blog website where you can read articles about various topics, including an article about API Documentation.
	Your goal is to explore the application and find the endpoint that generates files holding the server’s memory, where a secret flag is hidden.
	The website is running [picoCTF News](http://verbal-sleep.picoctf.net:54720/).
	**Hints**
		1. Explore backend development with us
		2. The head was dumped.

**Solution**
	1. Buscar donde se encuentra el archivo.
		- Se accede al sitio principal:  
			http://verbal-sleep.picoctf.net:54720/
		- Se explora la documentación de la API:  
		    http://verbal-sleep.picoctf.net:54720/api-docs/
		- Dentro de la documentación, se identifica el endpoint relacionado con diagnósticos:  
		    http://verbal-sleep.picoctf.net:54720/api-docs/#/Diagnosing/get_heapdump
		- Se prueba directamente el endpoint encontrado:  
		    http://verbal-sleep.picoctf.net:54720/heapdump
		- Esto descarga un archivo `.heapsnapshot` que contiene la memoria del servidor.
	2. Usando CLI:
		<script class = "Windows Powershell">
			PS C:\Users\luise\Downloads> Select-String "picoCTF{.*}" .\heapdump-1774037896456.heapsnapshot | ForEach-Object { $_.Matches.Value }
			picoCTF{Pat!3nt_15_Th3_K3y_a485f162}
			PS C:\Users\luise\Downloads>
		</script>
	3. O abriendo el `.heapsnapshot` en algún editor y hacer `Ctrl + F` para encontrar la bandera.
	4. Bandera: `picoCTF{Pat!3nt_15_Th3_K3y_a485f162}`.

**Notes**
	1. **API (Application Programming Interface)**  
	    - Es la forma en que el frontend se comunica con el backend mediante endpoints (URLs).  
	    - Ejemplo: `/api-docs`, `/heapdump`.
	2. **API Docs (Swagger)**  
	    - Es una interfaz que muestra todos los endpoints disponibles del servidor.  
	    - Sirve para descubrir rutas ocultas o interesantes.
	3. **Endpoint**  
	    - Es una ruta específica del servidor que realiza una acción.  
	    - Ejemplo: `/heapdump`.
	4. **Heap / Memoria**  
	    - Es la memoria donde el programa guarda datos en ejecución (variables, objetos, strings).
	5. **Heapdump (.heapsnapshot)**  
	    - Es un volcado (dump) de la memoria del servidor en un momento dado.  
	    - Puede contener información sensible como:
		    - tokens
		    - contraseñas
		    - flags

**References**
	