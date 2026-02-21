**Reto**
	
**Descripción**
	I accidentally wrote the flag down. Good thing I deleted it!You download the challenge files here: [challenge.zip](https://artifacts.picoctf.net/c_titan/75/challenge.zip)

**Solución**
/		1. Descomprimir el archivo 04 challenge.zip
/		2. Usando terminal de Git haciendo clic derecho sobre la carpeta > Mostrar más opciones > Open Git Bash here
		luise@CANGURO028 MINGW64 ~/Downloads/04 challenge/drop-in (master)
		$ ls
		message.txt
		
		luise@CANGURO028 MINGW64 ~/Downloads/04 challenge/drop-in (master)
		$ cat message.txt
		TOP SECRET
		
		luise@CANGURO028 MINGW64 ~/Downloads/04 challenge/drop-in (master)
		$ git log
		commit 3899edb7f3110d613c72ad40083fd8feeef703d0 (HEAD -> master)
		Author: picoCTF <ops@picoctf.com>
		Date:   Sat Mar 9 21:09:58 2024 +0000
		
		    remove sensitive info
		
		commit 6603cb4ff0c4ea293798c03a32e0d78d5ab12ca2
		Author: picoCTF <ops@picoctf.com>
		Date:   Sat Mar 9 21:09:58 2024 +0000
		
		    create flag
		
		luise@CANGURO028 MINGW64 ~/Downloads/04 challenge/drop-in (master)
		$ git show 3899edb7f3110d613c72ad40083fd8feeef703d0
		commit 3899edb7f3110d613c72ad40083fd8feeef703d0 (HEAD -> master)
		Author: picoCTF <ops@picoctf.com>
		Date:   Sat Mar 9 21:09:58 2024 +0000
		
		    remove sensitive info
		
		diff --git a/message.txt b/message.txt
		index ed59373..d552d1e 100644
		--- a/message.txt
		+++ b/message.txt
		@@ -1 +1 @@
		-picoCTF{s@n1t1z3_9539be6b}
		+TOP SECRET
		
		luise@CANGURO028 MINGW64 ~/Downloads/04 challenge/drop-in (master)
		$ git show 6603cb4ff0c4ea293798c03a32e0d78d5ab12ca2
		commit 6603cb4ff0c4ea293798c03a32e0d78d5ab12ca2
		Author: picoCTF <ops@picoctf.com>
		Date:   Sat Mar 9 21:09:58 2024 +0000
		
		    create flag
		
		diff --git a/message.txt b/message.txt
		new file mode 100644
		index 0000000..ed59373
		--- /dev/null
		+++ b/message.txt
		@@ -0,0 +1 @@
		+picoCTF{s@n1t1z3_9539be6b}
		
		luise@CANGURO028 MINGW64 ~/Downloads/04 challenge/drop-in (master)
		$

**Notes**
/		 1. Cómo funciona el reto:  
		El archivo `message.txt` actualmente muestra “TOP SECRET”.  
		El historial de Git indica que antes existía información sensible.  
		Un commit creó la bandera y otro la eliminó.  
		El objetivo es revisar commits anteriores para recuperar la información borrada.

/		 2. Método utilizado:  
		Se revisó el contenido actual con `cat message.txt`.  
		Se consultó el historial con `git log`.  
		Se identificaron dos commits importantes:  
		"create flag"  
		"remove sensitive info"  
		Se inspeccionaron ambos con `git show <hash>`.  
		En el diff apareció la bandera (línea con `+` al crearse y con `-` al eliminarse).

/		 3. Resultados:  
		Bandera obtenida: picoCTF{s@n1t1z3_9539be6b}

/		 4. Aprendizaje:  
		Git no borra realmente la información, solo registra cambios.  
		Los commits anteriores pueden recuperar datos eliminados.  
		`git show` permite ver exactamente qué se agregó o eliminó.  
		Eliminar un archivo en una versión no lo elimina del historial.

**Referencias**
	