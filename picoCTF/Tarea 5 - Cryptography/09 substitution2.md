**Challenge**
	
**Description**
	It seems that another encrypted message has been intercepted. The encryptor seems to have learned their lesson though and now there isn't any punctuation! Can you still crack the cipher?Download the message [here](https://artifacts.picoctf.net/c/112/message.txt).
	**Hints**
		1. Try refining your frequency attack, maybe analyzing groups of letters would improve your results?

**Solution**
	1. Download the `message`.
	2. Go to th website [Mono-alphabetic Substitution](https://www.dcode.fr/monoalphabetic-substitution), copy the message in `message.txt` and click on the `Decrypt Automatically` button:
		![[Files 09/Monoalphabetic Substitution Cipher - Online Cryptogram Decoder, Sol_ - [www.dcode.fr].png]]
	3. Flag: `PICOCTF{N6R4M_4N41Y515_15_73D10U5_8E1BF808}`.

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
	