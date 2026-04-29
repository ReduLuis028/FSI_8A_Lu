**Challenge**
	
**Description**
	In RSA, a small e value can be problematic, but what about N?
	Can you decrypt this? [values](https://challenge-files.picoctf.net/c_wily_courier/2bbb4086ce95d3e431695877b72b7ea062756cb58e97fb4b5a9f3b61ae21ce28/values)
	**Hints**
		1. Bits are expensive, I used only a little bit over 100 to save money

**Solution**
	1. **Lectura de datos**  
	    Se extraen los valores `n`, `c` y `e` del archivo proporcionado.
	2. **Análisis del problema**  
	    El valor de `n` es pequeño (aprox. 100 bits), lo que permite romper RSA mediante ataques de factorización.
	3. **Factorización de N**  
	    Se obtiene `n = p · q` usando un método de factorización (sin librerías de factorización directa en la implementación final).
	4. **Cálculo de parámetros RSA**  
	    Se calcula:
	    - φ(n) = (p − 1)(q − 1)
	    - d = e⁻¹ mod φ(n)
	5. **Descifrado**  
	    Se obtiene el mensaje con:
	    - m = c^d mod n
	6. **Conversión del resultado**  
	    El número resultante se convierte a bytes y luego a texto ASCII.
	7. **Obtención de la bandera** usando [[Files 02/solveValues.py]]
	    El mensaje decodificado es: `}19ea7cd1_do0g_0n_N_11ams{FTCocip`.
	8. Al invertirlo correctamente se obtiene: `picoCTF{sma11_N_n0_g0od_1dc7ae91}`.
		

**Notes**
	

**References**
	