**Reto**
	
**Descripción**
	Using a Secure Shell (SSH) is going to be pretty important.Can you `ssh` as `ctf-player` to `titan.picoctf.net` at port `61074` to get the flag?You'll also need the password `6dd28e9b`. If asked, accept the fingerprint with `yes`. If your device doesn't have a shell, you can use: [https://webshell.picoctf.org](https://webshell.picoctf.org/) If you're not sure what a shell is, check out our Primer: [https://primer.picoctf.com/#_the_shell](https://primer.picoctf.com/#_the_shell)
	
**Solución**
	1. Usando terminal de picoCTF
		Lui5-picoctf@webshell:~$ 
		Lui5-picoctf@webshell:~$ ssh ctf-player@titan.picoctf.net -p 61074
		ctf-player@titan.picoctf.net's password: 
		Welcome ctf-player, here's your flag: picoCTF{s3cur3_c0nn3ct10n_5d09a462}
		Connection to titan.picoctf.net closed.
		Lui5-picoctf@webshell:~$ 

**Notes**
	1. SSH permite conexión remota segura mediante cifrado.
	2. Se usa el comando: ssh usuario@host -p puerto.
	3. La fingerprint verifica la identidad del servidor.
	4. El reto evalúa autenticación y conexión remota básica.
	5. La flag se entrega tras login exitoso.

**Referencias**
	