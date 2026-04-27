**Challenge**
	
**Description**
	A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?
	Access the server using `nc verbal-sleep.picoctf.net 60516`
	**Hints**
		1. Understanding hashes is very crucial. [Read more here](https://primer.picoctf.org/#_hashing).
		2. Can you identify the hash algorithm? Look carefully at the length and structure of each hash identified.
		3. Tried using any hash cracking tools?

**Solution**
	1. Connect to the service: `nc verbal-sleep.picoctf.net 60516`
	2. The server provides a hash and asks for its password.
	3. Identify the hash type by its length:
	    - `32 characters → MD5`
	    - `40 characters → SHA-1`
	    - `64 characters → SHA-256`
	4. Crack each hash using a dictionary attack (`common passwords`).
	5. The hashes correspond to:
		- `482c811da5d5b4bc6d497ffa98491e38  → password123  `
		- `b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 → letmein  `
		- `916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745 → qwerty123`
	6. Since the challenge is multi-step, each correct password reveals the next hash.  
	    - This must be done in the same session.
	7. To automate the process, use a Python script ([[solveHashes.py]]) that:
	    - Connects to the server
	    - Extracts the hash
	    - Identifies its type
	    - Cracks it using a wordlist (e.g., `rockyou.txt`)
	    - Sends the correct password
	8. After solving all hashes, the server returns the flag.
		<script>
			Welcome!! Looking For the Secret?
			
			We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
			Enter the password for identified hash: 
			[+] Hash: 482c811da5d5b4bc6d497ffa98491e38
			[+] Password: password123
			Correct! You've cracked the MD5 hash with no secret found!
			
			Flag is yet to be revealed!! Crack this hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
			Enter the password for the identified hash: 
			[+] Hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
			[+] Password: letmein
			Correct! You've cracked the SHA-1 hash with no secret found!
			
			Almost there!! Crack this hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
			Enter the password for the identified hash: 
			[+] Hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
			[+] Password: qwerty098
			Correct! You've cracked the SHA-256 hash with a secret found. 
			The flag is: picoCTF{UseStr0nG_h@shEs_&PaSswDs!_6965e43b}
		</script>
	9. Flag: `picoCTF{UseStr0nG_h@shEs_&PaSswDs!_6965e43b}`.

**Notes**
	1. The vulnerability lies in using **weak, common passwords** with hashing.
	2. Hashing alone is not secure without salting.
	3. Dictionary attacks are effective against predictable passwords.

**References**
	