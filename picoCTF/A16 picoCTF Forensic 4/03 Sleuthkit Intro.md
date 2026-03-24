**Challenge**
	
**Description**
	Download the disk image and use `mmls` on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag.
	Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
	[Download disk image](https://artifacts.picoctf.net/c/164/disk.img.gz)
	Access checker program: `nc saturn.picoctf.net 50700`
	**Hints**
		1. None

**Solution**
	1. Extraer el archivo `disk.img.gz`.
	2. Comandos a usar:
		- `mmls disk.img`
		- `nc saturn.picoctf.net 50700`
	3. Una vez hecho, usar CLI:
		<script class = "CLI kali-linux">
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archvios 03]
			└─$ mmls disk.img
			DOS Partition Table
			Offset Sector: 0
			Units are in 512-byte sectors
			
			      Slot      Start        End          Length       Description
			000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
			001:  -------   0000000000   0000002047   0000002048   Unallocated
			002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)
			                                                                                  
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archvios 03]
			└─$ nc saturn.picoctf.net 50700
			What is the size of the Linux partition in the given disk image?
			Length in sectors: 202752
			202752
			Great work!
			picoCTF{mm15_f7w!}
			                                                                                  
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archvios 03]
			└─$ 
		</script>
	4. Bandera: `picoCTF{mm15_f7w!}`.

**Notes**
	1. `mmls disk.img`
	    - Lista la tabla de particiones de la imagen de disco.
	    - Permite ver el inicio (`Start`), fin (`End`) y tamaño (`Length`) de cada partición, para identificar la partición Linux donde está la bandera.
	2. `nc saturn.picoctf.net 50700`
	    - Se conecta al servicio remoto del reto con netcat.
	    - Permite enviar la respuesta (el tamaño en sectores de la partición Linux) y recibir la bandera.

**References**
	