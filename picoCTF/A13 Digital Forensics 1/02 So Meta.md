**Challenge**
	
**Description
	Find the flag in this [picture](https://challenge-files.picoctf.net/c_fickle_tempest/fea53d4b5a95f9e78fc25c77dd5332d9ef4aa71d2e64ea96bbe171e0300741b2/pico_img.png).

**Windows PowerShell solution**
	1. Se descargó el archivo **pico_img.png** y se sospechó que la bandera podía estar escondida dentro de los datos binarios o metadatos de la imagen.
	2. Para buscar directamente el formato típico de bandera de picoCTF, se utilizó **PowerShell** con el comando `Select-String`.
	3. Resultados:
		PS C:\Users\luise\Downloads> `Select-String -Path pico_img.png -Pattern "picoCTF{.*}"`
		pico_img.png:4:IHDRX1�tEXtSoftwareAdobe ImageReadyq�e<"iTXtXML:com.adobe.xmp<?xpacket
		begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?> <x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.3-c011
		66.145661, 2012/02/06-14:56:27        "> <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
		<rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/" xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
		xmlns:stRef="http://ns.adobe.com/xap/1.0/sType/ResourceRef#" xmp:CreatorTool="Adobe Photoshop CS6 (Windows)"
		xmpMM:InstanceID="xmp.iid:A5566E73B2B811E8BC7F9A4303DF1F9B"
		xmpMM:DocumentID="xmp.did:A5566E74B2B811E8BC7F9A4303DF1F9B"> <xmpMM:DerivedFrom
		stRef:instanceID="xmp.iid:A5566E71B2B811E8BC7F9A4303DF1F9B"
		stRef:documentID="xmp.did:A5566E72B2B811E8BC7F9A4303DF1F9B"/> </rdf:Description> </rdf:RDF> </x:xmpmeta> <?xpacket
		end="r"?>��C� tEXtArtist`picoCTF{s0_m3ta_bc056477}`~�~�CIDATx��]X�ֽ�4�7�
		*v�bｽg�-��Yc�h�I,�`��+���
		                         �@��{ｈQ���q~*^�[����o�{��){�יs��z���
		&L�0i�҄5&L�0i�Ҕ5&"�7o޾���o���o��?����5iҤ)_���\����k7&L2a"�RPPPTT�ϗ�����}��ݻw8�~������/���_�^��
		�5`���
		      ����
		          �������ᨠ�@�uMMMUUU����)�EVV�&
		                                      �0��`YY�YY�������qqq|H�@8@␦�      W𫼼<��{��8V�]��8
		PS C:\Users\luise\Downloads>

**Notes for Windows**
	1. Comando `Select-String`
		Es un comando de PowerShell que busca texto o patrones dentro de archivos.
		Funciona de manera similar a `grep` en Linux.
		Puede buscar texto simple o expresiones regulares dentro de archivos.
	2. Parámetro `-Path`
		Es un parámetro que indica la ruta o el archivo donde se realizará la búsqueda.
		En este caso se usa pico_img.png, lo que significa que PowerShell buscará dentro de ese archivo.
		Ejemplo: `-Path pico_img.png`
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
	5. Por qué funciona en una imagen
		Aunque pico_img.png es una imagen, los archivos PNG pueden contener:
		metadatos
		bloques de texto (tEXt)
		información de edición

**References**
	