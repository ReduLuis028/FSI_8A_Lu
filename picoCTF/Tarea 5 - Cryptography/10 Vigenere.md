**Challenge**
	
**Description**
	Can you decrypt this message?Decrypt this [message](https://artifacts.picoctf.net/c/158/cipher.txt) using this key "CYLAB".
	**Hints**
		1. https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

**Solution**
	1. Download the `message`.
	2. Go to the website [Vigenere Cipher](https://www.dcode.fr/vigenere-cipher), copy the message in `message.txt` on the textbox, the next is copy the key `CYLAB` in the `Knowing the Key/Password:` textbox and then click on `Decrypt`:
		![[Screenshot 2026-04-26 201221.png]]
	3. Flag: `picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_ae82272q}`.

**Notes**
	1. This cipher uses a **keyword** to change each letter of the message.
	2. It is like a **monoalphabetic substitution that changes every time**, depending on the key.
	3. How it works
		1. You choose a keyword  
		    - Example: `KEY`
		2. You repeat it until it matches the message length  
		    - Message: `HELLOWORLD`  
		    - Key: `KEYKEYKEYKE`
		3. Each letter is shifted using the key letter (like a Caesar shift, but changing each time)
		Each letter has a number: `A = 0, B = 1, C = 2, ... Z = 25`
		Then: `Cipher = (Plain letter + Key letter) mod 26`
	4. Simple example
		- Let’s encrypt:
		- Message: **HELLO**  
		- Key: **KEYKE**
			We shift each letter:
				- H + K → R
				- E + E → I
				- L + Y → J
				- L + K → V
				- O + E → S
		- Result: **RIJVS**
	5. Important idea
		- It is NOT one fixed substitution
		- The same letter can become different letters depending on position
		- That makes it stronger than monoalphabetic substitution
	6. How it is broken (basic idea)
		- If the key is short, patterns repeat
		- Cryptanalysis looks for repeated cycles
		- Once the key length is guessed, it becomes multiple Caesar ciphers

**References**
	