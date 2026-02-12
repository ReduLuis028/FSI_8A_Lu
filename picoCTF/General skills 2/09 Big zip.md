**Reto**
	
**Descripción**
	Unzip this archive and find the flag.
	[Download zip file](https://artifacts.picoctf.net/c/503/big-zip-files.zip)
	
**Solución**
	1. Usano terminl de picoCTF
		Previamente descomprimir el .zip
		Lui5-picoctf@webshell:~$ ls
		big-zip-files  big-zip-files.zip
		Lui5-picoctf@webshell:~$ cd big-zip-files/
		Lui5-picoctf@webshell:~/big-zip-files$ grep -r picoCTF
		folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
		Lui5-picoctf@webshell:~/big-zip-files$ 

**Notes**
	1. `grep -r` permite buscar texto dentro de todos los archivos de un directorio y sus subdirectorios.
	2. Sintaxis básica: `grep -r 'texto_a_buscar' ruta_directorio`.
	3. Útil cuando hay muchos archivos y carpetas y no se conoce exactamente dónde está la información.
	4. El resultado muestra la ruta del archivo y la línea donde aparece el texto buscado.
	5. En este ejercicio se buscó `picoCTF` directamente para localizar la flag dentro de los archivos.

**Referencias**