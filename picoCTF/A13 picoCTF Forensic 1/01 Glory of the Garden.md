**Challenge**
	
**Description**
	This file contains more than it seems.Get the flag from [garden.jpg](https://challenge-files.picoctf.net/c_fickle_tempest/19722024edeecca10f263776ab05c8b1235b136dcf25aa6e976d3860513ffcd5/garden.jpg).

**Linux solution**
	1. Se analizó el archivo **garden.jpg** buscando texto oculto dentro de los datos binarios.
	2. Para ello se utilizó el comando `strings`, que permite extraer texto legible desde archivos binarios.
	3. El resultado se filtró usando `grep` para buscar la palabra **pico**, que suele aparecer en las banderas de picoCTF.
		Comando utilizado: `strings garden.jpg | grep -i pico`
	4. Resultados:
		┌──(kali㉿kali)-[~]
		└─$ `strings garden.jpg | grep -i pico`                                     
		Here is a flag: picoCTF{more_than_m33ts_the_3y37fde8891}

**Windows PowerShell solution**
	1. El archivo **garden.jpg** parecía ser solo una imagen, pero el reto indicaba que contenía información oculta. Primero se revisaron los metadatos con **ExifTool**, pero no apareció ninguna pista relevante.
	2. Después se buscó texto dentro del archivo usando **PowerShell**: `Select-String -Path garden.jpg -Pattern "picoCTF{.*}"`
	3. Resultados:
		PS C:\Users\luise\Downloads> `Select-String -Path garden.jpg -Pattern "picoCTF{.*}"`
		garden.jpg:13403:�<�j~k��V�y9���S�� 1�u�������������Ӳ���Here is a flag: picoCTF{more_than_m33ts_the_3y37fde8891}
		PS C:\Users\luise\Downloads>

**Notes for Linux**
	1. Comando strings
		Extrae cadenas de texto legibles desde archivos binarios.
		Es útil para analizar archivos como imágenes, ejecutables o documentos que puedan contener texto oculto.
		Ejemplo: `strings garden.jpg`
	2. Parametro `grep`
		Es una herramienta que busca texto dentro de la salida de otro comando o dentro de archivos.
	3. Parametro `-i`
		Hace que la búsqueda ignore mayúsculas y minúsculas.
		Ejemplo: `grep -i pico`
	4. Parametro pipeline (`|`)
		El símbolo | envía la salida de un comando al siguiente.
		En este caso, el texto extraído por `strings` se pasa a grep para filtrar resultados.

**Notes for Windows**
	1. Comando `Select-String`
		Es un comando de PowerShell que busca texto o patrones dentro de archivos.
		Funciona de manera similar a `grep` en Linux.
		Puede buscar texto simple o expresiones regulares dentro de archivos.
	2. Parámetro `-Path`
		Es un parámetro que indica la ruta o el archivo donde se realizará la búsqueda.
		En este caso se usa pico_img.png, lo que significa que PowerShell buscará dentro de ese archivo.
		Ejemplo: `-Path garden.jpg`
	3. Parámetro `-Pattern`
		Define el texto o patrón que se desea encontrar dentro del archivo.
		Puede ser texto simple o una expresión regular.
		Ejemplo: `-Pattern "picoCTF{.*}"`
	4. Expresión regular usada:	`picoCTF{.*}`
		Significado:
			picoCTF → texto literal del formato de bandera.
			{ → inicio de la bandera.
			.* → cualquier número de caracteres.
			} → final de la bandera.
	5. Aunque **garden.jpg** es una imagen, los archivos binarios pueden contener **texto incrustado dentro de sus datos**, lo que permite encontrar información oculta utilizando herramientas de búsqueda de cadenas.

**References**
	