**Challenge**
	
**Description**
	The numbers... what do they mean?
	[numbers.png](https://challenge-files.picoctf.net/c_fickle_tempest/7b39deba4212c233b1628c93f16639ed02ad90f51436d2a8914bb11f74a982d3/the_numbers.png)
	**Hints**
		1. The flag is in the format PICOCTF{}

**Solution**
	1. Download the `image.png`.
	2. Get the numbers on the `.png`.
	3. Use the single substitution encryption, `A=1, ..., Z=26`.
	4. With this information, I did and run the following code: [[Files 01/Single Substitution Encryption.py]].
	5. Using the previous code, decrypt the numbers.
	6. Then we have the flag: `PICOCTF{THENUMBERSMASON}`.

**Notes**
	

**References**
	