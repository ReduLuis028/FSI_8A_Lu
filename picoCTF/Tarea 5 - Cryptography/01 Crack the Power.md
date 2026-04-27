**Challenge**
	
**Description**
	We received an encrypted message. The modulus is built from primes large enough that factoring them isn’t an option, at least not today. See if you can make sense of the numbers and reveal the flag.Download the [message](https://challenge-files.picoctf.net/c_amiable_citadel/22b49f8547060bf2b66398688e6e87f94c00953b7ee2ba34acc1270c72ff966e/message.txt).
	**Hints**
		1. When certain values in the encryption setup are smaller than usual, it opens up unexpected shortcuts to recover the plaintext.
		2. Consider whether you can invert the encryption without factoring `n`.
		3. Read more about Coppersmith's_attack [here](https://en.wikipedia.org/wiki/Coppersmith's_attack)

**Solution**
	1. Observe that this is RSA encryption:
	    `c = m^e * mod(n)`
		    - m: mensaje
			- e: exponente
			- n: módulo
			- c: ciphertext
	2. The exponent is small: `e = 20`
	3. If the plaintext mmm is small enough, then: `m^20 < n`
	    This means modular reduction never happens, so: `c = m^20`
	4. Therefore, we can recover mmm by taking the integer 20th root of `c`.
	5. Use Python ([[solveSmallE.py]]) to compute the exact root.
	6. The result converts directly to readable bytes, revealing the flag
		Flag: `picoCTF{t1ny_e_ee65653a}`.

**Notes**
	1. This attack works because:
	    - The exponent is small.
	    - No padding is used.
	    - The plaintext is smaller than `n^(1/e)`.
	2. No need to factor `n`, which would be infeasible.

**References**
	