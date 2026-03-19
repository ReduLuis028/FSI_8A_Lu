**Challenge**
	General Skills

**Description**
	Can you reverse a series of Linux text transformations to recover the original flag?
	Start searching for the flag here `nc foggy-cliff.picoctf.net 57600`
	**Hints**
		1. For text translation and character replacement, see [`tr` command documentation](https://man7.org/linux/man-pages/man1/tr.1.html).

**Solution**
	1. Usando terminal de picoCTF:
		<script class = "CLI picoCTF">
			Lui5-picoctf@webshell:~$ nc foggy-cliff.picoctf.net 57600
			
			===Welcome to the Text Transformations Challenge!===
			
			  
			
			Your goal: step by step, recover the original flag.
			
			At each step, you'll see the transformed flag and a hint.
			
			Enter the correct Linux command to reverse the last transformation.
			
			  
			
			--- Step 1 ---
			
			Current flag: KTY4ODhyMjFuLWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShTR1BicHZj
			
			Hint: Base64 encoded the string.
			
			Enter the Linux command to reverse it: base64 -d
			
			Correct!
			
			  
			
			--- Step 2 ---
			
			Current flag: )6888r21n-fa01g@ze0sfa4eG-gk3g-ta1ferirE(SGPbpvc
			
			Hint: Reversed the text.
			
			Enter the Linux command to reverse it: rev
			
			Correct!
			
			  
			
			--- Step 3 ---
			
			Current flag: cvpbPGS(Eriref1at-g3kg-Ge4afs0ez@g10af-n12r8886)
			
			Hint: Replaced underscores with dashes.
			
			Enter the Linux command to reverse it: tr '-' '_'
			
			Correct!
			
			  
			
			--- Step 4 ---
			
			Current flag: cvpbPGS(Eriref1at_g3kg_Ge4afs0ez@g10af_n12r8886)
			
			Hint: Replaced curly braces with parentheses.
			
			Enter the Linux command to reverse it: tr '()' '{}'
			
			Correct!
			
			  
			
			--- Step 5 ---
			
			Current flag: cvpbPGS{Eriref1at_g3kg_Ge4afs0ez@g10af_n12r8886}
			
			Hint: Applied ROT13 to letters.
			
			Enter the Linux command to reverse it: tr 'A-Za-z' 'N-ZA-Mn-za-m'
			
			Correct!
			
			  
			
			Congratulations! You've recovered the original flag:
			
			>>> picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_a12e8886}
		</script>
	2. Bandera: `picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_a12e8886}`.
**Notes**
	- Este reto consiste en **revertir transformaciones de texto** paso a paso para recuperar la flag.
	- Se trabaja directamente en la terminal de picoCTF usando `nc` para conectarse al servidor:
	    `nc foggy-cliff.picoctf.net 57600`
	- Cada paso del reto aplica una transformación distinta. Para revertirlas, se utilizan principalmente **comandos Linux básicos**:
	1. **Decodificar Base64**:
	    - Transformación: el texto original se codificó en Base64.
	    - Comando para revertir: `base64 -d`.
	2. **Revertir texto invertido**:
	    - Transformación: el texto fue invertido.
	    - Comando: `rev`
	3. **Reemplazar guiones por guiones bajos**:
	    - Transformación: se cambiaron guiones (`-`) por guiones bajos (`_`).
	    - Comando: `tr '-' '_'`
	4. **Reemplazar paréntesis por llaves**:
	    - Transformación: se cambiaron llaves `{}` por paréntesis `()`.
	    - Comando: `tr '()' '{}'`
	5. **Aplicar ROT13**:
	    - Transformación: las letras fueron cifradas con ROT13.
	    - Comando para revertir: `tr 'A-Za-z' 'N-ZA-Mn-za-m'`
	- Al aplicar todos los pasos en orden, se obtiene la **flag final**:
	    `picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_a12e8886}`
	- Este reto es un buen ejemplo de cómo **encadenar transformaciones de texto** y cómo `tr`, `rev` y `base64` pueden usarse para manipular y recuperar información en Linux.

**References**
	