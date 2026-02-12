**Reto**
	
**Descripción**
	Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames.[Addadshashanammu.zip](https://challenge-files.picoctf.net/c_wily_courier/1d211441eced2214a10b0c2aacbf05d153aafcd6edc055f913cafcdb48a0b02b/Addadshashanammu.zip)
	
**Solución**
	1. Usando terminal e picoCTF
		Lui5-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_wily_courier/1d211441eced2214a10b0c2aacbf05d153aafcd6edc055f913cafcdb48a0b02b/Addadshashanammu.zip
		--2026-02-11 18:55:00--  https://challenge-files.picoctf.net/c_wily_courier/1d211441eced2214a10b0c2aacbf05d153aafcd6edc055f913cafcdb48a0b02b/Addadshashanammu.zip
		Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.18, 3.160.5.64, 3.160.5.95, ...
		Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.18|:443... connected.
		HTTP request sent, awaiting response... 200 OK
		Length: 5166 (5.0K) [application/octet-stream]
		Saving to: 'Addadshashanammu.zip'
		
		Addadshashanammu.zip        100%[===========================================>]   5.04K  --.-KB/s    in 0s      
		
		2026-02-11 18:55:01 (881 MB/s) - 'Addadshashanammu.zip' saved [5166/5166]
		
		Lui5-picoctf@webshell:~$ unzip Addadshashanammu.zip
		Archive:  Addadshashanammu.zip
		   creating: Addadshashanammu/
		   creating: Addadshashanammu/Almurbalarammi/
		   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/
		   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/
		   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/
		   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/
		   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
		 extracting: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet.c  
		  inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet  
		Lui5-picoctf@webshell:~$ 
		Lui5-picoctf@webshell:~$ ls
		Addadshashanammu  Addadshashanammu.zip
		Lui5-picoctf@webshell:~$ cd Addadshashanammu/
		Lui5-picoctf@webshell:~/Addadshashanammu$ ls
		Almurbalarammi
		Lui5-picoctf@webshell:~/Addadshashanammu$ cd Almurbalarammi/
		Lui5-picoctf@webshell:~/Addadshashanammu/Almurbalarammi$ cd Ashalmimilkala/
		Lui5-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalmimilkala$ cd Assurnabitashpi/
		Lui5-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi$ cd Maelkashishi/
		Lui5-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi$ cd Onnissiralis/
		Lui5-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis
		$ cd Ularradallaku/
		Lui5-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis
		/Ularradallaku$ ls
		fang-of-haynekhtnamet  fang-of-haynekhtnamet.c
		Lui5-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis
		/Ularradallaku$ ./fang-of-haynekhtnamet 
		*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}
		Lui5-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis
		/Ularradallaku$    
**Notes**
	1. El tab-complete en la terminal permite autocompletar nombres de directorios y archivos largos, ahorrando tiempo y evitando errores tipográficos.
	2. `wget` se usa para descargar archivos desde una URL directamente en el terminal.
	3. `unzip` permite extraer archivos comprimidos y ver la estructura de carpetas creada.
	4. Navegar con `cd` y listar con `ls` ayuda a recorrer directorios largos y anidados.
	5. Ejecutar archivos binarios directamente (`./nombre_archivo`) permite obtener la salida, como la flag en este ejercicio.
	6. Combinar estas herramientas facilita explorar directorios complejos y encontrar información sin necesidad de escribir rutas completas manualmente.

**Referencias**