**Challenge**
	Forensics

**Description**
	Can you find the flag in this disk image? This time I deleted the file! Let see you get it now!Download the disk image [here](https://challenge-files.picoctf.net/c_plain_mesa/60a0a3c971e29caf69b4cac5323bb848d5227ac961f7add94437d5970be4be69/disko-4.dd.gz).
	**Hints**
		1. How would you look for deleted files?

**Solution**
	1. Instalar [Autopsy](https://www.autopsy.com/download/)
	2. Después pensar un poco sobre el hint dado por el reto.
		¿Cómo buscarías los archivos eliminados?
	3. Lo cual se responde creando un caso en la App.
	4. Dirigirse en la interfaz virtual hacía:
		Data Sources
		File Views ← ==Dirigirse aquí==
		├── File Types
			├── By Extension
			└── By MIME Type
		└── Deleted Files
		    ├── File System ()
			└── All (3)
	5. Presionar *Keyword Serach* para hacer la búsqueda a partir de esa carpeta y sus hijos, usar la palabra clave común de las banderas: *picoCTF*.
		Para mayor comprensión  ![[Screenshot 2026-03-13 214651.png]]
	6. Bandera: `picoCTF{d3l_d0n7_h1d3_w3ll_c2fcb641}`

**Notes**
	

**References**
	