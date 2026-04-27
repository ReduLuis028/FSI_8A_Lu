**Challenge**
	
**Description**
	A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?
	Download the message [here](https://artifacts.picoctf.net/c/152/message.txt).
	**Hints**
		1. Try a frequency attack. An online tool might help.

**Solution**
	1. Download the `message`.
	2. Go to th website [Mono-alphabetic Substitution](https://www.dcode.fr/monoalphabetic-substitution), copy the message in `message.txt` on the textbox, the next is copy the alphabet on the `Knowing the substitution alphabet` textbox, and click on the `Decrypt` button:
		![[Screenshot 2026-04-26 193053.png]]
	3. Flag: `picoCTF{5UB5717U710N_3V0LU710N_59533A2E}`.

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
	