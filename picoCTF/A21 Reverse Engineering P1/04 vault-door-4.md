**Challenge**
	
**Description**
	This vault uses ASCII encoding for the password.
	The source code for this vault is here: [VaultDoor4.java](https://challenge-files.picoctf.net/c_fickle_tempest/5a242afc9022df976b1c18fe9364788579431217536fca41006714b29d8931e1/VaultDoor4.java)
	**Hints**
		1. Use a search engine to find an "ASCII table"
		2. You will also need to know the difference between octal, decimal, and hexadecimal numbers.

**Solution**
	1. Analyze the byte array:
		<script class = "Java">
			byte[] myBytes = {106, 85, 53, 116, 95, 52, 95, 98, 0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f, 0142, 0131, 0164, 063, 0163, 0137, 040, 063, '0', 'd', 'c', '8', '5', 'b', 'e', 'd'};
		</script>
	2. Convert each value to ASCII:
		- Character → direct
		- Decimal → `chr(n)`
		- Octal → `chr(int(x,8))`
		- Hex → `chr(int(x,16))`
	3. Script used [[solveVaultDoor4.py]].
	4. Output: `jU5t_4_bUnCh_0f_bYt3s_30dc85bed`.
	5. Flag: `picoCTF{jU5t_4_bUnCh_0f_bYt3s_30dc85bed}`.

**Notes**
	

**References**
	