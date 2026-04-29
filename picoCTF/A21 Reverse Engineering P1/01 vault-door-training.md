**Challenge**
	
**Description**
	Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project.
	The laboratory is protected by a series of locked vault doors.
	Each door is controlled by a computer and requires a password to open.
	Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer!
	You will need to read the source code for each level to figure out what the password is for that vault door.
	As a warmup, we have created a replica vault in our training facility.The source code for the training vault is here: [VaultDoorTraining.java](https://challenge-files.picoctf.net/c_fickle_tempest/894d84f5b5e66228fa8e422d898a42adf4fd8298aa8d322decaf9b172ba276ea/VaultDoorTraining.java)
	**Hints**
		1. (None)

**Solution**
	1. By analyzing the source code (`VaultDoorTraining.java`), we see that the program expects an input in the format: `picoCTF{...}`.
	2. The program removes the prefix `picoCTF{` and the closing `}` using:
		<script>
		    String input = userInput.substring("picoCTF{".length(), userInput.length()-1);
	    </script>
	3. Then, the `checkPassword` method compares the extracted string with a hardcoded value:
		<script>
		    return password.equals("w4rm1ng_Up_w1tH_jAv4_000HPpgh7Ph");
	    </script>
	4. Therefore, the actual password is:
		`w4rm1ng_Up_w1tH_jAv4_000HPpgh7Ph`.
	5. Since the program expects the full format `picoCTF{password}`, the flag is:
		`picoCTF{w4rm1ng_Up_w1tH_jAv4_000HPpgh7Ph}`.

**Notes**
	

**References**
	