**Challenge**
	
**Description**
	Download this disk image and find the flag.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
	 [Download compressed disk image](https://artifacts.picoctf.net/c/212/disk.flag.img.gz)
	**Hints**
		1. None

**Solution**
	1. Extraer el archivo `disk.flag.img.gz`.
	2. Comandos a usar:
		- `mmls disk.flag.img`
		- `fls -r -o Start disk.flag.img | grep -i flag` → Start = 0000411648 → 411648
		- `icat -o Start disk.flag.img 1876` → 1876 = flag.txt
		- `icat -o Start disk.flag.img 1782` → 1782 = flag.txt.enc 
		- `icat -o Start disk.flag.img 1782 > flag.txt.enc` → Extraer contenido del inode `1782` y enviarlo a un archivo local `flag.txt.enc`
		- `openssl aes256 -salt -d -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567` → Desencriptar la bandera
		- `cat flag.txt`
	3. Una vez hecho, usar CLI:
		<script class = "CLI kali-linux">
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 05]
			└─$ mmls disk.flag.img   
			DOS Partition Table
			Offset Sector: 0
			Units are in 512-byte sectors
			
			      Slot      Start        End          Length       Description
			000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
			001:  -------   0000000000   0000002047   0000002048   Unallocated
			002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
			003:  000:001   0000206848   0000411647   0000204800   Linux Swap / Solaris x86 (0x82)
			004:  000:002   0000411648   0000819199   0000407552   Linux (0x83)
			                                                                                                      
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 05]
			└─$ fls -r -o 411648 disk.flag.img | grep -i flag
			+ r/r * 1876(realloc):  flag.txt
			+ r/r 1782:     flag.txt.enc
			                                                                                                      
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 05]
			└─$ icat -o 411648 disk.flag.img 1876
			           -0.881573            34.311733
			                                                                                                      
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 05]
			└─$ icat -o 411648 disk.flag.img 1782
			Salted__0��!�-6V����0��U��l��&�:�pj_1�0�|�h
			                                           �Ȥ7� ���؎$�'%                                                                                                      
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 05]
			└─$ icat -o 411648 disk.flag.img 1782 > flag.txt.enc
			                                                                                                      
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 05]
			└─$ openssl aes256 -salt -d -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567
			*** WARNING : deprecated key derivation used.
			Using -iter or -pbkdf2 would be better.
			bad decrypt
			40A72771987F0000:error:1C800064:Provider routines:ossl_cipher_unpadblock:bad decrypt:../providers/implementations/ciphers/ciphercommon_block.c:107:
			                                                                                                      
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 05]
			└─$ cat flag.txt
			picoCTF{h4un71ng_p457_0a710765}                                                                                                      
			                                                                                                      
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 05]
			└─$ 
		</script>
	4. Bandera: `picoCTF{h4un71ng_p457_0a710765}`.

**Notes**
	1. `mmls disk.flag.img`
	    - Lista la tabla de particiones de la imagen de disco.
	    - Permite ver el inicio (`Start`), fin (`End`) y tamaño (`Length`) de cada partición, para identificar la partición Linux donde está la bandera.
	2. `fls -r -o 411648 disk.flag.img | grep -i flag`
	    - `fls -r -o <offset>`: lista recursivamente todos los archivos de la partición indicada por el offset (`411648`).
	    - `grep -i flag`: filtra solo los archivos cuyo nombre contenga “flag”, como `flag.txt` o `flag.txt.enc`.
	    - Resultado: inodes de los archivos de interés (`1876` = flag.txt, `1782` = flag.txt.enc).
	3. `icat -o 411648 disk.flag.img 1876`
	    - Extrae el contenido del archivo cuyo inode es `1876`.
	    - En este caso, muestra datos legibles que podrían incluir coordenadas o información previa a la bandera.
	4. `icat -o 411648 disk.flag.img 1782`
	    - Extrae el archivo cifrado `flag.txt.enc` desde la imagen, mostrando datos binarios (no legibles).
	5. `icat -o 411648 disk.flag.img 1782 > flag.txt.enc`
	    - Redirige la salida de `icat` al archivo local `flag.txt.enc` para poder descifrarlo con OpenSSL.
	6. `openssl aes256 -salt -d -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567`
	    - Desencripta `flag.txt.enc` usando AES-256 y la contraseña proporcionada.
	    - Genera `flag.txt` que contiene la bandera.
	7. `cat flag.txt`
	    - Muestra el contenido de `flag.txt`, revelando la bandera:

**References**
	