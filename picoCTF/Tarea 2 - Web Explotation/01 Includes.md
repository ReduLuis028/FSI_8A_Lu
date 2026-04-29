**Reto**
	
**Descripción**
	Can you get the flag?Go to this [website](http://saturn.picoctf.net:50069/) and see what you can discover.

**Solución**
	1. Inspeccionano el [website](http://saturn.picoctf.net:50069/) y a su vez interactano con el hay una pista, un script que genera un saludo (`greetings()`), del cual se induce a verificar los diferentes archivos del sitio par encontrar la bandera:

		1.1. http://saturn.picoctf.net:50069/style.css
			body {
			  background-color: lightblue;
			}
			
			/*  picoCTF{1nclu51v17y_1of2_  */
		
		1.2. http://saturn.picoctf.net:50069/script.js
			function greetings()
			{
			  alert("This code is in a separate file!");
			}
			
			//  f7w_2of2_df589022}
		
		1.3. Bandera: picoCTF{1nclu51v17y_1of2_f7w_2of2_df589022}

**Notes**
	
**Referencias**
	