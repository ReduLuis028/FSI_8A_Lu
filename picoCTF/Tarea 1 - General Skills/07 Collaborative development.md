**Reto**
	
**Descripción**
	My team has been working very hard on new features for our flag printing program! I wonder how they'll work together?You can download the challenge files here: [challenge.zip](https://artifacts.picoctf.net/c_titan/71/challenge.zip)

**Solución**
/		1. Descomprimir el archivo 07 challenge.zip
/		2. Usando terminal de Git haciendo clic derecho sobre la carpeta > Mostrar más opciones > Open Git Bash here
		luise@CANGURO028 MINGW64 ~/Downloads/07 challenge/drop-in (main)
		$ ls
		flag.py
		
		luise@CANGURO028 MINGW64 ~/Downloads/07 challenge/drop-in (main)
		$ python flag.py
		Printing the flag...
		
		luise@CANGURO028 MINGW64 ~/Downloads/07 challenge/drop-in (main)
		$ git branch -a
		  feature/part-1
		  feature/part-2
		  feature/part-3
		* main
		
		luise@CANGURO028 MINGW64 ~/Downloads/07 challenge/drop-in (main)
		$ git checkout feature/part-1
		Switched to branch 'feature/part-1'
		
		luise@CANGURO028 MINGW64 ~/Downloads/07 challenge/drop-in (feature/part-1)
		$ ls
		flag.py
		
		luise@CANGURO028 MINGW64 ~/Downloads/07 challenge/drop-in (feature/part-1)
		$ python flag.py
		Printing the flag...
		picoCTF{t3@mw0rk_
		luise@CANGURO028 MINGW64 ~/Downloads/07 challenge/drop-in (feature/part-1)
		$ git checkout feature/part-2
		Switched to branch 'feature/part-2'
		
		luise@CANGURO028 MINGW64 ~/Downloads/07 challenge/drop-in (feature/part-2)
		$ ls
		flag.py
		
		luise@CANGURO028 MINGW64 ~/Downloads/07 challenge/drop-in (feature/part-2)
		$ python flag.py
		Printing the flag...
		m@k3s_th3_dr3@m_
		luise@CANGURO028 MINGW64 ~/Downloads/07 challenge/drop-in (feature/part-2)
		$ git checkout feature/part-3
		Switched to branch 'feature/part-3'
		
		luise@CANGURO028 MINGW64 ~/Downloads/07 challenge/drop-in (feature/part-3)
		$ ls
		flag.py
		
		luise@CANGURO028 MINGW64 ~/Downloads/07 challenge/drop-in (feature/part-3)
		$ python flag.py
		Printing the flag...
		w0rk_4c24302f}
		
		luise@CANGURO028 MINGW64 ~/Downloads/07 challenge/drop-in (feature/part-3)
		$

**Notes**
/		1. Cómo funciona el reto:  
		El proyecto usa varias ramas de Git.  
		En la rama `main` no aparece la bandera completa.  
		Cada rama `feature/part-*` contiene una parte distinta de la flag.  
		Se debe revisar cada rama para obtener todas las partes.
	
/		2. Método utilizado:  
		Se listaron las ramas con `git branch -a`.  
		Se cambió entre ramas usando `git checkout feature/part-*`.  
		En cada rama se ejecutó `python flag.py`.  
		Cada ejecución mostraba una parte diferente de la bandera.  
		Se combinaron manualmente las tres partes en orden.
	
/		3. Resultados:  
		Parte 1: picoCTF{t3@mw0rk_  
		Parte 2: m@k3s_th3_dr3@m_  
		Parte 3: w0rk_4c24302f}  
		Bandera obtenida: picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_4c24302f}
	
/		4. Aprendizaje:  
		Git permite trabajar con múltiples ramas en un mismo proyecto.  
		Las ramas pueden contener versiones diferentes de un archivo.  
		Es importante saber usar `git branch` y `git checkout`.  
		El reto demuestra cómo la información puede estar dividida en distintas branches.

**Referencias**
	