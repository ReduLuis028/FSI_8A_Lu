**Challenge**
	
**Description**
	In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding!The source code for this vault is here: [VaultDoor5.java](https://challenge-files.picoctf.net/c_fickle_tempest/676c61b70bd76ad210af911bd9cc981a14c6dd2c81ad6f8c79e7de9688b6564b/VaultDoor5.java)
	**Hints**
		1. You may find an encoder/decoder tool helpful, such as https://encoding.tools/
		2. Read the wikipedia articles on URL encoding and base 64 encoding to understand how they work and what the results look like.

**Solution**
	1. Identify the transformation:
		`password → URL encode → Base64 encode → expected`
	2. Reverse the process:
		`expected → Base64 decode → URL decode → password`
	3. Python script used [[solveVaultDoor5.py]].
	4. Output `c0nv3rt1ng_fr0m_ba5e_64_d1948d4e`.
	5. Flag: `picoCTF{c0nv3rt1ng_fr0m_ba5e_64_d1948d4e}`.

**Notes**
	

**References**
	