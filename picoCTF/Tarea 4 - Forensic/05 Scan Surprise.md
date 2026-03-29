**Challenge**
	
**Description**
	I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead?
	You can download the challenge files here: [challenge.zip](https://artifacts.picoctf.net/c_atlas/1/challenge.zip)
	**Hints**
		1. QR codes are a way of encoding data. While they're most known for storing URLs, they can store other things too.
		2. Mobile phones have included native QR code scanners in their cameras since version 8 (Oreo) and iOS 11.
		3. If you don't have access to a phone, you can also use `zbar-tools` to convert an image to text.

**Solution**
	1. Descargar la imagen, descomprimir la carpeta y dirigirse a donde se encuentre el QR del reto.
	2. Utilizar la herramienta sugerida por el reto.
		1. Instalarla: `sudo apt install zbar-tools`
		2. Ejecución <script>
			┌──(kali㉿kali)-[~/home/ctf-player/drop-in]
			└─$ sudo apt install zbar-tools
			[sudo] password for kali: 
			Upgrading:                      
			  libzbar0t64
			
			Installing:
			  zbar-tools
			
			Suggested packages:
			  zbarcam-gtk  zbarcam-qt
			
			Summary:
			  Upgrading: 1, Installing: 1, Removing: 0, Not Upgrading: 1810
			  Download size: 174 kB
			  Space needed: 103 kB / 60.9 GB available
			
			Continue? [Y/n] y
			Get:2 http://http.kali.org/kali kali-rolling/main amd64 zbar-tools amd64 0.23.93-9+b1 [38.4 kB]
			Get:1 http://http.kali.org/kali kali-rolling/main amd64 libzbar0t64 amd64 0.23.93-9+b1 [136 kB]                      
			Fetched 174 kB in 8s (21.5 kB/s)                                                                                     
			(Reading database ... 426756 files and directories currently installed.)
			Preparing to unpack .../libzbar0t64_0.23.93-9+b1_amd64.deb ...
			Unpacking libzbar0t64:amd64 (0.23.93-9+b1) over (0.23.93-9) ...
			Selecting previously unselected package zbar-tools.
			Preparing to unpack .../zbar-tools_0.23.93-9+b1_amd64.deb ...
			Unpacking zbar-tools (0.23.93-9+b1) ...
			Setting up libzbar0t64:amd64 (0.23.93-9+b1) ...
			Setting up zbar-tools (0.23.93-9+b1) ...
			Processing triggers for man-db (2.13.1-1) ...
			Processing triggers for dbus (1.16.2-2) ...
			Processing triggers for kali-menu (2025.4.3) ...
			Processing triggers for libc-bin (2.41-12) ...
			                                                                                                                      
			┌──(kali㉿kali)-[~/home/ctf-player/drop-in]
			└─$ zbarimg flag.png
			QR-Code:picoCTF{p33k_@_b00_3f7cf1ae}
			scanned 1 barcode symbols from 1 images in 0.07 seconds
		</script>
	3. Utilizar alguna app o el mismo teléfono para decodificar o desencriptar el QR:
		![[Archivos 05/Screenshot 2026-03-28 194823.png]]
	4. Bandera: `picoCTF{p33k_@_b00_3f7cf1ae}`.

**Notes**
	

**References**
	