**Challenge**
	
**Description**
	We found this weird message being passed around on the servers, we think we have a working decryption scheme.Download the message [here](https://artifacts.picoctf.net/c/127/message.txt).
	Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
	Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)
	**Hints**
		1. Do you know what `mod 37` means?
		2. `mod 37` means modulo 37. It gives the remainder of a number after being divided by 37.

**Solution**
	1. Download the file.
	2. Read the numebrs and apply `mod 37` to each one.
	3. Convert results using [[Files 02/solveMod37.py]]:
	    - `0–25 → A–Z`
	    - `26–35 → 0–9`
	    - `36 → _`
	4. Join all characters to form the message.
	5. Wrap it as a flag: `picoCTF{...}`.
	6. Flag `picoCTF{R0UND_N_R0UND_79C18FB3}`.

**Notes**
	

**References**
	