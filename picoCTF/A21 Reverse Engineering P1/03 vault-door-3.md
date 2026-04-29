**Challenge**
	
**Description**
	This vault uses for-loops and byte arrays.
	The source code for this vault is here: [VaultDoor3.java](https://challenge-files.picoctf.net/c_fickle_tempest/d2e2ce5be3c6983378013b304e34bbcfe51617a2f3ec987437028efbdbd93c83/VaultDoor3.java)
	**Hints**
		1. Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.

**Solution**
	1. The program (`VaultDoor3.java`) does not compare the password directly. Instead, it rearranges the input using several loops and stores the result in a `buffer`, which is then compared to a fixed string:
	    `jU5t_a_sna_3lpm13gf49_u_4_m9r540`
	2. Instead of manually reversing the logic, I replicated the exact same transformations in my own code, but using the known target string as input.
	3. I created a custom Java program [[solveVaultDoor3.java]]
	4. This program applies the same transformations as the original vault, effectively reconstructing the correct password automatically.
	5. Finally, the output of the program gives the valid flag in the required format: `picoCTF{...}`.
	6. Flag: `picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_99f530}`

**Notes**
	

**References**
	