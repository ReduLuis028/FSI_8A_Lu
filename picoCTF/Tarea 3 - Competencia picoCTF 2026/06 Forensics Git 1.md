**Challenge**
	Forensics

**Description**
	Can you find the flag in this disk image? Download the disk image [here](https://challenge-files.picoctf.net/c_plain_mesa/4538dd1f2e93e907c17f0b663c0e1fae2d7054a72b4ee36977f20cfbf3b0a01c/disk.img.gz).
	**Hints**
		1. How can you checkout the files of a previous commit?

**Solution**
	1. Instalar [Autopsy](https://www.autopsy.com/download/)
	2. Después pensar un poco sobre el hint dado por el reto.
		¿Cómo puedes revisar archivos de un commit previo?
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
								└── secrets
									└── .git ← ==Por el nombre del reto se infiere que se encuentra en la carpeta .git, extraerla con la App==
										├── branches
										├── hooks
										├── info
										├── objects
										└── refs
					├── folder3
					└── folderN
		File Views
		├── File Types
			├── By Extension
			└── By MIME Type
		└── Deleted Files
		    ├── File System ()
			└── All (3)
	5. Presionar *Keyword Serach* para hacer la búsqueda a partir de esa carpeta y sus hijos, usar la palabra clave común de las banderas: *picoCTF* y *flag*.
		Para mayor comprensión:
		![[Archivos 06 FG 1/Screenshot 2026-03-14 140029.png]]
		![[Archivos 06 FG 1/Screenshot 2026-03-14 140109.png]]
		Como muestra en la imagen previa, se encuentra `177789af0b300e043ea8f54ea57d6cee352291ae 5fb8194539c770a830b8ba089a50778c07072b03 ctf-player <ctf-player@example.com> 1763544005 +0000	commit: Remove flag`, donde pasa de un hash al otro y hay una leyenda que dice `Remove flag`.
			Donde se encontró el hash del commit inicial: `177789af0b300e043ea8f54ea57d6cee352291ae.
			Y el hash del commit que borro la bandera: `5fb8194539c770a830b8ba089a50778c07072b03`.
	6. Una vez con la carpeta `.git` exportada en `Forensics Git 1\Export\.git`.
		Hay que abrir la terminal donde se encuentre la carpeta `.git`.
	7. CLI (Git Bash)
		<script class="git">
			luise@CANGURO028 MINGW64 ~/OneDrive/Dokumente/Forensics Git 1 Autopsy/Forensics Git 1/Export ((177789a...))
			$ git log --oneline
			177789a (HEAD) Add flag
			
			luise@CANGURO028 MINGW64 ~/OneDrive/Dokumente/Forensics Git 1 Autopsy/Forensics Git 1/Export ((177789a...))
			$ git checkout 177789af0b300e043ea8f54ea57d6cee352291ae
			HEAD is now at 177789a Add flag
			
			luise@CANGURO028 MINGW64 ~/OneDrive/Dokumente/Forensics Git 1 Autopsy/Forensics Git 1/Export ((177789a...))
			$ ls -la
			total 9
			drwxr-xr-x 1 luise 197609  0 Mar 14 13:51 ./
			drwxr-xr-x 1 luise 197609  0 Mar 14 13:51 ../
			drwxr-xr-x 1 luise 197609  0 Mar 14 13:52 .git/
			-rw-r--r-- 1 luise 197609 31 Mar 14 13:51 flag.txt
			
			luise@CANGURO028 MINGW64 ~/OneDrive/Dokumente/Forensics Git 1 Autopsy/Forensics Git 1/Export ((177789a...))
			$ cat flag.txt
			picoCTF{g17_r3m3mb3r5_d4ddf904}
			luise@CANGURO028 MINGW64 ~/OneDrive/Dokumente/Forensics Git 1 Autopsy/Forensics Git 1/Export ((177789a...))
			$
		</script>
	8. Bandera (la bandera se gurda al mismo nivel de la carpeta `.git`, una vez ejecutado el comando `checkout`): `picoCTF{g17_1n_7h3_d15k_041217d8}`

**Notes**
	Proceso:
		- **Explorar:** `git log --oneline` Encuentra el hash del commit objetivo.
		- **Recuperar:** `git checkout <hash>` Restaura los archivos a tu carpeta actual.
		- **Verificar:** `git ls -la` Confirma que el archivo con la bandera existe ahí.
		- **Leer:** `cat <nombre_archivo>` Extrae la información final.
	Función de los comandos:
		- **Listar el historial del repositorio**: 
			`git log --oneline` Sirve para visualizar los commits y obtener el hash del punto en el tiempo deseado.
		- **Mover el puntero al commit específico**:
			`git checkout <hash>` Al ejecutar `git checkout 177789af0b300e043ea8f54ea57d6cee352291ae`, el sistema restaura los archivos al estado en que se encontraban en ese commit.
		- **Listar los archivos restaurados**:
			`ls -la` Permite identificar los nombres de los archivos presentes en el commit actual.
		- **Leer el contenido del archivo**:
			`cat flag.txt` Comando para imprimir en pantalla el contenido del archivo recuperado.

**References**
	