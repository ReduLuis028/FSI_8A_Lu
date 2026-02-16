**Reto**
	
**Descripción**
	Fix the syntax error in the Python script to print the flag. [Download Python script](https://artifacts.picoctf.net/c/4/fixme2.py)
	
**Solución**
	1. Usando terminal de Windows y VSCode
		C:\Users\luise\Downloads>py "06 fixme2.py"
		  File "C:\Users\luise\Downloads\06 fixme2.py", line 22
		    if flag = "":
		       ^^^^^^^^^
		SyntaxError: invalid syntax. Maybe you meant '' or ':=' instead of '='?

		Correccion en la linea 22

		C:\Users\luise\Downloads>py "06 fixme2.py"
		That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_e8814d03}
		
		C:\Users\luise\Downloads>

**Notes**
	1. '=' es asignación.
	2. == es comparación.
	3. El error fue usar = en condición.
	4. Refuerza operadores lógicos en Python.

**Referencias**
	