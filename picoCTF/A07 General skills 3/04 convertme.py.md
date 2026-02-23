**Reto**
	
**Descripción**
	Run the Python script and convert the given number from decimal to binary to get the flag. [Download Python script](https://artifacts.picoctf.net/c/22/convertme.py)
	
**Solución**
	1. Usando terminal de Windows
		C:\Users\luise\Downloads>py "04 convertme.py"
		If 31 is in decimal base, what is it in binary base?
		Answer: 11111
		That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_762f748e}
		
		C:\Users\luise\Downloads>
/
	2. Abriendo el código y cambiando la sentencia `if` con un condición siempre verdadera (true)
		convertme.py"
		If 33 is in decimal base, what is it in binary base?
		Answer: 1
		That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_762f748e}
/

**Notes**
	1. Conversión de base 10 a base 2.
	2. 31 decimal = 11111 binario.
	3. Refuerza sistemas de numeración.
	4. Valida entrada correcta del usuario.

**Referencias**
	