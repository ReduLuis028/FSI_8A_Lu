**Challenge**
	
**Description**
	What happens if you have a small exponent? There is a twist though, we padded the plaintext so that (M ** e) is just barely larger than N. Let's decrypt this: [values](https://challenge-files.picoctf.net/c_wily_courier/b61c2229204b98a71ea091b7f3c85b9520289448c2633b160d5f08a3f1bdadd3/values)
	**Hints**
		1. RSA tutorial.
		2. How could having too small an e affect the security of this 2048 bit key?
		3. Make sure you don't lose precision, the numbers are pretty big (besides the e value).
		4. You shouldn't have to make too many guesses
		5. pico is in the flag, but not at the beginning

**Solution**
	1. **Lectura de datos**
	    - Se abre el archivo `ciphertext`.
	    - Se extraen los números con regex.
	    - Se asignan:
	        - `n` → módulo RSA
	        - `c` → ciphertext
	        - `e` → exponente público
	2. **Conversión de tipos**
	    - Se convierten todos los valores a `int` para evitar errores en operaciones matemáticas.
	3. **Ataque aplicado (Small Exponent Attack)**
	    - Se intenta recuperar el mensaje usando raíz cúbica:
	        - Se evalúa:  `m = ∛c`
	    - Se usa: `gmpy2.iroot(c, e)`
	4. **Verificación**
	    - Se comprueba si la raíz es exacta (`exact = True`).
	    - Esto indica que no hubo modular wrap (`m^e < n`).
	5. **Conversión a texto**
	    - El entero recuperado se convierte a bytes:
	        - `to_bytes((bit_length+7)//8, "big")`
	    - Luego se decodifica a ASCII para obtener la flag.
	6. **Ejecución del script** [[Files 01/solveRSA.py]]
	    - Script ejecutado con Python 3.12: `py -3.12 solveRSA.py`
	7. Flag: `picoCTF{e_sh0u1d_b3_lArg3r_92f4d5a5}`.

**Notes**
	

**References**
	