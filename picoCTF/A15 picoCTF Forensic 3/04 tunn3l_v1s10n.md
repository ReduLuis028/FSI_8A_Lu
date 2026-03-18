**Challenge**
	
**Description**
	We found this file. Recover the flag.[tunn3l_v1s10n](https://challenge-files.picoctf.net/c_wily_courier/626df9feed926c1e1280804f5d87fde5576e266ff250a819a5528b0471b0f3f7/tunn3l_v1s10n)
	**Hints**
		1. Weird that it won't display right...

**Solution**
	1. Utilizar un editor hexadecimal, ya sea el integro con el SO o una app como HxD, para cambiar los bytes de la cabecera:
		Los bytes que se muestran en la ventana izquierda son los originas del archivo, y los de la derecha son los ya modificados, 
			42 4D 		→ firma de tipo de archivo `.bmp` 
			8E 26 2C 00	→ tamaño archivo  
			00 00 		→ reservado  
			00 00 		→ reservado  
			36 00 00 00 → offset (inicio de imagen)  
			28 00 00 00 → tamaño header DIB
		![[Screenshot 2026-03-18 154326.png]]
	2. Después se modificaron los bytes del campo `height = altura` para poder ver mas alla de lo permitido previamente y saber si se encuentra la bandera en la imagen, ya que no se encuentra en texto plano para recuperarla con `strings` o `Select-String`.
		![[Screenshot 2026-03-18 154830.png]]
	3. Bandera: `picoCTF{qu1t3_a_V13W_2020}`.

**Notes**
	Revisar los bytes según el formato del archivo.

**References**
	[Wikipedia.](https://es.wikipedia.org/wiki/Windows_bitmap)