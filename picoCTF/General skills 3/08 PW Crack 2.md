**Reto**
	
**Descripción**
	Can you crack the password to get the flag?
	Download the password checker [here](https://artifacts.picoctf.net/c/15/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/15/level2.flag.txt.enc) in the same directory too.

**Solución**
	1. Usando terminal de Windows CMD y VSCode
		C:\Users\luise\Downloads>certutil -dump ".\08 level2.flag.txt.enc"
		  0000  ...
		  001f
		    0000  43 50 00 0a 70 6d 25 1e  47 4b 57 50 5b 66 56 54   CP..pm%.GKWP[fVT
		    0010  5d 5e 52 0b 54 66 56 55  01 5c 00 51 01 5c 1e      ]^R.TfVU.\.Q.\.
		CertUtil: -dump comando completado correctamente.
		
		Y calculdora de Windows
			0x43 XOR 0x70(p) = 0x33
			0x50 XOR 0x69(i) = 0x39
			0x00 XOR 0x63(c) = 0x63
			0x0A XOR 0x6F(o) = 0x65
			33 39 63 65 = 3 9 c e
		
		C:\Users\luise\Downloads>py "08 level2.py"
		Please enter correct password for flag: 39ce
		Welcome back... your flag, user:
		picoCTF{tr45h_51ng1ng_502ec42e}
		
		C:\Users\luise\Downloads>
\
	2. Usando terminal de Windows PowerShell y VSCode
		PS C:\Users\luise\Downloads> Format-Hex '.\08 level2.flag.txt.enc'
		
		
		           Ruta: C:\Users\luise\Downloads\08 level2.flag.txt.enc
		
		           00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
		
		00000000   43 50 00 0A 70 6D 25 1E 47 4B 57 50 5B 66 56 54  CP..pm%.GKWP[fVT
		00000010   5D 5E 52 0B 54 66 56 55 01 5C 00 51 01 5C 1E     ]^R.TfVU.\.Q.\.
		
		Y calculdora de Windows
			0x43 XOR 0x70(p) = 0x33
			0x50 XOR 0x69(i) = 0x39
			0x00 XOR 0x63(c) = 0x63
			0x0A XOR 0x6F(o) = 0x65
			33 39 63 65 = 51.0 57.0 99.0 101.0 = 3 9 c e (Hexadecimal → Decimal → ASCII)
		
		PS C:\Users\luise\Downloads> py '.\08 level2.py'
		Please enter correct password for flag: 39ce
		Welcome back... your flag, user:
		picoCTF{tr45h_51ng1ng_502ec42e}
		PS C:\Users\luise\Downloads>

**Notes**
	1. Mismo principio de cifrado XOR.
	2. Se aplicó Known Plaintext Attack.
	3. Se calculó clave: 39ce.
	4. Refuerza análisis criptográfico básico.

**Referencias**
	