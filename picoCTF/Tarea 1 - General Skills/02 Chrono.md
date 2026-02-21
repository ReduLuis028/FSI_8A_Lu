**Reto**
	
**Descripción**
	How to automate tasks to run at intervals on linux servers?Use ssh to connect to this server:
	Server: saturn.picoctf.net
	Port: 65425
	Username: picoplayer 
	Password: bLgSMmbY6X

**Solución**
	 1. Usando terminal de pcioCTF
		Lui5-picoctf@webshell:~$ ssh -p 65425 picoplayer@saturn.picoctf.net
		The authenticity of host '[saturn.picoctf.net]:65425 ([13.59.203.175]:65425)' can't be established.
		ED25519 key fingerprint is SHA256:dMTscRrUiURy7uMu5eGWwEKdd2FzqLzx6LfWhssWnNQ.
		This host key is known by the following other names/addresses:
		    ~/.ssh/known_hosts:16: [hashed name]
		Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
		Warning: Permanently added '[saturn.picoctf.net]:65425' (ED25519) to the list of known hosts.
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
		
		picoplayer@challenge:~$ cat /etc/crontab
		# picoCTF{Sch3DUL7NG_T45K3_L1NUX_1b4d8744}
		picoplayer@challenge:~$ 
		
**Notes**
/       1. Funcionamiento del reto:
		El reto se centra en el conocimiento del sistema de archivos de Linux y la ubicación de archivos de configuración para tareas automáticas.
		La flag estaba escondida como un comentario dentro de la tabla de cron (crontab).

/       2. Método utilizado:
		Conexión remota segura (SSH).
		Uso del comando cat para leer archivos de configuración del sistema en el directorio /etc/.

/       3. Resultados:
		Bandera obtenida: picoCTF{Sch3DUL7NG_T45K3_L1NUX_1b4d8744}

/       4. Aprendizaje:
		Cron y Crontab: Es el administrador de procesos en segundo plano que ejecuta scripts o comandos a intervalos regulares (minutos, horas, días).
		Rutas Críticas: /etc/crontab es un archivo fundamental para administradores de sistemas y un punto común de revisión en auditorías de seguridad

**Referencias**
	