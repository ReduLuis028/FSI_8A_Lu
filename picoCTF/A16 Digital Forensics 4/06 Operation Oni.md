**Challenge**
	
**Description**
	Download this disk image, find the key and log into the remote machine.
	Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
	[Download disk image](https://artifacts.picoctf.net/c/71/disk.img.gz)
	Remote machine: `ssh -i key_file -p 52003 ctf-player@saturn.picoctf.net`
		**Hints**
		1. None

**Solution**
	1. Extraer el archivo `disk.img.gz`.
	2. Comandos a usar:
		- `mmls disk.img`
		- `fls -o Start disk.im` → Start = 0000206848 → 206848
		- `fls -o 206848 disk.img 470` → 470 = Listar el contenido del inode `470` (`root` = usuario/administrador principal del equipo)
		- `fls -o 206848 disk.img 3916` → 3916 = Listar el contenido del inode `3916` (`ssh` = conexión segura mediante el interprete de comandos)
		- `icat -o 206848 disk.img 2345 > id_ed25519` → Extraer contenido del inode `2345` y enviarlo a un archivo local `id_ed25519`
		- `chmod 600 id_ed25519` → 
		- `ssh -i id_ed25519 -p 52003 ctf-player@saturn.picoctf.net`
		- `ls`
		- `cat flag.txt`
	3. Una vez hecho, usar CLI:
		<script>
			┌──(kali㉿kali)-[~]
			└─$ mmls disk.img
			DOS Partition Table
			Offset Sector: 0
			Units are in 512-byte sectors
			
			      Slot      Start        End          Length       Description
			000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
			001:  -------   0000000000   0000002047   0000002048   Unallocated
			002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
			003:  000:001   0000206848   0000471039   0000264192   Linux (0x83)
			                                                                                                      
			┌──(kali㉿kali)-[~]
			└─$ fls -o 206848 disk.img     
			d/d 458:        home
			d/d 11: lost+found
			d/d 12: boot
			d/d 13: etc
			d/d 79: proc
			d/d 80: dev
			d/d 81: tmp
			d/d 82: lib
			d/d 85: var
			d/d 94: usr
			d/d 104:        bin
			d/d 118:        sbin
			d/d 464:        media
			d/d 468:        mnt
			d/d 469:        opt
			d/d 470:        root
			d/d 471:        run
			d/d 473:        srv
			d/d 474:        sys
			V/V 33049:      $OrphanFiles
			                                                                                                      
			┌──(kali㉿kali)-[~]
			└─$ fls -o 206848 disk.img 470 
			r/r 2344:       .ash_history
			d/d 3916:       .ssh
			                                                                                                      
			┌──(kali㉿kali)-[~]
			└─$ fls -o 206848 disk.img 3916
			r/r 2345:       id_ed25519
			r/r 2346:       id_ed25519.pub
			                                                                                                      
			┌──(kali㉿kali)-[~]
			└─$ icat -o 206848 disk.img 2345 > id_ed25519
			                                                                                                      
			┌──(kali㉿kali)-[~]
			└─$ chmod 600 id_ed25519
			                                                                                                      
			┌──(kali㉿kali)-[~]
			└─$ ssh -i id_ed25519 -p 52003 ctf-player@saturn.picoctf.net
			** WARNING: connection is not using a post-quantum key exchange algorithm.
			** This session may be vulnerable to "store now, decrypt later" attacks.
			** The server may need to be upgraded. See https://openssh.com/pq.html
			Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 6.8.0-1047-aws x86_64)
			
			 * Documentation:  https://help.ubuntu.com
			 * Management:     https://landscape.canonical.com
			 * Support:        https://ubuntu.com/advantage
			
			This system has been minimized by removing packages and content that are
			not required on a system that users do not log into.
			
			To restore this content, you can run the 'unminimize' command.
			
			The programs included with the Ubuntu system are free software;
			the exact distribution terms for each program are described in the
			individual files in /usr/share/doc/*/copyright.
			
			Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
			applicable law.
			
			ctf-player@challenge:~$ ls
			flag.txt
			ctf-player@challenge:~$ cat flag.txt
			picoCTF{k3y_5l3u7h_af277f77}
		</script>
	4. Bandera: `picoCTF{k3y_5l3u7h_af277f77}`.

**Notes**
	1. `mmls disk.img`
	    - Lista la tabla de particiones de la imagen de disco.
	    - Permite identificar las particiones Linux y sus offsets en sectores.
	2. `fls -o 206848 disk.img`
	    - Lista los archivos y directorios de la partición con offset `206848`.
	    - Resultado: directorios principales (`home`, `boot`, `root`, etc.), incluyendo `root` donde se encuentra la llave SSH.
	3. `fls -o 206848 disk.img 470`
	    - Lista el contenido del directorio con inode `470` (que corresponde a `/root`).
	    - Resultado: `.ash_history`, `.ssh` (directorio que contiene la llave).
	4. `fls -o 206848 disk.img 3916`
	    - Lista el contenido del directorio `.ssh` (inode `3916`).
	    - Resultado: `id_ed25519` (llave privada) y `id_ed25519.pub` (llave pública).
	5. `icat -o 206848 disk.img 2345 > id_ed25519`
	    - Extrae el archivo con inode `2345` (llave privada `id_ed25519`) y lo guarda localmente.
	6. `chmod 600 id_ed25519`
	    - Cambia los permisos de la llave privada para que solo el usuario actual pueda leer/escribir, necesario para SSH.
	7. `ssh -i id_ed25519 -p 52003 ctf-player@saturn.picoctf.net`
	    - Se conecta al servidor remoto usando la llave privada extraída, puerto `52003` y usuario `ctf-player`.
	8. `ls`
	    - Lista archivos en el directorio remoto; permite ver que `flag.txt` está presente.
	9. `cat flag.txt`
	    - Muestra el contenido de la bandera:

**References**
	