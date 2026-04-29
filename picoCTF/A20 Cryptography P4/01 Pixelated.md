**Challenge**
	
**Description**
	I have these 2 images, can you make a flag out of them?
	[scrambled1.png](https://challenge-files.picoctf.net/c_wily_courier/d1577440e9a1f6f9ff3eacd6ec6a4b40722de3970b527f0e07e5a4a6f1c3c3e8/scrambled1.png) 
	[scrambled2.png](https://challenge-files.picoctf.net/c_wily_courier/d1577440e9a1f6f9ff3eacd6ec6a4b40722de3970b527f0e07e5a4a6f1c3c3e8/scrambled2.png)
	**Hints**
		1. https://en.wikipedia.org/wiki/Visual_cryptography
		2. Think of different ways you can "stack" images.

**Solution**
	1. Download the images.
	2. Download the Stego solver from [Stegsolve](https://kb.offsec.nl/tools/forensics/stegsolve/).
	3. Run the `.jar` [[Files 01/setegolve.jar]]
		- Open the file [[scrambled1.png]].
			![[Files 01/Screenshot 2026-04-21 202441.png]]
		- Then Analyze > Image Combiner:
			![[Files 01/Screenshot 2026-04-21 202523.png]]
		- And select the image [[scrambled2.png]].
			![[Files 01/Screenshot 2026-04-21 202538.png]]
		- Finally you can push the button `>` to move forward and see the flag.
			![[Files 01/Screenshot 2026-04-21 202601.png]]
	4. Flag: `picoCTF{8cdf93c3}`.

**Notes**
	

**References**
	You can also get this app from the [GitHub repoitory](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install) for `Linux` and on its [Web site](https://kb.offsec.nl/tools/forensics/stegsolve/) for Windows.