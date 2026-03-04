**Reto**
	

**Descripción**
	How about trying to match a regular expression The website is running [here](http://saturn.picoctf.net:62566/).

**Solución**
	1. Se inspecciona el código fuente del sitio.
	2. En el script JavaScript se observa la validación:
		<script>
			function send_request() {
				let val = document.getElementById("name").value;
				// ^p.....F!?
				fetch(`/flag?input=${val}`)
					.then(res => res.text())
					.then(res => {
						const res_json = JSON.parse(res);
						alert(res_json.flag)
						return false;
					})
				return false;
			}
		</script>
	3. La expresión regular indica:
	    - `^` → Inicio de la cadena
	    - `p` → Debe iniciar con la letra **p**
	    - `.....` → Cinco caracteres cualquiera
	    - `F` → Letra **F** mayúscula
	    - `!?` → Puede o no terminar con `!`
	4. Probando combinaciones que coincidan con el patrón, se obtiene la bandera:
		picoCTF{succ3ssfully_matchtheregex_08c310c6}

**Notes**
	1. Siempre revisar el código fuente en retos web.
	2. Las expresiones regulares suelen revelar el formato exacto esperado.
	3. El símbolo `^` indica inicio de cadena.
	4. El `.` representa cualquier carácter.
	5. El `?` indica que el carácter previo es opcional.
	6. Muchas validaciones se hacen del lado del cliente (JavaScript), lo que facilita el análisis.

**Referencias**
	