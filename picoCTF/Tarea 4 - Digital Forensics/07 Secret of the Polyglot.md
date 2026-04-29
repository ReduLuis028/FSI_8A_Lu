**Challenge**
	
**Description**
	The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is.
	They've brought you in as an external expert to examine the file.
	Can you extract all the information from this strange file?
	Download the suspicious file [here](https://artifacts.picoctf.net/c_titan/97/flag2of2-final.pdf).
	**Hints**
		1. This problem can be solved by just opening the file in different ways

**Solution**
	1. Descargar el archivo.
	2. Instalar la siguiente herramientas:
		- `sudo apt update`
		- `sudo apt install poppler-utils`
		- `sudo apt install tesseract-ocr`
	3. Usar de los siguientes comandos para la encontrar la bandera:
		<script>
			┌──(kali㉿kali)-[~]
			└─$ wget https://artifacts.picoctf.net/c_titan/97/flag2of2-final.pdf
			--2026-03-28 22:29:56--  https://artifacts.picoctf.net/c_titan/97/flag2of2-final.pdf
			Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.161.55.64, 3.161.55.100, 3.161.55.61, ...
			Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.161.55.64|:443... connected.
			HTTP request sent, awaiting response... 200 OK
			Length: 3362 (3.3K) [application/octet-stream]
			Saving to: ‘flag2of2-final.pdf’
			
			flag2of2-final.pdf            100%[===============================================>]   3.28K  --.-KB/s    in 0s      
			
			2026-03-28 22:29:57 (17.9 MB/s) - ‘flag2of2-final.pdf’ saved [3362/3362]
			
			                                                                                                                      
			┌──(kali㉿kali)-[~]
			└─$ pdftotext flag2of2-final.pdf 
			                                                                                                                      
			┌──(kali㉿kali)-[~]
			└─$ cat flag2of2-final.txt
			1n_pn9_&_pdf_724b1287}
			
			
			                                                                                                                      
			┌──(kali㉿kali)-[~]
			└─$ file flag2of2-final.pdf  
			flag2of2-final.pdf: PNG image data, 50 x 50, 8-bit/color RGBA, non-interlaced
			                                                                                                                      
			┌──(kali㉿kali)-[~]
			└─$ pdftoppm flag2of2-final.pdf  salida -png
			                                                                                                                      
			┌──(kali㉿kali)-[~]
			└─$ convert flag2of2-final.pdf  salida.png
			                                                                                                                      
			┌──(kali㉿kali)-[~]
			└─$ open salida.png 
                                                                                                                      
			┌──(kali㉿kali)-[~]
			└─$ 
		</script>
		Una vez viendo la `salida.png` escribir manualmente la primera parte de la bandera `picoCTF{f1u3n7_`.
	4. Bandera: `picoCTF{f1u3n7_1n_pn9_&_pdf_724b1287}`.

**Notes**
	

**References**
	