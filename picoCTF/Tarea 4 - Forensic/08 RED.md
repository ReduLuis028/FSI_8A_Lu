**Challenge**
	
**Description**
	RED, RED, RED, RED
	Download the image: [red.png](https://challenge-files.picoctf.net/c_verbal_sleep/831307718b34193b288dde31e557484876fb84978b5818e2627e453a54aa9ba6/red.png)
	**Hints**
		1. The picture seems pure, but is it though?
		2. Red?Ged?Bed?Aed?
		3. Check whatever Facebook is called now.

**Solution**
	1. Descargar el archivo.
	2. Instalar la siguiente herramientas:
		- `sudo apt update`
		- `sudo apt install ruby ruby-dev build-essential`
		- `gem install zsteg`
	3. Usar de los siguientes comandos para la encontrar la bandera:
		<script>
			┌──(kali㉿kali)-[~]
			└─$ wget https://challenge-files.picoctf.net/c_verbal_sleep/831307718b34193b288dde31e557484876fb84978b5818e2627e453a54aa9ba6/red.png
			--2026-03-29 01:17:50--  https://challenge-files.picoctf.net/c_verbal_sleep/831307718b34193b288dde31e557484876fb84978b5818e2627e453a54aa9ba6/red.png
			Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.161.44.84, 3.161.44.103, 3.161.44.22, ...
			Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.161.44.84|:443... connected.
			HTTP request sent, awaiting response... 200 OK
			Length: 796 [application/octet-stream]
			Saving to: ‘red.png’
			
			red.png                              100%[=====================================================================>]     796  --.-KB/s    in 0s      
			
			2026-03-29 01:17:55 (15.0 MB/s) - ‘red.png’ saved [796/796]
			
			                                                                                                                                                   
			┌──(kali㉿kali)-[~]
			└─$ zsteg red.png
			meta Poem           .. text: "Crimson heart, vibrant and bold,\nHearts flutter at your sight.\nEvenings glow softly red,\nCherries burst with sweet life.\nKisses linger with your warmth.\nLove deep as merlot.\nScarlet leaves falling softly,\nBold in every stroke."
			chunk:0:IHDR        .. file: Adobe Photoshop Color swatch, version 0, 128 colors; 1st RGB space (0), w 0x80, x 0x806, y 0, z 0; 2nd HSB space (1), w 0x100, x 0, y 0xff01, z 0xff
			b1,rgba,lsb,xy      .. text: "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ=="
			b1,rgba,msb,xy      .. file: OpenPGP Public Key
			b2,g,lsb,xy         .. text: "ET@UETPETUUT@TUUTD@PDUDDDPE"
			b2,rgb,lsb,xy       .. file: OpenPGP Secret Key
			b2,bgr,msb,xy       .. file: OpenPGP Public Key
			b2,rgba,lsb,xy      .. file: OpenPGP Secret Key
			b2,rgba,msb,xy      .. text: "CIkiiiII"
			b2,abgr,lsb,xy      .. file: OpenPGP Secret Key
			b2,abgr,msb,xy      .. text: "iiiaakikk"
			b3,rgba,msb,xy      .. text: "#wb#wp#7p"
			b3,abgr,msb,xy      .. text: "7r'wb#7p"
			b4,b,lsb,xy         .. file: 0421 Alliant compact executable not stripped
			                                                                                                                                                   
			┌──(kali㉿kali)-[~]
			└─$ echo cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ== | base64 -d
			picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}                                                                                                                                                             
			┌──(kali㉿kali)-[~]
			└─$ 
		</script>
	4. Bandera: `picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}`.

**Notes**
	

**References**
	