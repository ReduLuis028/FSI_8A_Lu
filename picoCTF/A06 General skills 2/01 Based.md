**Reto**
	
**Descripción**
	To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337?
	Connect with nc fickle-tempest.picoctf.net 50955.
	
**Solución**
	Haciendo conversiones con Conversor.exe hecha en una materia previa (separado por espacios, cada digito), y uso de tabla ASCII (https://elcodigoascii.com.ar/)
		`BINARIO → DECIMAL → ASCII`
		`01101100 = 108 = 'l'`
		`01101001 = 105 = 'i'`
		`01111010 = 122 = 'z'`
		`01100001 = 97  = 'a'`
		`01110010 = 114 = 'r'`
		`01100100 = 100 = 'd'`
		`Resultado: lizard`
		
		OCTAL → DECIMAL → ASCII
		o156 = 110 = 'n'
		o165 = 117 = 'u'
		o162 = 114 = 'r'
		o163 = 115 = 's'
		o145 = 101 = 'e'
		Resultado: nurse
		
		HEXADECIMAL → DECIMAL → ASCII
		6c = 108 = 'l'
		69 = 105 = 'i'
		67 = 103 = 'g'
		68 = 104 = 'h'
		74 = 116 = 't'
		Resultado: light

	Lui5-picoctf@webshell:~$ nc fickle-tempest.picoctf.net 50955
	Let us see how data is stored
	lizard
	Please give the 01101100 01101001 01111010 01100001 01110010 01100100 as a word.
	...
	you have 45 seconds.....
	
	Input:
	lizard
	Please give me the  o156 o165 o162 o163 o145 as a word.
	Input:
	nurse
	Please give me the 6c69676874 as a word.
	Input:
	light
	You've beaten the challenge
	Flag: picoCTF{learning_about_converting_values_6c3Fb625}

**Notes**
	1. Entender distintos tipos de codificación de datos (binario, octal, hexadecimal) es clave para convertirlos a caracteres legibles.
	2. Para convertir binario a ASCII: Convertir de BINARIO → DECIMAL → ASCII usando calculadora en modo programador o tablas ASCII.
	3. Para convertir octal a ASCII: Convertir OCTAL → DECIMAL → ASCII.
	4. Para convertir hexadecimal a ASCII: Convertir HEXADECIMAL → DECIMAL → ASCII.
	5. Esta técnica permite interpretar datos codificados en distintos formatos y comunicarse correctamente con programas que usan esas representaciones.
	6. Herramientas útiles: calculadora en modo programador, tablas ASCII online.

**Referencias**