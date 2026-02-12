**Reto**
	
**Descripción**
	There's an interesting script in the user's home directory
	
**Solución**
	1. Usando terminal de picoCTF
		Lui5-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_wily_courier/ad443900e4d8d8e6d0f3250730125d24ce6ceaf10ab38658eaafc175eee37422/static
		--2026-02-11 18:41:03--  https://challenge-files.picoctf.net/c_wily_courier/ad443900e4d8d8e6d0f3250730125d24ce6ceaf10ab38658eaafc175eee37422/static
		Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.64, 3.160.5.18, 3.160.5.40, ...
		Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.64|:443... connected.
		Lui5-picoctf@webshell:~$ ssh picoplayer@saturn.picoctf.net -p 58523
		The authenticity of host '[saturn.picoctf.net]:58523 ([13.59.203.175]:58523)' can't be established.
		ED25519 key fingerprint is SHA256:DiJcS90U9QussLS8HLR6l6BGJb5eCA0vRmA18IvDvw8.
		This key is not known by any other names
		Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
		Warning: Permanently added '[saturn.picoctf.net]:58523' (ED25519) to the list of known hosts.
		picoplayer@saturn.picoctf.net's password: 
		Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.8.0-1044-aws x86_64)
		
		 * Documentation:  https://help.ubuntu.com
		 * Management:     https://landscape.canonical.com
		 * Support:        https://ubuntu.com/advantage
		
		The programs included with the Ubuntu system are free software;
		the exact distribution terms for each program are described in the
		individual files in /usr/share/doc/*/copyright.
		
		Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
		applicable law.
		
		picoplayer@challenge:~$ ls
		useless
		picoplayer@challenge:~$ ./useless
		Read the code first
		picoplayer@challenge:~$ file useless
		useless: Bourne-Again shell script, ASCII text executable
		picoplayer@challenge:~$ cat useless
		#!/bin/bash
		# Basic mathematical operations via command-line arguments
		
		if [ $# != 3 ]
		then
		  echo "Read the code first"
		else
		        if [[ "$1" == "add" ]]
		        then 
		          sum=$(( $2 + $3 ))
		          echo "The Sum is: $sum"  
		
		        elif [[ "$1" == "sub" ]]
		        then 
		          sub=$(( $2 - $3 ))
		          echo "The Substract is: $sub" 
		
		        elif [[ "$1" == "div" ]]
		        then 
		          div=$(( $2 / $3 ))
		          echo "The quotient is: $div" 
		
		        elif [[ "$1" == "mul" ]]
		        then
		          mul=$(( $2 * $3 ))
		          echo "The product is: $mul" 
		
		        else
		          echo "Read the manual"
		         
		        fi
		fi
		picoplayer@challenge:~$ ./useless add 100 300
		The Sum is: 400
		picoplayer@challenge:~$ ./useless sub 100 300
		The Substract is: -200
		picoplayer@challenge:~$ ./useless man        
		Read the code first
		picoplayer@challenge:~$ ./useless --help
		Read the code first
		picoplayer@challenge:~$ ./useless -help
		Read the code first
		picoplayer@challenge:~$ ./useless      
		Read the code first
		picoplayer@challenge:~$ ./useless echo
		Read the code first
		picoplayer@challenge:~$ man useless
		
		useless
		     useless, -- This is a simple calculator script
		
		SYNOPSIS
		     useless, [add sub mul div] number1 number2
		
		DESCRIPTION
		     Use the useless, macro to make simple calulations like addition,subtraction, multiplication and divi-
		     sion.
		
		Examples
		     ./useless add 1 2
		       This will add 1 and 2 and return 3
		
		     ./useless mul 2 3
		       This will return 6 as a product of 2 and 3
		
		     ./useless div 6 3
		       This will return 2 as a quotient of 6 and 3
		
		     ./useless sub 6 5
		       This will return 1 as a remainder of substraction of 5 from 6
		
		Authors
		     This script was designed and developed by Cylab Africa
		
		     picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_3823}
		
		picoplayer@challenge:~$ 
**Notes**
	2. Los scripts de Bash (`.sh` o ejecutables de texto) pueden inspeccionarse con `cat` para entender su funcionamiento antes de ejecutarlos.
	3. `file nombre_archivo` permite identificar el tipo de archivo (script, binario, texto, etc.).
	4. Ejecutar un script con `./nombre_script` permite pasar argumentos directamente desde la línea de comandos.
	5. Leer el código es importante para descubrir cómo interactuar con el script y qué argumentos acepta.
	6. En este ejercicio, el script `useless` funciona como una calculadora simple con operaciones `add`, `sub`, `mul` y `div`.
	7. Revisar ejemplos en la sección de “man” o dentro del propio script ayuda a usar correctamente los argumentos.
	8. La flag estaba directamente en el script, demostrando que a veces solo hace falta leer el código.

**Referencias**