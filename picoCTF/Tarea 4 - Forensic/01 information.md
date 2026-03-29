**Challenge**
	
**Description**
	Files can always be changed in a secret way.
	Can you find the flag? [cat.jpg](https://challenge-files.picoctf.net/c_wily_courier/76e95e3e6ee69b4f82b3cea25051f5a9a5918b57809a1f90b29b06b776c73bc7/cat.jpg)
	**Hints**
		1. Look at the details of the file
		2. Make sure to submit the flag as picoCTF{XXXXX}

**Solution**
	1. Descargar el archivo.
	2. Analizar la imagen, se hicieron varis pruebas con algunas herramientas como `strings`, `finstr`, `binwalk`, `zsteg`, y ninguna mostro el resultado esperado, esperando que estuviera en texto plano la bandera, hasta que se deicidio revisar los metadatos de la imagen con `exiftool`, resultando la bandera en el metadato `license` en un formato `base64`:
		<script>
			┌──(kali㉿kali)-[~]
			└─$ exiftool cat.jpg
			ExifTool Version Number         : 13.36
			File Name                       : cat.jpg
			Directory                       : .
			File Size                       : 878 kB
			File Modification Date/Time     : 2025:12:12 14:21:14-05:00
			File Access Date/Time           : 2026:03:28 13:22:42-04:00
			File Inode Change Date/Time     : 2026:03:28 13:22:33-04:00
			File Permissions                : -rw-rw-r--
			File Type                       : JPEG
			File Type Extension             : jpg
			MIME Type                       : image/jpeg
			JFIF Version                    : 1.02
			Resolution Unit                 : None
			X Resolution                    : 1
			Y Resolution                    : 1
			Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
			Copyright Notice                : PicoCTF
			Application Record Version      : 4
			XMP Toolkit                     : Image::ExifTool 10.80
			License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
			Rights                          : PicoCTF
			Image Width                     : 2560
			Image Height                    : 1598
			Encoding Process                : Baseline DCT, Huffman coding
			Bits Per Sample                 : 8
			Color Components                : 3
			Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
			Image Size                      : 2560x1598
			Megapixels                      : 4.1
			                                                                                                                      
			┌──(kali㉿kali)-[~]
			└─$ echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d
			picoCTF{the_m3tadata_1s_modified}                                                                                                                      
			┌──(kali㉿kali)-[~]
			└─$ 
		</script>
	3. Bandera: `picoCTF{the_m3tadata_1s_modified}`.

**Notes**
	

**References**
	