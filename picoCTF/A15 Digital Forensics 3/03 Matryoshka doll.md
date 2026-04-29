**Challenge**
	
**Description**
	Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one?Image: [dolls.jpg](https://challenge-files.picoctf.net/c_wily_courier/9bf118825bda566d4622b19d243e75877e2c17db745281bc5b0d11efd2278161/dolls.jpg)
	**Hints**
		1. Wait, you can hide files inside files? But how do you find them?
		2. Make sure to submit the flag as picoCTF{XXXXX}

**Solution**
	1. Guía de que hacer:
		- Analizar `dolls.jpg` con **binwalk**.
		- Extraer el primer ZIP (`4286C.zip`) que contiene `2_c.jpg`.
		- Analizar y extraer `2_c.jpg` para obtener `3_c.jpg`.
		- Analizar y extraer `3_c.jpg` para obtener `4_c.jpg`.
		- Usar `strings "4_c.jpg" | grep picoCTF` sobre `4_c.jpg` para sacar la bandera.
	2. Guía en CLI:
		<script>
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 03]
			└─$ binwalk dolls.jpg
			
			DECIMAL       HEXADECIMAL     DESCRIPTION
			--------------------------------------------------------------------------------
			0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
			3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
			272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378933, uncompressed size: 383920, name: base_images/2_c.jpg
			651591        0x9F147         End of Zip archive, footer length: 22
			
			                                                                                                      
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 03]
			└─$ binwalk -e dolls.jpg
			
			DECIMAL       HEXADECIMAL     DESCRIPTION
			--------------------------------------------------------------------------------
			272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378933, uncompressed size: 383920, name: base_images/2_c.jpg
			
			WARNING: One or more files failed to extract: either no utility was found or it's unimplemented
			
			                                                                                                      
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 03]
			└─$ cd _dolls.jpg.extracted
			                                                                                                      
			┌──(kali㉿kali)-[/run/…/kali/ESD-USB/Archivos 03/_dolls.jpg.extracted]
			└─$ ls
			4286C.zip  base_images
			                                                                                                      
			┌──(kali㉿kali)-[/run/…/kali/ESD-USB/Archivos 03/_dolls.jpg.extracted]
			└─$ unzip 4286C.zip -d extracted_zip
			Archive:  4286C.zip
			  inflating: extracted_zip/base_images/2_c.jpg  
			                                                                                                      
			┌──(kali㉿kali)-[/run/…/kali/ESD-USB/Archivos 03/_dolls.jpg.extracted]
			└─$ cd extracted_zip 
			                                                                                                      
			┌──(kali㉿kali)-[/run/…/ESD-USB/Archivos 03/_dolls.jpg.extracted/extracted_zip]
			└─$ ls
			base_images
			                                                                                                      
			┌──(kali㉿kali)-[/run/…/ESD-USB/Archivos 03/_dolls.jpg.extracted/extracted_zip]
			└─$ cd base_images
			                                                                                                      
			┌──(kali㉿kali)-[/run/…/Archivos 03/_dolls.jpg.extracted/extracted_zip/base_images]
			└─$ ls
			2_c.jpg
			                                                                                                      
			┌──(kali㉿kali)-[/run/…/Archivos 03/_dolls.jpg.extracted/extracted_zip/base_images]
			└─$ binwalk 2_c.jpg
			
			DECIMAL       HEXADECIMAL     DESCRIPTION
			--------------------------------------------------------------------------------
			0             0x0             PNG image, 526 x 1106, 8-bit/color RGBA, non-interlaced
			3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
			187707        0x2DD3B         Zip archive data, at least v2.0 to extract, compressed size: 196025, uncompressed size: 201427, name: base_images/3_c.jpg
			383787        0x5DB2B         End of Zip archive, footer length: 22
			383898        0x5DB9A         End of Zip archive, footer length: 22
			
			                                                                                                      
			┌──(kali㉿kali)-[/run/…/Archivos 03/_dolls.jpg.extracted/extracted_zip/base_images]
			└─$ unzip 2_c.jpg -d extracted_zip2
			Archive:  2_c.jpg
			warning [2_c.jpg]:  187707 extra bytes at beginning or within zipfile
			  (attempting to process anyway)
			  inflating: extracted_zip2/base_images/3_c.jpg  
			                                                                                                      
			┌──(kali㉿kali)-[/run/…/Archivos 03/_dolls.jpg.extracted/extracted_zip/base_images]
			└─$ cd extracted_zip2/base_images
			                                                                                                       
			┌──(kali㉿kali)-[/run/…/extracted_zip/base_images/extracted_zip2/base_images]
			└─$ l 
			3_c.jpg
			                                                                                                       
			┌──(kali㉿kali)-[/run/…/extracted_zip/base_images/extracted_zip2/base_images]
			└─$ binwalk 3_c.jpg
			
			DECIMAL       HEXADECIMAL     DESCRIPTION
			--------------------------------------------------------------------------------
			0             0x0             PNG image, 428 x 1104, 8-bit/color RGBA, non-interlaced
			3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
			123606        0x1E2D6         Zip archive data, at least v2.0 to extract, compressed size: 77633, uncompressed size: 79786, name: base_images/4_c.jpg
			201405        0x312BD         End of Zip archive, footer length: 22
			
			                                                                                                       
			┌──(kali㉿kali)-[/run/…/extracted_zip/base_images/extracted_zip2/base_images]
			└─$ unzip 3_c.jpg -d extracted_zip3
			Archive:  3_c.jpg
			warning [3_c.jpg]:  123606 extra bytes at beginning or within zipfile
			  (attempting to process anyway)
			  inflating: extracted_zip3/base_images/4_c.jpg  
			                                                                                                       
			┌──(kali㉿kali)-[/run/…/extracted_zip/base_images/extracted_zip2/base_images]
			└─$ cd extracted_zip3
			                                                                                                       
			┌──(kali㉿kali)-[/run/…/base_images/extracted_zip2/base_images/extracted_zip3]
			└─$ ls
			base_images
			                                                                                                       
			┌──(kali㉿kali)-[/run/…/base_images/extracted_zip2/base_images/extracted_zip3]
			└─$ unzip 3_c.jpg -d extracted_zip4
			unzip:  cannot find or open 3_c.jpg, 3_c.jpg.zip or 3_c.jpg.ZIP.
			                                                                                                       
			┌──(kali㉿kali)-[/run/…/base_images/extracted_zip2/base_images/extracted_zip3]
			└─$ ls
			base_images
			                                                                                                       
			┌──(kali㉿kali)-[/run/…/base_images/extracted_zip2/base_images/extracted_zip3]
			└─$ cd base_images  
			                                                                                                       
			┌──(kali㉿kali)-[/run/…/extracted_zip2/base_images/extracted_zip3/base_images]
			└─$ ls
			4_c.jpg
			                                                                                                       
			┌──(kali㉿kali)-[/run/…/extracted_zip2/base_images/extracted_zip3/base_images]
			└─$ strings 4_c.jpg | grep picoCTF
			picoCTF{LL9lb1dR4QbGe4l4iWCvGq9pdtwt7392}
			                                                                                                       
			┌──(kali㉿kali)-[/run/…/extracted_zip2/base_images/extracted_zip3/base_images]
			└─$ 
			
		</script>
	3. Bandera: `picoCTF{LL9lb1dR4QbGe4l4iWCvGq9pdtwt7392}`.

**Notes**
	1. Las imágenes contienen archivos ZIP ocultos de manera anidada (una dentro de otra), similar a las muñecas rusas “matryoshka”.
	2. `binwalk` es útil para analizar imágenes y detectar datos incrustados como ZIPs.
	3. Se puede extraer cada ZIP manualmente usando `unzip`, incluso si hay bytes extra al inicio de la imagen.
	4. La bandera se encuentra en la última imagen (`4_c.jpg`) y se puede obtener usando `strings` combinado con `grep`.
	5. Es importante seguir el orden de extracción para llegar al archivo final que contiene la bandera.
	6. Cada paso de análisis y extracción confirma la presencia de otro archivo dentro, haciendo la secuencia repetitiva pero necesaria.

**References**