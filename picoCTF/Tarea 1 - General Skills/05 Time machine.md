**Reto**
	
**Descripción**
	What was I last working on? I remember writing a note to help me remember...You can download the challenge files here: [challenge.zip](https://artifacts.picoctf.net/c_titan/66/challenge.zip)

**Solución**
/		1. Descomprimir el archivo 05 challenge.zip
/		2. Usando terminal de Git haciendo clic derecho sobre la carpeta > Mostrar más opciones > Open Git Bash here
		luise@CANGURO028 MINGW64 ~/Downloads/05 challenge/drop-in (master)
		$ ls
		message.txt
		
		luise@CANGURO028 MINGW64 ~/Downloads/05 challenge/drop-in (master)
		$ cat message.txt
		This is what I was working on, but I'd need to look at my commit history to know why...
		luise@CANGURO028 MINGW64 ~/Downloads/05 challenge/drop-in (master)
		$ git log
		commit 3339c144a0c78dc2fbd3403d2fb37d3830be5d94 (HEAD -> master)
		Author: picoCTF <ops@picoctf.com>
		Date:   Sat Mar 9 21:10:22 2024 +0000
		
		    picoCTF{t1m3m@ch1n3_d3161c0f}
		
		luise@CANGURO028 MINGW64 ~/Downloads/05 challenge/drop-in (master)
		$

**Notes**
/		 1. Cómo funciona el reto:  
		El reto indica que olvidaste en qué estabas trabajando.  
		Menciona que escribiste una nota para recordarlo.  
		Esto sugiere que la información está en el historial de Git (commits anteriores).  
		La bandera se encontraba en un commit pasado.

/		2. Método utilizado:  
		Se revisó el historial con `git log`.  
		Se identificó un commit que contenía la nota.  
		Se inspeccionó el contenido con `git show <hash>` o revisando el mensaje del commit.  
		La bandera estaba directamente en ese registro anterior.

/		3. Resultados:  
		Bandera obtenida: picoCTF{t1m3m@ch1n3_d3161c0f}

/		4. Aprendizaje:  
		Git guarda todo el historial del proyecto.  
		Los commits anteriores pueden contener información importante.  
		`git log` y `git show` permiten viajar en el tiempo dentro del repositorio.  
		El reto demuestra cómo recuperar información del pasado usando Git.

**Referencias**
	