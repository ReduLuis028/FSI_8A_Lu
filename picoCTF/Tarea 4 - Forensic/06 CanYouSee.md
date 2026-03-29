**Challenge**
	
**Description**
	How about some hide and seek?
	Download this file [here](https://artifacts.picoctf.net/c_titan/4/unknown.zip).
	**Hints**
		1. How can you view the information about the picture?
		2. If something isn't in the expected form, maybe it deserves attention?

**Solution**
	1. Descargar la carpeta, descomprimirla.
	2. Analizar la imagen con `exiftool` como menciona el **Hint 1**, y posteriormente, desencriptar el metadato `Attribution URL` y que es lo único que puede parecer raro, no hubo `warnings`.
		<script>
			┌──(kali㉿kali)-[~]
			└─$ exiftool ukn_reality.jpg 
			ExifTool Version Number         : 13.36
			File Name                       : ukn_reality.jpg
			Directory                       : .
			File Size                       : 2.3 MB
			File Modification Date/Time     : 2024:02:15 17:40:14-05:00
			File Access Date/Time           : 2026:03:28 22:10:19-04:00
			File Inode Change Date/Time     : 2026:03:28 22:10:19-04:00
			File Permissions                : -rw-r--r--
			File Type                       : JPEG
			File Type Extension             : jpg
			MIME Type                       : image/jpeg
			JFIF Version                    : 1.01
			Resolution Unit                 : inches
			X Resolution                    : 72
			Y Resolution                    : 72
			XMP Toolkit                     : Image::ExifTool 11.88
			Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fZGVjYTA2ZmJ9Cg==
			Image Width                     : 4308
			Image Height                    : 2875
			Encoding Process                : Baseline DCT, Huffman coding
			Bits Per Sample                 : 8
			Color Components                : 3
			Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
			Image Size                      : 4308x2875
			Megapixels                      : 12.4
			                                                                                                                      
			┌──(kali㉿kali)-[~]
			└─$ echo cGljb0NURntNRTc0RDQ3QV9ISUREM05fZGVjYTA2ZmJ9Cg== | base64 -d
			picoCTF{ME74D47A_HIDD3N_deca06fb}
		</script>
	3. Bandera: `picoCTF{ME74D47A_HIDD3N_deca06fb}`.

**Notes**
	

**References**
	