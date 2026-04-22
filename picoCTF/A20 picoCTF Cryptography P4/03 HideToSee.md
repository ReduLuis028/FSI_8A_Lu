**Challenge**
	
**Description**
	How about some hide and seek heh?
	Look at this image [here](https://artifacts.picoctf.net/c/239/atbash.jpg).
	**Hints**
		1. Download the image and try to extract it.

**Solution**
	1. Download the image.
	2. Go to the website [Aperi'Solve](https://aperisolve.com/), upload the image and click on `Analyze image`:
		![[Files 03/Screenshot 2026-04-21 213528.png]]
	3. Then you are going to get the following, a set of images, download them as 7z:
		![[Files 03/Aperi'Solve - Steganography Analysis - [aperisolve.com].png]]
	4. So you have to download and extract the [[steghide.7z]] file, then copy the text that has the file encrypted.txt:
		In my case that text was `krxlXGU{zgyzhs_xizxp_1u84w779}`.
		![[Files 03/Screenshot 2026-04-21 214603.png]]
	5. Finally, we decrypt the flag on the website [Atbash Cipher](https://www.dcode.fr/atbash-cipher):
		![[Files 03/Screenshot 2026-04-21 215048.png]]
	6. Flag: `picoCTF{atbash_crack_1f84d779}`.

**Notes**
	

**References**
	1. https://aperisolve.com/
	2. https://www.dcode.fr/en