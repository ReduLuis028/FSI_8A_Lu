**Reto**
	
**Descripción**
	Can you break into this super secure portal? http://fickle-tempest.picoctf.net:51580

**Solución**
	1. Se accede al sitio desde el navegador Chrome.  
	2. Se abre la consola del desarrollador (F12 → Console).  
	3. Se inspecciona el código JavaScript ofuscado.  
	4. Se identifica un arreglo con fragmentos de texto:  
		<html><head>
			<body background="barbed_wire.jpeg">
				<script type="text/javascript">
					  var _0x5a46 = ['daf93}', '_again_4', 'this', "Password Verified", "Incorrect password", 'getElementById', 'value', 'substring', 'picoCTF{', 'not_this'];
					  var flag = ['daf93}', '_again_4', 'this', "Password Verified", "Incorrect password", 'getElementById', 'value', 'substring', 'picoCTF{', 'not_this'];
				</script>
			</body>
		</html>
\
	5. Se observa que la flag puede reconstruirse concatenando  ciertos índices del arreglo.  
	6. En consola del navegador de Chrome se ejecuta (este nombre se puede cambair por una variable más natural):  
		console.log(_0x5a46[8] + _0x5a46[9] +  _0x5a46[1] + _0x5a46[0]);
		console.log(flag[8] + flag[9] +  flag[1] + flag[0]);
	7. Se obtiene la flag directamente.
		picoCTF{not_this_again_4daf93}

**Notes**
	El código estaba ofuscado pero no protegido.
	La validación era completamente del lado del cliente.
	Técnica utilizada: Análisis y reconstrucción de strings en JavaScript.
	Herramienta usada: Consola del navegador.

**Referencias**
	