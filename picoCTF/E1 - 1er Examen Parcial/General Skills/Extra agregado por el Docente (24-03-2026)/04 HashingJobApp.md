**Challenge**
	
**Description**
	If you want to hash with the best, beat this test!
	`nc saturn.picoctf.net 54496`
	**Hints**
		1. You can use a commandline tool or web app to hash text
		2. Press Ctrl and c on your keyboard to close your connection and return to the command prompt.

**Solution**
	1. Conectarse al servidor: `nc saturn.picoctf.net 54496`
	2. Un vez dentro calcular el `hash MD5` de la cadena dada por el servidor
		<script class = "Conexion al servior">
			┌──(kali㉿kali)-[~]
			└─$ nc saturn.picoctf.net 54496
			Please md5 hash the text between quotes, excluding the quotes: 'crawl space'
			Answer: 
			a320efce66b14e02f4569a08959ad2e8
			a320efce66b14e02f4569a08959ad2e8
			Correct.
			Please md5 hash the text between quotes, excluding the quotes: 'bad haircut'
			Answer: 
			cdefceb62375fcec3f327834a99e9a58
			cdefceb62375fcec3f327834a99e9a58
			Correct.
			Please md5 hash the text between quotes, excluding the quotes: 'Joan of Arc'
			Answer: 
			19ba425a542946fcf13228d9ddd53139
			19ba425a542946fcf13228d9ddd53139
			Correct.
			picoCTF{4ppl1c4710n_r3c31v3d_674c1de2}
			                                                                             
			┌──(kali㉿kali)-[~]
			└─$ 
		</script>
		<script class = "Calculo del hash MD5">
			┌──(kali㉿kali)-[~]
			└─$ echo -n "crawl space" | md5sum
			a320efce66b14e02f4569a08959ad2e8  -
			                                                                             
			┌──(kali㉿kali)-[~]
			└─$ echo -n "bad haircut" | md5sum
			cdefceb62375fcec3f327834a99e9a58  -
			                                                                             
			┌──(kali㉿kali)-[~]
			└─$ echo -n "Joan of Arc" | md5sum
			19ba425a542946fcf13228d9ddd53139  -
			                                                                             
			┌──(kali㉿kali)-[~]
			└─$ 
		</script>
		Hecho lo anterior el mismo servidor mostrara la bandera.
		![[Archivos 04/Screenshot 2026-03-27 110654.png]]
	3. Bandera: `picoCTF{4ppl1c4710n_r3c31v3d_674c1de2}`.

**Notes**
	1. Un **hash MD5** es una función que:
		- Toma cualquier texto o archivo.
		- Lo convierte en un código fijo de **32 caracteres hexadecimales**.
	2. `echo -n "Backstreet Boys"`:
		- `echo` → imprime texto.
		- `-n` → evita el salto de línea (`\n`).
	3. Pipe `|`:
		- Es una **tubería (pipe)**.
		- Pasa la salida del comando anterior al siguiente .
	4. `md5sum`:
		- Calcula el **hash MD5** de lo que recibe.
		- Devuelve: `<hash>  -`.

**References**
	