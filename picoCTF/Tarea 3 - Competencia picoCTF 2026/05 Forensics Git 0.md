**Challenge**
	Forensics

**Description**
	Can you find the flag in this disk image? Download the disk image [here](https://challenge-files.picoctf.net/c_plain_mesa/96db2eea3d6d3e215d3dc2289457a1bc10b17b1de69c46996a171f4f689db74b/disk.img.gz).
	**Hints**
		1. How can you extract the directory from the disk image?

**Solution**
	1. Instalar [Autopsy](https://www.autopsy.com/download/)
	2. Después pensar un poco sobre el hint dado por el reto.
		¿Cómo puedes extraer el directorio de la imagen disco?
	3. Lo cual se responde creando un caso en la App.
	4. Dirigirse en la interfaz virtual hacía:
		Data Sources
		├── disk.img_1 Host
			├── disk.img
				├── vol1
				├── vol2
				├── vol3
				└── vol4 ← ==Ir al este volumen==
					├── folder1
					├── folder2
					├── home ← ==Ir a esta carpeta==
						└── ctf-player
							└── Code
								└── secrets ← ==Aquí se encuentra un nota de sugerencia de formato==
									└── .git ← ==Por el nombre del reto se infiere que se encuentra en la carpeta .git==
										├── branches
										├── hooks
										├── info
										├── objects
											├── 18
											├── 32 ==Y finalmente en esta carpeta se encuentra la bandera==
											├── 46
											├── info
											└── pack
										└── refs
					├── folder3
					└── folderN
	5. Presionar *Keyword Serach* para hacer la búsqueda a partir de esa carpeta y sus hijos, usar la palabra clave común de las banderas: *picoCTF* y *flag*.
		Para mayor comprensión:
		![[Archivos 05 FG 0/Screenshot 2026-03-13 235735.png]]
		![[Archivos 05 FG 0/Screenshot 2026-03-13 235637.png]]
	6. Bandera: `picoCTF{g17_1n_7h3_d15k_041217d8}`

**Notes**
	- La bandera está separada en dos partes:
		1a parte: En una nota (*note.txt The picoCTF flag format is 'picoCTF{}' where there is some leetspeak phrase in between the curly braces*) en la carpeta `secrets`, la cual sugiere usar el formato `picoCTF{}`.
	- Posteriormente en carpetas inferiores se encuentra la bandera con otra sugerencia 
		2a parte: En otro archivo (*Wrap this phrase in the flag format: g17_1n_7h3_d15k_041217d8*) haciendo énfasis en la previa, la cual es envolver la frase encontrada en el formato `g17_1n_7h3_d15k_041217d8`.

**References**
	