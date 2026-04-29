**Challenge**
	
**Description**
	Now you DON’T see me.This [report](https://artifacts.picoctf.net/c/84/Financial_Report_for_ABC_Labs.pdf) has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?
	**Hints**
		1. How can you be sure of the redaction?

**Solution**
	1. Descargar el archivo.
	2. Instalar la siguiente herramientas:
		- `sudo apt update`
		- `sudo apt install poppler-utils`
	3. Usar el comando `pdftotext` *archivo.pdf* `- | grep picoCTF\{\.*\}`
		<script>
			┌──(kali㉿kali)-[~]
			└─$ pdftotext Financial_Report_for_ABC_Labs.pdf - | grep picoCTF\{\.*\}
			picoCTF{C4n_Y0u_S33_m3_fully}
		</script>
	4. Bandera: `picoCTF{C4n_Y0u_S33_m3_fully}`.

**Notes**
	

**References**
	