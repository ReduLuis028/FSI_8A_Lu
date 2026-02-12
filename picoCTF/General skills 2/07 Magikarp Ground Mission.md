**Reto**
	
**Descripción**
	Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin.
	Login via `ssh` as `ctf-player` with the password, `8c606eb1` on the host `wily-courier.picoctf.net` and port `58012`.
	
**Solución**
	1. Usando termina e picoCTF
		Lui5-picoctf@webshell:~$ ssh ctf-player@wily-courier.picoctf.net -p 58012
		The authenticity of host '[wily-courier.picoctf.net]:58012 ([18.189.99.27]:58012)' can't be established.
		ED25519 key fingerprint is SHA256:ErlUUvYlrAxfSW1tIdzfOnGTBSr5OFkZvz0nMN4Vodw.
		This host key is known by the following other names/addresses:
		    ~/.ssh/known_hosts:3: [hashed name]
		Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
		Warning: Permanently added '[wily-courier.picoctf.net]:58012' (ED25519) to the list of known hosts.
		ctf-player@wily-courier.picoctf.net's password: 
		Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 6.14.0-1012-aws x86_64)
		
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
		
		ctf-player@pico-chall$ ls
		1of3.flag.txt  instructions-to-2of3.txt
		ctf-player@pico-chall$ cat 1of3.flag.txt
		picoCTF{xxsh_
		
		ctf-player@pico-chall$ cat instructions-to-2of3.txt
		Next, go to the root of all things, more succinctly `/`
		ctf-player@pico-chall$ cd /
		ctf-player@pico-chall$ ls
		2of3.flag.txt  boot       dev  home                      lib    media  opt   root  sbin  sys  usr
		bin            challenge  etc  instructions-to-3of3.txt  lib64  mnt    proc  run   srv   tmp  var
		ctf-player@pico-chall$ cat 2of3.flag.txt
		0ut_0f_//4t3r_
		
		ctf-player@pico-chall$ cat instructions-to-3of3.txt
		Lastly, ctf-player, go home... more succinctly `~`
		ctf-player@pico-chall$ cd ~
		ctf-player@pico-chall$ ls
		3of3.flag.txt  drop-in
		ctf-player@pico-chall$ cat 3of3.flag.txt
		0b24fc4f}
		ctf-player@pico-chall$ 
		
		1ra parte: picoCTF{xxsh_
		2da parte: 0ut_0f_//4t3r_
		3ra parte: 0b24fc4f}
		
		picoCTF{xxsh_0ut_0f_//4t3r_0b24fc4f}

**Notes**
	1. `ssh usuario@host -p puerto` permite conectarse a un servidor remoto por terminal.
	2. `ls` lista los archivos y directorios del directorio actual.
	3. `cat archivo` muestra el contenido de un archivo de texto.
	4. `cd /` mueve al directorio raíz del sistema.
	5. `cd ~` regresa al directorio home del usuario actual.
	6. Las rutas especiales `/` (raíz) y `~` (home) son atajos importantes para navegar rápido.
	7. Leer archivos de instrucciones dentro del sistema ayuda a encontrar las siguientes ubicaciones de la flag.
	8. Algunas flags están divididas en partes y deben unirse en orden para formar el resultado final.

**Referencias**