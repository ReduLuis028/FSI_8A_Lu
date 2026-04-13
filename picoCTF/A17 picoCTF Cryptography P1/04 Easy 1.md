**Challenge**
	
**Description**
	The one time pad can be cryptographically secure, but not when you know the key. Can you solve this?We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this [table](https://challenge-files.picoctf.net/c_fickle_tempest/859ffc313a4d8b63149f144745043a7312fc4f993e405eeeb8ee5ae6ca8444a8/table.txt) to solve it?.
	Flag encrypted (FE): `UFJKXQZQUNB`.
	Key: `SOLVECRYPTO`.
	**Hints**
		1. Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.
		2. Please use all caps for the message.

**Solution**
	- Understand that the table corresponds to a **Vigenère cipher** (shifted alphabet table).
	- Align the ciphertext with the key:
	3. Use the table:
	    - Take the **key letter as a row**
	    - Find the **FE letter in that row**
	    - The **letter that names that column = original letter**
	4. Apply this for all letters [[Files 04/decrypt flag.py]]:
		`U F J K X Q Z Q U N B`
		`S O L V E C R Y P T O`
		`↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓` 
		`C R Y P T O I S F U N`
	5. Obtain the decrypted message: `CRYPTOISFUN`.
	6. Use the format for the flag: `picoCTF{CRYPTOISFUN}`.

**Notes**
	

**References**
	