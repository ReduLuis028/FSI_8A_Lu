**Reto**
	
**Descripción**
	How well can you perfom basic binary operations? Start searching for the flag here `nc titan.picoctf.net 62785`

**Solución**
	1. Usando terminal de picoCTF y usando Calculadora de Windows
		Lui5-picoctf@webshell:~$ nc titan.picoctf.net 62785

		Welcome to the Binary Challenge!"
		Your task is to perform the unique operations in the given order and find the final result in hexadecimal that yields the flag.
		
		Binary Number 1: 01001111
		Binary Number 2: 10011000
		
		
		Question 1/6:
		Operation 1: '|'
		Perform the operation on Binary Number 1&2.
		Enter the binary result: 11011111
		Correct!
		
		Question 2/6:
		Operation 2: '>>'
		Perform a right shift of Binary Number 2 by 1 bits .
		Enter the binary result: 01001100
		Correct!
		
		Question 3/6:
		Operation 3: '+'
		Perform the operation on Binary Number 1&2.
		Enter the binary result: 11100111
		Correct!
		
		Question 4/6:
		Operation 4: '<<'
		Perform a left shift of Binary Number 1 by 1 bits.
		Enter the binary result: 10011110
		Correct!
		
		Question 5/6:
		Operation 5: '&'
		Perform the operation on Binary Number 1&2.
		Enter the binary result: 00001000
		Correct!
		
		Question 6/6:
		Operation 6: '*'
		Perform the operation on Binary Number 1&2.
		Enter the binary result: 10111011101000
		Correct!
		
		Enter the results of the last operation in hexadecimal: 2EE8
		
		Correct answer!
		The flag is: picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_6ab1ad84}

**Notes**
/		1. Operaciones utilizadas:
		|     → *OR* bit a bit: Devuelve 1 si al menos un bit es 1.
		>> → *Desplazamiento a la derecha*: Cada bit se mueve hacia la derecha, el bit más a la derecha se pierde y se agrega 0 a la izquierda.
		+   → *Suma aritmética*: Convertir los binarios a decimal, sumar y luego convertir el resultado a binario.
		<< → *Desplazamiento a la izquierda*: Cada bit se mueve hacia la izquierda, se agrega 0 a la derecha.
		&   → *AND bit a bi*t: Devuelve 1 solo si ambos bits son 1.
		*    → *Multiplicación aritmética*: Multiplicar los números decimales y convertir el resultado a binario (no se limita a 8 bits).

/		2. Proceso paso a paso de esta sesión:
		Binary 1: 01001111, Binary 2: 10011000
		Pregunta 1: |        → 11011111
		Pregunta 2: >> 1 → 01001100
		Pregunta 3: +       → 11100111
		Pregunta 4: << 1 → 10011110
		Pregunta 5: &      → 00001000
		Pregunta 6: *       → 10111011101000
		Pregunta 6.1        → Pregunta 6 en hexadecimal: 2EE8
		
/		3. Aprendizajes:
		Es importante identificar correctamente qué operación se aplica y cómo interpretar los resultados en binario o decimal.
		La conversión final a hexadecimal permite obtener la bandera de manera estándar en picoCTF.
		Algunos retos tienen convenciones no estándar para operaciones como * o +, así que hay que prestar atención a las instrucciones del desafío.

**Referencias**
	