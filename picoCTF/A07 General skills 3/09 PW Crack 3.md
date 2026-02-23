**Reto**
	
**Descripción**
	Can you crack the password to get the flag?
	Download the password checker [here](https://artifacts.picoctf.net/c/16/level3.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/16/level3.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/16/level3.hash.bin) in the same directory too.
	There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

**Solución**
	1. Usando terminal de Windows PowerShell y VSCode
		Windows PowerShell
		Copyright (C) Microsoft Corporation. Todos los derechos reservados.
		
		PS C:\Users\luise\Downloads> Format-Hex '09 level3.flag.txt.enc'
		
		
		           Ruta: C:\Users\luise\Downloads\09 level3.flag.txt.enc
		
		           00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
		
		00000000   48 5F 56 0A 7B 62 73 1E 55 02 00 0D 67 50 59 54  H_V.{bs.U...gPYT
		00000010   56 51 04 0B 5F 69 07 07 08 01 07 04 01 06 48     VQ.._i........H

		Y calculdora de Windows
			0x XOR 0x70(p) = 0x38
			0x XOR 0x69(i) = 0x36
			0x XOR 0x63(c) = 0x35
			0x XOR 0x6F(o) = 0x65
			38 36 35 65 → 56.0 54.0 53.0 101.0 → 8 6 5 e (Hexadecimal → Decimal → ASCII)

		PS C:\Users\luise\Downloads> py '.\09 level3.py'
		Please enter correct password for flag: 865e
		Welcome back... your flag, user:
		picoCTF{m45h_fl1ng1ng_2b072a90}
		PS C:\Users\luise\Downloads>

**Notes**
		

**Referencias**
	