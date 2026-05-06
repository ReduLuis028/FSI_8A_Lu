**Challenge**
	
**Description**
	Can you open this safe?I forgot the key to my safe but this [program](https://artifacts.picoctf.net/c/83/SafeOpener.java) is supposed to help me with retrieving the lost key.
	Can you help me unlock my safe?
	Put the password you recover into the picoCTF flag format like:`picoCTF{password}`
	**Hints**
		1. (None)

**Solution**
	1. Download and open the `file.java`.
	2. Analyze it and search for something to decrypt
		- In this case a coe in base64: `cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz`.
	3. Decrypt the base64 with the following code in Pyhton [[Files 01/solvebase64.py]].
	4. Then we get the flag: `picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}`.

**Notes**
	

**References**
	