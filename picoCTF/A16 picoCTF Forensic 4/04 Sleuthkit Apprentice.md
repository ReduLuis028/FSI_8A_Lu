**Challenge**
	
**Description**
	Download this disk image and find the flag.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
	 [Download compressed disk image](https://artifacts.picoctf.net/c/137/disk.flag.img.gz)
	**Hints**
		1. None

**Solution**
	1. Extraer el archivo `disk.flag.img.gz`.
	2. Comandos a usar:
		- `mmls disk.flag.img`
		- `fls -r -o Start disk.flag.img | grep -i flag` → Start = 0000360448 → 360448
		- `icat -o 360448 disk.flag.img 2082`→ flag.txt = 2082
		- `icat -o 360448 disk.flag.img 2371`→ flag.uni.txt = 2371
	3. Una vez hecho, usar CLI:
		<script class = "CLI kali-linux">
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 04]
			└─$ mmls disk.flag.img                                         
			DOS Partition Table
			Offset Sector: 0
			Units are in 512-byte sectors
			
			      Slot      Start        End          Length       Description
			000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
			001:  -------   0000000000   0000002047   0000002048   Unallocated
			002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
			003:  000:001   0000206848   0000360447   0000153600   Linux Swap / Solaris x86 (0x82)
			004:  000:002   0000360448   0000614399   0000253952   Linux (0x83)
			                                                                                                      
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 04]
			└─$ sudo fls -r -o 360448 disk.flag.img | grep -i flag
			++ r/r * 2082(realloc): flag.txt
			++ r/r 2371:    flag.uni.txt
			                                                                                                      
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 04]
			└─$ sudo icat -o 360448 disk.flag.img 2082
			            3.449677            13.056403
			                                                                                                      
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 04]
			└─$ sudo icat -o 360448 disk.flag.img 2371
			picoCTF{by73_5urf3r_adac6cb4}
			                                                                                                      
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 04]
			└─$ 
		</script>
	4. Bandera: `picoCTF{by73_5urf3r_adac6cb4}`.

**Notes**
	1. `mmls disk.flag.img`
	    - Lista la tabla de particiones de la imagen de disco.
	    - Permite ver el inicio (`Start`), fin (`End`) y tamaño (`Length`) de cada partición, para identificar la partición Linux donde está la bandera.
	2. `fls -r -o 360448 disk.flag.img | grep -i flag`
	    - `fls -r -o <offset>`: lista recursivamente los archivos de la partición en el offset indicado.
	    - `grep -i flag`: filtra los archivos que contienen la palabra “flag” (mayúscula o minúscula).
	    - Permite encontrar los inodes de los archivos que contienen la bandera.
	3. `icat -o 360448 disk.flag.img 2082`
	    - Extrae el contenido del archivo cuyo inode es `2082` en la partición con offset `360448`.
	4. `icat -o 360448 disk.flag.img 2371`
	    - Similar al anterior, extrae `flag.uni.txt` usando su inode `2371`.
	    - Este es el archivo que contiene la bandera real.

**References**
	