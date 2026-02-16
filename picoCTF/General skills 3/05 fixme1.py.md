**Reto**
	
**Descripción**
	Fix the syntax error in this Python script to print the flag. [Download Python script](https://artifacts.picoctf.net/c/26/fixme1.py)

**Solución**
	1. Usando terminal de Windows y VSCode
		C:\Users\luise\Downloads>py "05 fixme1.py"
		  File "C:\Users\luise\Downloads\05 fixme1.py", line 16
		    print('That is correct! Here\'s your flag: ' + flag)
		IndentationError: unexpected indent
		
		Corrección de indetacion en la linea 20
		
		C:\Users\luise\Downloads>py "05 fixme1.py"
		That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_09ee727a}
		
		C:\Users\luise\Downloads>

**Notes**
	1. Python usa indentación obligatoria.
	2. Un espacio incorrecto genera IndentationError.
	3. Se corrigió alineación del bloque.
	4. Refuerza estructura sintáctica en Python.

**Referencias**
	