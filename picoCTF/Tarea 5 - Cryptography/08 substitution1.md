**Challenge**
	
**Description**
	A second message has come in the mail, and it seems almost identical to the first one. Maybe the same thing will work again.
	Download the message [here](https://artifacts.picoctf.net/c/182/message.txt).
	**Hints**
		1. Try a frequency attack.
		2. Do the punctuation and the individual words help you make any substitutions?

**Solution**
	1. Download the `message`.
	2. Go to th website [Mono-alphabetic Substitution](https://www.dcode.fr/monoalphabetic-substitution), copy the message in `message.txt` and click on the `Decrypt Automatically` button:
		![[Files 08/Monoalphabetic Substitution Cipher - Online Cryptogram Decoder, Sol_ - [www.dcode.fr].png]]
	3. Flag: `PICOCTF{FR3QU3NCY_4774CK5_4R3_C001_7AA384BC}`.

**Notes**
	1. This cipher replaces each letter with another letter using a fixed rule (a “key”).
	2. You make a scrambled alphabet (example key):
	    - Plain: ABCDEFGHIJKLMNOPQRSTUVWXYZ
	    - Cipher: QWERTYUIOPASDFGHJKLZXCVBNM
	3. Then you replace letters one by one:
	    - A → Q
	    - B → W
	    - C → E
	    - etc.
	4. So a word like **HELLO** becomes something like **ITSSO** (depends on the key).
	5. **Important idea:**
		- The same letter is always replaced the same way.
		- So “A” is always the same cipher letter everywhere.
	6. **How it is broken (inside idea):**
		- It keeps language patterns (like letter frequency).
		- For example, in English, “E” is very common, so attackers guess it from frequency.

**References**
	