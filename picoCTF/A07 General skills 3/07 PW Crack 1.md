**Reto**
	
**Descripción**
	Can you crack the password to get the flag?
	Download the password checker [here](https://artifacts.picoctf.net/c/11/level1.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/11/level1.flag.txt.enc) in the same directory too.

**Solución**
	1. Usando terminal de Windows CMD y VSCode
		C:\Users\luise\Downloads>certutil -dump '.\07 level1.flag.txt.enc'
		  0000  ...
		  001e
		    0000  41 0c 52 0e 72 31 77 1a  04 51 04 09 6e 17 00 0f   A.R.r1w..Q..n...
		    0010  56 54 5f 06 6e 03 50 52  05 56 01 57 01 18         VT_.n.PR.V.W..
		CertUtil: -dump comando completado correctamente.
		
		Y calculdora de Windows
			0x41 XOR 0x70(p) = 0x31
			0x0C XOR 0x69(i) = 0x65
			0x52 XOR 0x63(c) = 0x31
			0x0E XOR 0x6F(o) = 0x61
			31 65 31 61 = 49.0 101.0 49.0 97.0 = 1 e 1 a (Hexadecimal → Decimal → ASCII)
		
		C:\Users\luise\Downloads>py level1.py
		Please enter correct password for flag: 1e1a
		Welcome back... your flag, user:
		picoCTF{545h_r1ng1ng_fa343060}
		
		C:\Users\luise\Downloads>
\
	2. Usando terminal de Windows PowerShell y VSCode
		PS C:\Users\luise\Downloads> Format-Hex '.\07 level1.flag.txt.enc'


           Ruta: C:\Users\luise\Downloads\07 level1.flag.txt.enc

           00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F

		00000000   41 0C 52 0E 72 31 77 1A 04 51 04 09 6E 17 00 0F  A.R.r1w..Q..n...
		00000010   56 54 5F 06 6E 03 50 52 05 56 01 57 01 18        VT_.n.PR.V.W..
		
		Y calculdora de Windows
			0x41 XOR 0x70(p) = 0x31
			0x0C XOR 0x69(i) = 0x65
			0x52 XOR 0x63(c) = 0x31
			0x0E XOR 0x6F(o) = 0x61
			31 65 31 61 = 49.0 101.0 49.0 97.0 = 1 e 1 a (Hexadecimal → Decimal → ASCII)
		
		PS C:\Users\luise\Downloads> py .\level1.py
		Please enter correct password for flag: 1e1a
		Welcome back... your flag, user:
		picoCTF{545h_r1ng1ng_fa343060}
		PS C:\Users\luise\Downloads>

**Notes**
	1. Archivo cifrado con XOR.
	2. Se asumió inicio 'picoCTF{'.
	3. Se aplicó: clave = cifrado XOR texto conocido.
	4. Se obtuvo la clave: 1e1a.
	5. Se validó ejecutando el script.
	6. Uso de herramientas hex: 
		certutil
			6.1. Muestra el contenido del archivo en formato hexadecimal.
			6.2. Permite ver los bytes reales almacenados.
			6.3. Es útil para analizar archivos binarios o cifrados.
			6.4. Funciona en CMD (Windows).
		Format-Hex
			6.5. Muestra el contenido del archivo en hexadecimal.
			6.6. Presenta dirección, bytes y representación ASCII.
			6.7. Es más visual y ordenado que certutil.
			6.8. Funciona en PowerShell.
				
**Referencias**
	