**Challenge**
	
**Description**
	We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it?
	Download the leak [here](https://artifacts.picoctf.net/c/151/leak.tar).
	The first user in `usernames.txt` corresponds to the first password in `passwords.txt`.
	The second user corresponds to the second password, and so on.
	**Hints**
		1. Maybe other passwords will have hints about the leak?

**Solution**
	1. Extract the `.tar` file to obtain:
	    - `usernames.txt`
	    - `passwords.txt`
	2. Match usernames with passwords by index.
	3. Locate the user `cultiris` in `usernames.txt` and obtain its corresponding password from `passwords.txt`.
	4. The encrypted password obtained is:
		`cvpbPGS{P7e1S_54I35_71Z3}`.
	5. Notice that the format resembles a flag but is not readable. This suggests a simple cipher.
	6. To test all possible shifts of a **Caesar cipher**, use the following Python script ([[decryptTheUserCultiris.py]]).
		<script>
			[+] Found password: cvpbPGS{P7e1S_54I35_71Z3}
			
			[+] Trying Base64:
			        Not Base64
			
			[+] Trying Hex:
			        Not Hex
			
			[+] Trying Caesar shifts:
			
			[+] Found flag (shift 13): picoCTF{C7r1F_54V35_71M3}
		</script>
	7. Running the script reveals the correct shift (13) and outputs the flag: `picoCTF{C7r1F_54V35_71M3}`.

**Notes**
	

**References**
	