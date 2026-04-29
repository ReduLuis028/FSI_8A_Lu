**Reto**
	
**Descripción**
	The flag is somewhere on this web application not necessarily on the website. Find it.Check [this](http://saturn.picoctf.net:65316/) out.

**Solución**
	1. Inspeccionando archivos que usualmente no están a la vista para una posible vulnerabilidad,  y en si como el reto se llama 'Roboto Sans' se induce empezar por el archivo robots.txt
		1.1. http://saturn.picoctf.net:65316/robots.txt
			<html><head><link rel="stylesheet" href="resource://content-accessible/plaintext.css"></head><body><pre>User-agent *
			Disallow: /cgi-bin/
			Think you have seen your flag or want to keep looking.
			
			ZmxhZzEudHh0;anMvbXlmaW
			anMvbXlmaWxlLnR4dA==
			svssshjweuiwl;oiho.bsvdaslejg
			Disallow: /wp-admin/</pre></body></html>
		1.2. Decodificando la bse64 de lo previo encontrado en el archivo robots.txt, y una vez decodificado, ir a los sitios
			┌──(kali㉿kali)-[~]
			└─$ echo "ZmxhZzEudHh0" | base64 -d
			flag1.txt                                                                                                        
			┌──(kali㉿kali)-[~]
			└─$ echo "anMvbXlmaWxlLnR4dA= =" | base64 -d
			js/myfile.txt                                                                                                        
			┌──(kali㉿kali)-[~]
			└─$ 
		1.3. http://saturn.picoctf.net:65316/flag1.txt
			<html><head><title>404 Not Found</title></head>
			<body>
			<center><h1>404 Not Found</h1></center>
			<hr><center>nginx/1.21.6</center>
			</body></html>
		1.4. http://saturn.picoctf.net:65316/js/myfile.txt
			<html><head><link rel="stylesheet" href="resource://content-accessible/plaintext.css"></head><body><pre>picoCTF{Who_D03sN7_L1k5_90B0T5_22ce1f22}
			</pre></body></html>

**Notes**
	
**Referencias**
	