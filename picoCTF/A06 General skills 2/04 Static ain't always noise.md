**Reto**
	
**Descripción**
	Can you look at the data in this binary? The bash script might help![static](https://challenge-files.picoctf.net/c_wily_courier/ad443900e4d8d8e6d0f3250730125d24ce6ceaf10ab38658eaafc175eee37422/static), [ltdis.sh](https://challenge-files.picoctf.net/c_wily_courier/ad443900e4d8d8e6d0f3250730125d24ce6ceaf10ab38658eaafc175eee37422/ltdis.sh)
	
**Solución**
	1. Usando la terminal de picoCTF
		Lui5-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_wily_courier/ad443900e4d8d8e6d0f3250730125d24ce6ceaf10ab38658eaafc175eee37422/static
		--2026-02-11 18:41:03--  https://challenge-files.picoctf.net/c_wily_courier/ad443900e4d8d8e6d0f3250730125d24ce6ceaf10ab38658eaafc175eee37422/static
		Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.64, 3.160.5.18, 3.160.5.40, ...
		Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.64|:443... connected.
		HTTP request sent, awaiting response... 200 OK
		Length: 16776 (16K) [application/octet-stream]
		Saving to: 'static'
		
		static                      100%[===========================================>]  16.38K  --.-KB/s    in 0.005s  
		
		2026-02-11 18:41:03 (3.21 MB/s) - 'static' saved [16776/16776]
		
		Lui5-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_wily_courier/ad443900e4d8d8e6d0f3250730125d24ce6ceaf10ab38658eaafc175eee37422/ltdis.sh
		--2026-02-11 18:41:16--  https://challenge-files.picoctf.net/c_wily_courier/ad443900e4d8d8e6d0f3250730125d24ce6ceaf10ab38658eaafc175eee37422/ltdis.sh
		Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.95, 3.160.5.18, 3.160.5.40, ...
		Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.95|:443... connected.
		HTTP request sent, awaiting response... 200 OK
		Length: 785 [application/octet-stream]
		Saving to: 'ltdis.sh'
		
		ltdis.sh                    100%[===========================================>]     785  --.-KB/s    in 0s      
		
		2026-02-11 18:41:16 (350 MB/s) - 'ltdis.sh' saved [785/785]
		
		Lui5-picoctf@webshell:~$ ls
		ltdis.sh  static
		Lui5-picoctf@webshell:~$ file static
		static: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=9a00d4dca6b92d22aa0cd1fceffa4ed7495b8534, for GNU/Linux 3.2.0, not stripped
		Lui5-picoctf@webshell:~$ file ltdis.sh
		ltdis.sh: Bourne-Again shell script, ASCII text executable
		Lui5-picoctf@webshell:~$ ./ltdis.sh static
		-bash: ./ltdis.sh: Permission denied
		Lui5-picoctf@webshell:~$ 
		Lui5-picoctf@webshell:~$ chmod +x ltdis.sh
		Lui5-picoctf@webshell:~$ ./ltdis.sh static
		Attempting disassembly of static ...
		Disassembly successful! Available at: static.ltdis.x86_64.txt
		Ripping strings from binary with file offsets...
		Any strings found in static have been written to static.ltdis.strings.txt with file offset
		Lui5-picoctf@webshell:~$ 
		Lui5-picoctf@webshell:~$ ls
		ltdis.sh  static  static.ltdis.strings.txt  static.ltdis.x86_64.txt
		Lui5-picoctf@webshell:~$ cat static.ltdis.strings.txt | grep picoCTF
		   3020 picoCTF{d15a5m_t34s3r_20335e41}
		Lui5-picoctf@webshell:~$ 

**Notes**
	1. `wget` permite descargar archivos desde URLs directamente en la terminal.
	2. `file nombre_archivo` ayuda a identificar el tipo de archivo (binario, script, texto, etc.).
	3. Los scripts de Bash (`.sh`) pueden necesitar permisos de ejecución: `chmod +x archivo`.
	4. Ejecutar el script (`./archivo`) puede automatizar tareas sobre archivos binarios, como análisis o extracción de información.
	5. El script `ltdis.sh` se usa para disassemblar un binario ELF y extraer cadenas de texto (strings) con sus offsets.
	6. Los archivos generados (`.ltdis.x86_64.txt` y `.ltdis.strings.txt`) contienen el análisis y pueden buscarse con `grep` para encontrar la flag.
	7. Combinar estas herramientas facilita explorar y analizar binarios sin necesidad de herramientas externas complejas.

**Referencias**