**Challenge**
	
**Description**
	A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher). Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it?
	Download the message [here](https://artifacts.picoctf.net/c/190/message.txt).Put the decoded message in the picoCTF flag format, `picoCTF{decoded_message}`.
	**Hints**
		1. Once you've understood how the cipher works, it's best to draw it out yourself on paper

**Solution**
	1. Downloa the `file.txt`.
	2. Obtain the text in it. `Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA`.
	3. Use the following website [Rail Fence (Zig-Zag) Cipher](https://www.dcode.fr/rail-fence-cipher), click on the `Keep punctuation and spaces` checkbox and the `Automatic Decryption` button to see the decrypted flag:
		![[Rail Fence (Zig-Zag) Cipher - Online Decoder, Encoder, Solver_ - [www.dcode.fr].png]]
	4. Wrap the flag in the Pico format: `picoCTF{...}`.
	5. Flag: `picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3}`.

**Notes**
	1. This is a _transposition cipher_ (it does NOT change letters, only their position).
	2. You write the message in a zig-zag pattern across several rows.
	3. Example with 3 rails:
	4. Message: **WEAREDISCOVEREDFLEEATONCE**
	5. Write it like this:
		`W   E   C   R   L   T   E  `
		` E R D S O E E F E A O C   `
		`  A   I   V   D   E   N    `
	6. Then you read row by row:
		Cipher text:  **WECRLTEERDSOEEFEAOCAIVDEN**
	7. **Important idea:**
		- Letters stay the same
		- Only their positions are shuffled in a zig-zag pattern
	8. **How it is broken (inside idea):**
		- You try different rail numbers (2, 3, 4…)
		- Then rebuild the zig-zag until the message makes sense

**References**
	https://www.dcode.fr/rail-fence-cipher