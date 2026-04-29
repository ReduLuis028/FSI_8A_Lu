**Challenge**
	
**Description
	This is a really weird text file. Can you find the flag?Get the flag from [TXT](https://challenge-files.picoctf.net/c_fickle_tempest/31fe772e6a4c71e867af0b2a93818e06d8f8ebf8af2a9615495d00356ff576da/flag.txt).

**Solution**
	1. Una vez con el archivo `flag.txt` en posesión, al intentar abrirlo en cualquier editor de texto, podemos darnos cuenta de los *magic bytes*, los cuales nos indican que tipo de formato debería ser realmente, o con el que se creo originalmente, si y solo si no fueron alterados.
		PS C:\Users\luise\Downloads> Format-Hex flag.txt
		           Ruta: C:\Users\luise\Downloads\flag.txt
		           00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
		00000000   ==89 50 4E== 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52  ==PNG==........IHDR
	2. Una vez indentificados los magic bytes, cambiamos el formato por el que debe ser:
				PS C:\Users\luise\Downloads> Format-Hex flag.png
		           Ruta: C:\Users\luise\Downloads\flag.png
		           00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
		00000000   ==89 50 4E== 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52  ==PNG==........IHDR
	3. Previo hecho el punto anterior, cambiamos la extensión (`.txt → .png`), cuando no devuelva nada al CLI, significa que fue exitoso el comando:
		PS C:\Users\luise\Downloads> `Rename-Item flag.txt flag.png`
		PS C:\Users\luise\Downloads>
	4. Y abrimos el archivo en su formato de origen, así obteniendo la bandera:
		`picoCTF{now_you_know_about_extensions}`

**Notes**
	1. Comando `Format-Hex source.txt`:
		Lee el archivo byte por byte.
		Muestra el contenido en hexadecimal y también una vista en texto.
	2. Comando `Rename-Item source.txt target.png`:
		Cambia el **nombre o extensión** de un archivo.

**References**
	