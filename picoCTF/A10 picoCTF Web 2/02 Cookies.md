**Reto**
	
**Descripción**
	Who doesn't love cookies? Try to figure out the best one. http://wily-courier.picoctf.net:55588/

**Solución**
	1. Usando navegaor Firefox con extensión Cookies'Editor
		Al ingresar una cookie valida en la página web, retorna que es una cookie, entonces procedemos ver la extensión, donde podemos ver que esa cookie sugerida la inicio tiene un valor 1, y podemos inducir que si cambiamos a un siguiente numero, por ejemplo 2, y recargamos la página nos mostrara otra sugerencia, y así podemos realizarlo, peor esto sería muy tardado...
	2. Usando terminal de Kali Linux par automatizar el proceso el solución previa
		┌──(kali㉿kali)-[~]
		└─$ for i in {1..30}; do
		    curl -s http://wily-courier.picoctf.net:55588/check -H "Cookie: name=$i" | grep pico && echo "Encontrado en: $i"
		done
		            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{3v3ry1_l0v3s_c00k135_a4dadb49}
		Encontrado en: 18

**Notes**
	1. El reto se basa en la manipulación de **cookies HTTP**.
	2. La página asigna una cookie llamada `name` con un valor numérico.
	3. El servidor cambia la respuesta según el valor de esa cookie.
	4. Cambiar manualmente el valor permite descubrir distintas respuestas.
	5. La bandera aparece cuando la cookie tiene el valor correcto (en este caso, 18).
	6. Esto es un ejemplo de **enumeración por fuerza bruta sobre cookies**.
	7. Automatizar con un bucle en `bash` acelera el proceso.
	8. `curl` permite enviar cookies manualmente con la opción `-H "Cookie: ..."`.
	9. Conceptos clave
		9.1. Las cookies almacenan información del lado del cliente.    
		9.2. El servidor puede tomar decisiones basadas en su valor.    
		9.3. Si no hay validación adecuada, pueden manipularse fácilmente.

**Referencias**
	