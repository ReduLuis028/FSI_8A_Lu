**Challenge**
	
**Description**
	Can you figure out how this program works to get the flag?
	Connect to the program with netcat:`$ nc saturn.picoctf.net 49233`
	The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/529/picker-IV.c).
	The binary can be downloaded [here](https://artifacts.picoctf.net/c/529/picker-IV).
	**Hints**
		1. With Python, there are no binaries. With compiled languages like C, there is source code, and there are binaries. Binaries are created from source code, they are a conversion from the human-readable source code, to the highly efficient machine language, in this case: x86_64.
		2. How can you find the address that `win` is at?

**Solution**
	1. Download the binary `picker-IV` and analyze it using a decompiler (e.g., Ghidra, Binary Ninja, or Hex-Rays).
	2. From the decompiled code (as seen in the image), identify the function:
		- This function prints the flag, so the goal is to execute it.
			<script>
				int win() {
					puts("You won!");
					stream = fopen("flag.txt", "r");
					...
				}
			</script>
		- Image:
			![[Files 06/Screenshot 2026-05-06 101246.png]]
	3. Analyze the `main` function:
		<script>
			printf("Enter the address in hex to jump to, excluding '0x': ");
			__isoc99_scanf("%x", &v4);
			printf("You input 0x%x\n", v4);
			((void (*)(void))v4)();
		</script>
		The program:
			- Takes a user input (hex address).
			- Casts it to a function pointer.
			- Executes it.
			- This means you can jump to **any function in memory**.
	4. Find the address of `win`
		From the decompiler (image), `win` is located at: `40129E`.
	5. Connect to the service and input the address:
		<script>
			C:\Users\luise>ncat saturn.picoctf.net 49233
			Enter the address in hex to jump to, excluding '0x': 40129E
			You input 0x40129e
			You won!
			picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_b8de1af4}
		</script>
	6. Flag: `picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_b8de1af4}`.

**Notes**
	

**References**
	