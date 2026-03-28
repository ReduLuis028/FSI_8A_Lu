**Challenge**
	
**Description**
	Help us test the form by submiting the username as `test` and password as `test!`
	The website running [here](http://saturn.picoctf.net:62853/).
	**Hints**
		1. any redirections?

**Solution**
	1. Se accede al sitio y se inicia sesión con las credenciales `test:test!`.
		http://saturn.picoctf.net:62853/
	2. Después del login, el sitio realiza **múltiples redirecciones**.
		http://saturn.picoctf.net:62853/next-page/id=cGljb0NURntwcm94aWVzX2Fs
		http://saturn.picoctf.net:62853/next-page/id=bF90aGVfd2F5X2QxYzBiMTEyfQ==
	3. Donde llega al sitio final, en el cual no se puede hacer mucho:
		http://saturn.picoctf.net:62853/home
	4. Al observar las URLs, se detecta un parámetro `id` igual a valores en **Base64**:
	    - `cGljb0NURntwcm94aWVzX2Fs`
	    - `bF90aGVfd2F5X2QxYzBiMTEyfQ==`
	5. Se decodifican ambos valores ([[Archivos 05/solve_base64.py]]):
	    - `cGljb0NURntwcm94aWVzX2Fs` → `picoCTF{proxies_al`
	    - `bF90aGVfd2F5X2QxYzBiMTEyfQ==` → `l_the_way_d1c0b112}`
	6. Se concatenan los resultados para obtener la flag completa:
		`picoCTF{proxies_all_the_way_d1c0b112}`.

**Notes**
	1. El uso de Base64 en URLs **no protege información**, solo la codifica.
	2. Las redirecciones pueden ocultar datos sensibles si no se validan correctamente.
	3. Es importante inspeccionar (F12) el tráfico (Network) para detectar este tipo de comportamiento, y que se logra preciar como se redirige a través de los sitios.

**References**
	