**Reto**
	
**Descripción**
	Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!You can download the challenge files here: [challenge.zip](https://artifacts.picoctf.net/c_atlas/19/challenge.zip)
	`ssh -p 58248 ctf-player@atlas.picoctf.net`Using the password `1db87a14`. Accept the fingerprint with `yes`, and `ls` once connected to begin. Remember, in a shell, passwords are hidden!

**Solución**
	1. Usando terminal de picoCTF
		Lui5-picoctf@webshell:~$ ssh -p 58248 ctf-player@atlas.picoctf.net
		ctf-player@atlas.picoctf.net's password: 
		Welcome to the Binary Search Game!
		I'm thinking of a number between 1 and 1000.
		Enter your guess: 500
		Lower! Try again.
		Enter your guess: 250
		Higher! Try again.
		Enter your guess: 375
		Lower! Try again.
		Enter your guess: 312
		Lower! Try again.
		Enter your guess: 281
		Higher! Try again.
		Enter your guess: 296
		Higher! Try again.
		Enter your guess: 304
		Higher! Try again.
		Enter your guess: 308
		Lower! Try again.
		Enter your guess: 306
		Higher! Try again.
		Enter your guess: 307
		Congratulations! You guessed the correct number: 307
		Here's your flag: picoCTF{g00d_gu355_1597707f}
		Connection to atlas.picoctf.net closed.
		Lui5-picoctf@webshell:~$ 
		
**Notes**
/		1. Cómo funciona el juego:
		Te pide un número entre 1 y 1000.
		Te indica si el número secreto es mayor (“Higher!”) o menor (“Lower!”) que tu intento.
		Solo se tienen 10 intentos para acertar.
		Cuando aciertas, muestra la bandera.

/		2. Método utilizado:
		Aplicaste búsqueda binaria, dividiendo el rango a la mitad en cada intento para encontrar el número secreto de manera eficiente:
		Rango inicial: low = 1, high = 1000
		Primer intento: medio del rango (mid = (low + high)//2)
		Ajustas el rango según la pista del juego.
		Se repitió hasta adivinar el número secreto (307).
		Esto garantiza encontrar el número en máximo 10 intentos, sin adivinar al azar.

/		3. Resultados:
		Número secreto encontrado: 307
		Bandera obtenida: picoCTF{g00d_gu355_1597707f}

/		4. Aprendizaje:
		La búsqueda binaria es un algoritmo muy eficiente para encontrar elementos en un rango ordenado.
		Practicarla manualmente ayuda a entender cómo funcionan los algoritmos antes de automatizarlos.

**Referencias**
	