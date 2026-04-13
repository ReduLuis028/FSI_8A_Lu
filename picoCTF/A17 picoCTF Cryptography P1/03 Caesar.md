**Challenge**
	
**Description**
	Decrypt this message.Message: 	[message](https://challenge-files.picoctf.net/c_fickle_tempest/416ba12d66a8544f2d97e21fb165aa02f99c01ea26c5cec454a98c24c2e538d0/data.enc)
	**Hints**
		1. Caesar cipher tutorial

**Solution**
	1. Download the file.
	2. Search for the flag pico in the file:
		<script class = "Powershell">
			PS C:\Users\luise\Downloads> strings data.enc | Select-String picoCTF
			
			picoCTF{mbyccsxqdrobelsmyxigfknnoo}
		</script>
	3. With this information, go to the following page [Caesar Cipher](https://www.dcode.fr/caesar-cipher) and decrypt what is in parentheses of the flag previously obtained.
		![[Files 03/Screenshot 2026-04-13 091605.png]]
	4. Then we have the flag: `picoCTF{crossingtherubiconywvaddee}`.

**Notes**
	

**References**
	https://www.dcode.fr/en