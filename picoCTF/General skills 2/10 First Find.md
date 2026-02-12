**Reto**
	
**Descripción**
	Unzip this archive and find the file named 'uber-secret.txt'
	[Download zip file](https://artifacts.picoctf.net/c/500/files.zip)
	
**Solución**
	1. Usando terminal de picoCTF
		Lui5-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/500/files.zip
		--2026-02-11 19:25:40--  https://artifacts.picoctf.net/c/500/files.zip
		Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.33, 3.170.131.18, ...
		Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
		HTTP request sent, awaiting response... 200 OK
		Length: 3995553 (3.8M) [application/octet-stream]
		Saving to: 'files.zip'
		
		files.zip                   100%[===========================================>]   3.81M  1.81MB/s    in 2.1s    
		
		2026-02-11 19:25:42 (1.81 MB/s) - 'files.zip' saved [3995553/3995553]
		
		Lui5-picoctf@webshell:~$ ls
		files.zip
		Lui5-picoctf@webshell:~$ unzip files.zip 
		Archive:  files.zip
		   creating: files/
		   creating: files/satisfactory_books/
		   creating: files/satisfactory_books/more_books/
		  inflating: files/satisfactory_books/more_books/37121.txt.utf-8  
		  inflating: files/satisfactory_books/23765.txt.utf-8  
		  inflating: files/satisfactory_books/16021.txt.utf-8  
		  inflating: files/13771.txt.utf-8   
		   creating: files/adequate_books/
		   creating: files/adequate_books/more_books/
		   creating: files/adequate_books/more_books/.secret/
		   creating: files/adequate_books/more_books/.secret/deeper_secrets/
		   creating: files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/
		 extracting: files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt  
		  inflating: files/adequate_books/more_books/1023.txt.utf-8  
		  inflating: files/adequate_books/46804-0.txt  
		  inflating: files/adequate_books/44578.txt.utf-8  
		   creating: files/acceptable_books/
		   creating: files/acceptable_books/more_books/
		  inflating: files/acceptable_books/more_books/40723.txt.utf-8  
		  inflating: files/acceptable_books/17880.txt.utf-8  
		  inflating: files/acceptable_books/17879.txt.utf-8  
		  inflating: files/14789.txt.utf-8   
		Lui5-picoctf@webshell:~$ 
		Lui5-picoctf@webshell:~$ find -name uber
		Lui5-picoctf@webshell:~$ find -name uber%
		Lui5-picoctf@webshell:~$ find -name 'uber-secret.txt'
		./files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
		Lui5-picoctf@webshell:~$ cat ./files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
		picoCTF{f1nd_15_f457_ab443fd1}
		Lui5-picoctf@webshell:~$ 
		
**Notes**
	2. `unzip` permite extraer el contenido de archivos comprimidos y ver la estructura de carpetas creada.
	3. `find` sirve para buscar archivos por nombre dentro de directorios y subdirectorios.
	4. Sintaxis básica: `find -name 'nombre_archivo'`.
	5. Se pueden usar comodines: `find -name 'uber*'` para coincidencias parciales.
	6. Los directorios ocultos (como `.secret`) también son recorridos por `find`.
	7. Una vez localizada la ruta, usar `cat` para leer el contenido del archivo.
	
**Referencias**