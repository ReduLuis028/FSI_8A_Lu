**Challenge**
	
**Description**
	Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image.
	[dds1-alpine.flag.img.gz](https://challenge-files.picoctf.net/c_wily_courier/a118330a1c5e12f3b59fc45a75b8838700482f89c8ea71a28aa1bd66c7ba3968/dds1-alpine.flag.img.gz)
	**Hints**
		1. Have you ever used `file` to determine what a file was?
		2. Relevant terminal-fu in picoGym: https://play.picoctf.org/practice/challenge/85
		3. Mastering this terminal-fu would enable you to find the flag in a single command: https://play.picoctf.org/practice/challenge/48
		4. Using your own computer, you could use qemu to boot from this disk!

**Solution**
	1. Una vez descargado y descomprimido el archivo `dds1-alpine.flag.gz`, utilizar comandos de la `Gitbash` más `Powershell` o solo `Powershell`:
		<script class = "Gitbash + Powershell">
			PS C:\Users\luise\Downloads\Archivos 02> strings dds1-alpine.flag.img | Select-String picoCTF
			
			  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_5e56e786}
		</script>
		<script class = "Powershell">
			PS C:\Users\luise\Downloads\Archivos 02> Select-String picoCTF dds1-alpine.flag.img
			
			dds1-alpine.flag.img:366173:  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_5e56e786}
		</script>
	2. Bandera: `picoCTF{f0r3ns1c4t0r_n30phyt3_5e56e786}`.

**Notes**
	1. `strings dds1-alpine.flag.img | Select-String picoCTF`
	    - `strings`: extrae todo el texto legible de un archivo binario.
	    - `Select-String picoCTF`: filtra las líneas que contienen el patrón `picoCTF`.
	    - Permite encontrar la bandera sin montar la imagen de disco.
	2. `Select-String picoCTF dds1-alpine.flag.img`
	    - Alternativa en PowerShell que hace lo mismo: buscar en un archivo binario el texto que contiene `picoCTF`.

**References**
	