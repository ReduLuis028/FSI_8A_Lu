**Challenge**
	
**Description**
	Python scripts are invoked kind of like programs in the Terminal...Can you run [ende.py](https://challenge-files.picoctf.net/c_wily_courier/127cb8c34891ed49ec4c6989a4e55345c8ea50cc744dfd4a578c29f6d16b44cb/ende.py) using [password.txt](https://challenge-files.picoctf.net/c_wily_courier/127cb8c34891ed49ec4c6989a4e55345c8ea50cc744dfd4a578c29f6d16b44cb/password.txt) to get [flag.txt.en](https://challenge-files.picoctf.net/c_wily_courier/127cb8c34891ed49ec4c6989a4e55345c8ea50cc744dfd4a578c29f6d16b44cb/flag.txt.en)?
	**Hints**
		1. Get the Python script accessible in your shell by entering the following command in the Terminal prompt: $ wget followed by a link to the script. The link can be copied from the details section.
		2. $ man python

**Solution**
	1. Descargar los archivos.
	2. Verificar y analizar el código Python:
		- **Convierte la contraseña en una clave** 
			La contraseña se pasa a base64.
		    `ssb_b64 = base64.b64encode(sim_sala_bim.encode())`
		- **Crea un objeto de cifrado**
			Usa esa clave para inicializar el cifrado/desencriptado.
		    `c = Fernet(ssb_b64)`
		- **Lee el archivo cifrado**
		    `data = f.read()`
		- **Desencripta los datos**
		    Usa la clave para obtener el contenido original.
		    `data_c = c.decrypt(data.encode())`
		- **Imprime el resultado**
		    `sys.stdout.buffer.write(data_c)`
	3. Uso de la terminal
		<script class = "CLI Powershell">
			PS G:\Mi unidad\Ingeniería en Computación\IC 9no Semestre\Optativa VII Fundamentos de la Seguridad de la Información\FSI_8A_Lu\picoCTF\E1 - 1er Examen Parcial\General Skills\Extra agregado por el Docente (24-03-2026)\Archivos 08> Get-Content password.txt | python ende.py -d flag.txt.en
			Please enter the password:picoCTF{4p0110_1n_7h3_h0us3_9c5f9bcf}
		</script>

**Notes**
	1. `Get-Content password.txt`
		Lee el contenido del archivo `password.txt`.
		- Si el archivo tiene una línea:
		    `my_password`
		    eso es lo que devuelve.
	2. Pipe `|` (tubería).
		- Toma la salida del comando de la izquierda.
		- Y la envía como entrada al de la derecha.
	3. `python ende.py -d flag.txt.en`
		1. Ejecuta el script de Python:
			**Se leen los argumentos**, dentro del script:
				`sys.argv`	queda así: ["ende.py", "-d", "flag.txt.en"]
		2. `-d` → modo **decrypt**
			- **El programa detecta el modo**
			    `if sys.argv[1] == "-d":`
			    Entra en el bloque de **desencriptar**
			- **Toma el archivo**
			    `with open(sys.argv[2], "r") as f:`
			    Abre `flag.txt.en`
			- **Obtiene la contraseña** (Punto 2 de la **Solution**)
			    `sim_sala_bim = input(...)`
		3. `flag.txt.en` → archivo cifrado

**References**
	