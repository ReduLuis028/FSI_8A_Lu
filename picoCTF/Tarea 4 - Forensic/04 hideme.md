**Challenge**
	
**Description**
	Every file gets a flag.The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](https://artifacts.picoctf.net/c/261/flag.png).
	**Hints**
		1. (None)

**Solution**
	1. Descargar el archivo.
	2. Instalar las siguientes herramientas:
		- `sudo apt install exiftool`
		- `sudo apt install binwalk`
	3. Haciendo uso de las herrmientas `exiftool` y `binwalk` tenemos:
		<script>
			┌──(kali㉿kali)-[~]
			└─$ exiftool flag.png                         
			ExifTool Version Number         : 13.36
			File Name                       : flag.png
			Directory                       : .
			File Size                       : 43 kB
			File Modification Date/Time     : 2023:03:15 23:15:31-04:00
			File Access Date/Time           : 2026:03:28 14:04:08-04:00
			File Inode Change Date/Time     : 2026:03:28 14:04:08-04:00
			File Permissions                : -rw-rw-r--
			File Type                       : PNG
			File Type Extension             : png
			MIME Type                       : image/png
			Image Width                     : 512
			Image Height                    : 504
			Bit Depth                       : 8
			Color Type                      : RGB with Alpha
			Compression                     : Deflate/Inflate
			Filter                          : Adaptive
			Interlace                       : Noninterlaced
			Warning                         : [minor] Trailer data after PNG IEND chunk
			Image Size                      : 512x504
			Megapixels                      : 0.258
			                                                                                                                                                   
			┌──(kali㉿kali)-[~]
			└─$ strings flag.png | grep pico
			                                                                                                                                                   
			┌──(kali㉿kali)-[~]
			└─$ binwalk -e flag.png
			
			DECIMAL       HEXADECIMAL     DESCRIPTION
			--------------------------------------------------------------------------------
			41            0x29            Zlib compressed data, compressed
			39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/
			39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2858, uncompressed size: 3015, name: secret/flag.png
			
			WARNING: One or more files failed to extract: either no utility was found or it's unimplemented
                                                                                                                                                   
			┌──(kali㉿kali)-[~]
			└─$ ls
			Desktop  disk  Documents  Downloads  flag.png  _flag.png.extracted  Music  Pictures  Public  sstv  Templates  venv  Videos
			                                                                                                                                                   
			┌──(kali㉿kali)-[~]
			└─$ cd _flag.png.extracted
			                                                                                                                                                   
			┌──(kali㉿kali)-[~/_flag.png.extracted]
			└─$ ls 
			29  29.zlib  9B3B.zip  secret
			                                                                                                                                                   
			┌──(kali㉿kali)-[~/_flag.png.extracted]
			└─$ ls secret
			flag.png
			                                                                                                                                                   
			┌──(kali㉿kali)-[~]
			└─$ open flag.png
			                                                                                                                                                   
			┌──(kali㉿kali)-[~]
			└─$ 
		</script>
		La bandera se encontró en un archivo oculto visto gracias a `exiftool` por el `warning` y `binwalk`, de tal modo que se extrajo, y se encontraba en la carpeta `secret`, abrir la imagen para visualizar la bandera.
	1. Bandera: `picoCTF{Hiddinng_An_imag3_within_@n_ima9e_96539bea}`

**Notes**
	

**References**
	