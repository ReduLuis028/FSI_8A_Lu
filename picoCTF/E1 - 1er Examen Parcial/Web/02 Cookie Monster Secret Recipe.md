**Challenge**
	
**Description**
	Cookie Monster has hidden his top-secret cookie recipe somewhere on his website. As an aspiring cookie detective, your mission is to uncover this delectable secret. Can you outsmart Cookie Monster and find the hidden recipe?
	You can access the Cookie Monster [here](http://verbal-sleep.picoctf.net:57709/) and good luck
	**Hints**
		1. Sometimes, the most important information is hidden in plain sight. Have you checked all parts of the webpage?
		2. Cookies aren't just for eating - they're also used in web technologies!
		3. Web browsers often have tools that can help you inspect various aspects of a webpage, including things you can't see directly.

**Solution**
	1. Inspeccionando la pagina medinte DevTools (F12) ir a `Application` → `Storage` → `Cookies` (clicar o revisar el dominio del puerto http://verbal-sleep.picoctf.net:57709) y ahí es donde se encuentra la cookie en bse64:
		![[Archivos 02/Screenshot 2026-03-20 120856.png]]
	2. Usando Pyhton para decodificar la cookie [[Archivos 05/solve_base64.py]]
		<script>
			C:\Users\luise>python
			Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
			Type "help", "copyright", "credits" or "license" for more information.
			>>> import base64
			>>>
			>>> data = "cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzJDODA0MEVGfQ=="
			>>> decoded = base64.b64decode(data).decode()
			>>>
			>>> print(decoded)
			picoCTF{c00k1e_m0nster_l0ves_c00kies_2C8040EF}
			>>>
		</script>

**Notes**
	1. Las cookies almacenan información del lado del cliente y pueden inspeccionarse desde el navegador.  
	2. Se accede a ellas usando DevTools (F12) → Application/Storage → Cookies.  
	3. También pueden verse con `document.cookie` en la consola.  
	4. Los valores de cookies pueden estar codificados (ej. Base64 o URL encoding).  
	5. Base64 es un método de codificación reversible, común en CTFs.  
	6. URL encoding usa formatos como %3D que deben limpiarse antes de decodificar.  
	7. Es importante revisar todas las partes de la web (HTML, cookies, headers).  
	8. En retos web, la información sensible muchas veces está “oculta a simple vista”.

**References**
	