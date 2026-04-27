**Challenge**
	
**Description**
	This service provides you an encrypted flag. Can you decrypt it with just N & e?
	`$ nc verbal-sleep.picoctf.net 64112`
	The program's source code can be downloaded [here](https://challenge-files.picoctf.net/c_verbal_sleep/c798cbe85b3e431345406f393827b9b905481b5fcd6d4b4a845527ee0602da9b/encrypt.py).
	**Hints**
		1. How much do we trust randomness?
		2. Notice anything interesting about N?
		3. Try comparing N across multiple requests.

**Solution**
	1. Connect to the service multiple times: `ncat verbal-sleep.picoctf.net 64112`
	2. Collect several pairs of:
	    - `N`
	    - `ciphertext`
	3. Observe that different executions sometimes generate moduli that share a common factor.  
	    This indicates poor randomness in prime generation.
	4. Compute the **Greatest Common Divisor** between different values of NNN:
	    - `If gcd⁡(N1,N2)≠1`, then a prime factor is shared.
	5. Once a shared prime ppp is found:
		<script class = "Python">
			p = gcd(N1, N2)  
			q = N1 // p
		</script>
	6. Compute:
		<script class = "Python">
			phi = (p-1)*(q-1)  
			d = inverse(65537, phi)
		</script>
	7. Decrypt the ciphertext:
		<script class = "Python">
			m = pow(c, d, N)
		</script>
	8. Convert to readable text:
		<script class = "Python">
			long_to_bytes(m)
		</script>
	9. Once done, automate and obtain the flag with the following code [[solveN1...Nn.py]]:
		<script class = "CMD">
			[+] Collecting data...
			[+] Got N: 18526038028110889135709875823098855909062958568351202952985971524592283518938977930202872425160972379088789979071225808625784546204637789261481458796992138
			[+] Got N: 26152377829710668037462724089993185713973181976152995884413816032824031038972147807955342496362530583031420514636972720751099677874963342330027373820505018
			[+] Got N: 13902220965374502357771459735834348630775151542363166750076458855703844210942783031807083882315481858576812983311540995463982829173089601072075235638193166
			[+] Got N: 23031718438690770388707426365077017461754156215498660173427567004491289695800443994749491155464390820225903963227001141611620624602243041011069364060467522
			[+] Got N: 16453312704232910487136244914926734830180003695228690076056270053336517978863354125079510585006360510565776832110366202372097188832315442211684089137626698
			[+] Got N: 24431043841154711607651340249052825246836280969739484821991814719286616051746604459251390499018734554319249292987941276285673934621544140781021306088215498
			[+] Got N: 22505482925703094002221421345989576722178750218056776706670917818960064225500758987911233435229081921820547882594682774524042436720561853614481738443299962
			[+] Got N: 18750937093192346926420604538772113252670419980804252638130083354321375922983752085027400641109020980101454026651203284011447141087335202000660551621193054
			[+] Searching for shared primes...
			[+] Found shared prime!
			[+] FLAG: picoCTF{tw0_1$_pr!m341c6ed35}
		</script>
	10. Flag: `picoCTF{tw0_1$_pr!m341c6ed35}`.

**Notes**
	

**References**
	