**Challenge**
	General Skills

**Description**
	Can you conjure the right bytes? The program's source code can be downloaded [here](https://challenge-files.picoctf.net/c_lonely_island/f75c06c78a50734a46ec2257851cdc7d2b22fce326bba0308f94ade73d12f0da/app.py).
	Connect to the program with netcat:`$ nc lonely-island.picoctf.net 52777`
	**Hints**
		1. There's no way to print these bytes
		2. Use pwntools to send raw bytes over the network

**Solution**
	1. Comando a utilizar: `(python3 -c "import sys; sys.stdout.buffer.write(b'\xff\xff\xff\n')"; cat) | nc lonely-island.picoctf.net 52777`
	2. Usando terminal de picoCTF
		Lui5-picoctf@webshell:~$ `(python3 -c "import sys; sys.stdout.buffer.write(b'\xff\xff\xff\n')"; cat) | nc lonely-island.picoctf.net 52777`
		⊹──────[ BYTEMANCY-2 ]──────⊹
		☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
		
		Send me the HEX BYTE 0xFF 3 times, side-by-side, no space.
		
		☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
		⊹─────────────⟡─────────────⊹
		==> picoCTF{3ff5_4_d4yz_9a6da265}

**Notes**
	1. Con el **código fuente disponible**, se analiza la lógica del programa para determinar la entrada necesaria para obtener la flag.
	2. **Proceso Python** (`python3 -c "import sys; sys.stdout.buffer.write(b'\xff\xff\xff\n')";`): Genera los bytes `FF FF FF` y añade un salto de línea (`\n`) para accionar el "Enter".
		- **Librería** `import sys`: Importa el módulo del sistema para manejar la entrada y salida de bajo nivel (stdin y stdout).
		- `sys.stdout.buffer.write(b'\xff\xff\xff\n')`: Envía los bytes crudos al programa.
			`sys`:
				Módulo de Python que permite interactuar con el sistema: entrada, salida y errores. Aquí se usa para acceder a la **salida estándar** (`stdout`) y escribir bytes directamente.
			`.stdout` (atributo de `sys` que representa la **salida estándar**):
				`stdout` normalmente envía texto a `sys`, no bytes.
				Salida estándar del programa, normalmente lo que se ve en pantalla.
				Ejemplo normal: print("hola") escribe en `stdout`.
			`.buffer` (atributo de `stdout` que representa la **capa binaria** de la salida estándar):
				`.buffer` permite enviar datos binarios a `.stdout`sin convertirlos a texto, exactamente como están en memoria.
			`write()`:
				Función que escribe los datos que le va pasar a `.buffer`.
				Aquí le pasamos bytes puros a la función.
		- `b'\xff\xff\xff\n`': Secuencia de tres bytes con valor 255 seguida de un salto de línea.
			La `b` indica que lo que viene es un **objeto de tipo `bytes`**, no un string de texto, es decir, los valores como `\xff` se interpretan como **bytes con valor 255** al enviarse o usarse, no como caracteres de texto.
			`\xff` → representa el byte 255 en hexadecimal.
			Hay tres bytes \xff seguidos → FF FF FF.
			`\n` → byte de salto de línea, equivalente a presionar Enter.
	3. `;`: Indica la ejecución del comando anterior de si mismo (`import sys`), y después ejecutar el siguiente comando (`sys.stdout...`).
	4. `cat`: Mantiene abierta la conexión para recibir la respuesta del servidor.
	5. **Pipe (`|`):** Conecta la salida del comando con la entrada del programa en el servidor.
	6. `nc`: Conecta con el servidor y envía los datos.
	7. El código del reto compara la entrada recibida con `b"\xff\xff\xff"`. Como no se puede escribir esos bytes desde el teclado, se generan en Python y se envían directamente al servidor mediante `netcat`. Al coincidir, el servidor libera la flag.

**References**
	