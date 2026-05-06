**Challenge**
	
**Description**
	This service can provide you with a random number, but can it do anything else?
	Connect to the program with netcat:`$ nc saturn.picoctf.net 55392`
	The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/515/picker-I.py).
	**Hints**
		1. Can you point the program to a function that does something useful for you?

**Solution**
	1. Download the `picker-I.py` file and analyze it.
	2. Then you can see a function `win()` that open a file called `flag.txt`.
	3. So, `eval(user_input + '()')` means you can insert any input and the code will add `()` to the end of whatever it is.
		<script>
			┌──(kali㉿kali)-[~]
			└─$ nc saturn.picoctf.net 55392
			Try entering "getRandomNumber" without the double quotes...
			==> win
			0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x63 0x65 0x34 0x62 0x35 0x64 0x35 0x62 0x7d 
		</script>
	4. Now we decode the hex format into ASCII with the code [[Files 03/solveHex.py]].
	5. Flag `picoCTF{4_d14m0nd_1n_7h3_r0ugh_ce4b5d5b}`.

**Notes**
	

**References**
	