**Challenge**
	
**Description**
	We found this [file](https://challenge-files.picoctf.net/c_fickle_tempest/87bdc8ce30b177d033b3d68bca4647950bb07304032861baa912ebe08701d355/mystery). Recover the flag.

**Solution**
	1. Descargar el archivo [mystery](https://challenge-files.picoctf.net/c_fickle_tempest/87bdc8ce30b177d033b3d68bca4647950bb07304032861baa912ebe08701d355/mystery), y verificar su hexbyte (representación hexadecimal de los bytes).
		Se leen los bytes del header del archivo y en la quinta parte hexadecimal(`00000050`) desde el byte 07 al 0A, se puede notar que tambien hay bytes corruptos.
		Formato del archivo corrupto [mystery](https://challenge-files.picoctf.net/c_fickle_tempest/87bdc8ce30b177d033b3d68bca4647950bb07304032861baa912ebe08701d355/mystery):
		    PS C:\Users\luise\Downloads> Format-Hex .\mystery
		               Ruta: C:\Users\luise\Downloads\mystery
		               00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
		    ==00000000   89 65 4E 34 0D 0A B0 AA 00 00 00 0D 43 22 44 52  eN4..°ª....C"DR==
		    00000010   00 00 06 6A 00 00 04 47 08 02 00 00 00 7C 8B AB  ...j...G.....|«
		    00000020   78 00 00 00 01 73 52 47 42 00 AE CE 1C E9 00 00  x....sRGB.®Î.é..
		    00000030   00 04 67 41 4D 41 00 00 B1 8F 0B FC 61 05 00 00  ..gAMA..±.üa...
		    00000040   00 09 70 48 59 73 AA 00 16 25 00 00 16 25 01 49  ..pHYsª..%...%.I
		    00000050   52 24 F0 AA AA FF A5 ==AB 44 45 54== 78 5E EC BD 3F  R$ðªª.¥==«DET==x^ì½?
		    00000060   8E 64 CD 71 BD 2D 8B 20 20 80 90 41 83 02 08 D0  dÍq½-  A..Ð
		    00000070   F9 ED 40 A0 F3 6E 40 7B 90 23 8F 1E D7 20 8B 3E  ùí@ ón@{#.× >
		    00000080   B7 C1 0D 70 03 74 B5 03 AE 41 6B F8 BE A8 FB DC  ·Á.p.tµ.®Akø¾¨ûÜ
		    00000090   3E 7D 2A 22 33 6F DE 5B 55 DD 3D 3D F9 20 91 88  >}* "3oÞ[UÝ= =ù
		    000000A0   38 71 22 32 EB 4F 57 CF 14 E6 25 FF E5 FF 5B 2C  8q"2ëOWÏ.æ%.å.[,
	2. Ahora verificar un archivo parecido, que tenga un formato parecido, el cual es un .PNG.
		Se leen los **primeros 16 bytes** del header del archivo, también en la quinta parte hexadecimal(`00000050`) desde el byte `07` al `0A`, para notar como deberían ser bytes corrompidos.
		Formato hexabyte de un PNG no corrupto:
		    PS C:\Users\luise\Downloads> Format-Hex .\image.png
		               Ruta: C:\Users\luise\Downloads\image.png
		               00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
		    ==00000000   89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52  PNG........IHDR==
		    00000010   00 00 03 C2 00 00 03 0B 08 06 00 00 00 85 0C 2E  ...Â...........
		    00000020   D1 00 00 00 01 73 52 47 42 00 AE CE 1C E9 00 00  Ñ....sRGB.®Î.é..
		    00000030   00 04 67 41 4D 41 00 00 B1 8F 0B FC 61 05 00 00  ..gAMA..±.üa...
		    00000040   00 09 70 48 59 73 00 00 0E C3 00 00 0E C3 01 C7  ..pHYs...Ã...Ã.Ç
		    00000050   6F A8 64 00 00 FF A5 ==49 44 41 54== 78 5E 4C FD 4B  o¨d...¥==IDAT==x^LýK
		    00000060   93 E4 C8 B2 AD 89 7D AA 6A 66 80 7B 44 66 D5 DE  äÈ²­}ªjf{DfÕÞ
		    00000070   B7 9B 77 D4 D2 03 0A A7 FC 8D FC AB DD 24 85 22  ·wÔÒ..§üü«Ý$"
		    00000080   E4 3D FB EC AA CC 70 07 60 A6 AA 1C 28 32 CF 1D  ä=ûìªÌp.`¦ª.(2Ï.
		    00000090   F8 A8 1E 11 E1 00 0C BA 96 AE 87 FC 5F FF 6F FF  ø¨..á..º®ü_.o.
		    000000A0   F7 FC 53 16 FF 94 C9 9F BA 38 F7 C6 B1 1B E7 A3  ÷üS..Éº8÷Æ±.ç£
	3. Pasar a corregir el hexabyte del archivo, ya sea con algún editor visual ([HxD](https://mh-nexus.de/en/downloads.php?product=HxD20)) o por CLI (Windows Powershell):
		<script>
		    # Leer el archivo completo
		    $bytes = [System.IO.File]::ReadAllBytes("mystery")
		
		    # Cabecera PNG (primeros 16 bytes)
		    $pngHeader = 0x89,0x50,0x4E,0x47,0x0D,0x0A,0x1A,0x0A,0x00,0x00,0x00,0x0D,0x49,0x48,0x44,0x52
		    for ($i=0; $i -lt 16; $i++) { $bytes[$i] = $pngHeader[$i] }
		
		    # Offset donde empieza « D E T (ajusta según tu archivo)
		    $offset = 0x57
		
		    # Bytes nuevos: I D A T
		    $newBytes = 0x49,0x44,0x41,0x54
		
		    # Reemplazar solo esos 4 bytes, dejando el siguiente byte (X) intacto
		    for ($i=0; $i -lt $newBytes.Length; $i++) { $bytes[$offset + $i] = $newBytes[$i] }
		
		    # Guardar archivo corregido
		    [System.IO.File]::WriteAllBytes("mystery_fixed.png", $bytes)
		</script>
	4. Resultado de los comandos (Corrección en Powershell) o ya sea con el editor visual (posterior a ello cambiar la extensión en el explorador de archivos):
		Se reemplazan los **primeros 16 bytes** por los de un header PNG válido.
		Se reemplazan los **4 bytes del bloque `«DET`** por **`IDAT`**, dejando intacto el siguiente byte `x`.
		Se guarda el archivo como `mystery_fixed.png`.
		Formato hexabyte arreglado:
			PS C:\Users\luise\Downloads> Format-Hex .\mystery_fixed.pn
			           Ruta: C:\Users\luise\Downloads\mystery_fixed.png
			           00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0
			==00000000   89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52  PNG........IHDR==
			00000010   00 00 06 6A 00 00 04 47 08 02 00 00 00 7C 8B AB  ...j...G.....|«
			00000020   78 00 00 00 01 73 52 47 42 00 AE CE 1C E9 00 00  x....sRGB.®Î.é..
			00000030   00 04 67 41 4D 41 00 00 B1 8F 0B FC 61 05 00 00  ..gAMA..±.üa...
			00000040   00 09 70 48 59 73 AA 00 16 25 00 00 16 25 01 49  ..pHYsª..%...%.I
			00000050   52 24 F0 AA AA FF A5 ==49 44 41 54== 78 5E EC BD 3F  R$ðªª.¥==IDAT==x^ì½?
			00000060   8E 64 CD 71 BD 2D 8B 20 20 80 90 41 83 02 08 D0  dÍq½-  A..Ð
			00000070   F9 ED 40 A0 F3 6E 40 7B 90 23 8F 1E D7 20 8B 3E  ùí@ ón@{#.× >
			00000080   B7 C1 0D 70 03 74 B5 03 AE 41 6B F8 BE A8 FB DC  ·Á.p.tµ.®Akø¾¨ûÜ
			00000090   3E 7D 2A 22 33 6F DE 5B 55 DD 3D 3D F9 20 91 88  >}* "3oÞ[UÝ= =ù
			000000A0   38 71 22 32 EB 4F 57 CF 14 E6 25 FF E5 FF 5B 2C  8q"2ëOWÏ.æ%.å.[,
	5. Bandera: `picoCTF{c0rrupt10n_1847995}`

**Notes**
	Lo importante fue identificar bytes corruptos (`«DET`) y corregirlos según un PNG estándar.
	La manipulación de bytes se hace **directamente sobre el array de bytes**; así se puede reparar archivos binarios sin depender del formato original.

**References**
	