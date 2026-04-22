**Challenge**
	
**Description**
	What do the [flags](https://challenge-files.picoctf.net/c_fickle_tempest/214c9d918be75903d4183c35fa4b94ef60dba05fc4df37c97cf0868087067372/flag.png) mean?
	**Hints**
		1. The flag is in the format PICOCTF{}

**Solution**
	1. Open the image `flag.png`.
	2. Identify the symbols shown in the image as nautical signal flags, which correspond to letters in the  
	3. International maritime signal flags system.
	4. Convert each flag into its corresponding letter using `International maritime signal flags`.
	5. Combine the letters to form the hidden message.
	6. Wrap the result in the required format:
	7. All these steps were performed using the Gemini AI:
		![[Files 05/Descifrando Banderas Marítimas CIS - Google Gemini - [gemini.google.com].png]]
	8. Prompt used:
		<script>
			Actúa como un experto en criptografía y señales marítimas. Analiza la imagen adjunta que contiene banderas del Código Internacional de Señales (CIS).
			Instrucciones estrictas:
				Identifica cada bandera individualmente, de izquierda a derecha, incluyendo las que están fuera y dentro de las llaves { }.
				Traduce cada bandera a su letra o número correspondiente según el estándar náutico internacional.
				Ten especial cuidado con los números: identifica correctamente la bandera del número 1 (círculo rojo) y el número 5 (franjas amarillas y azules horizontales).
				El formato final debe ser PICOCTF{CONTENIDO}.
				Verifica que el contenido interno sea F1AG5AND5TUFF.
				Entrega directamente la flag final.
				Y entrega el desgloce de como lo realizas.
		</script>
	9. Another way is to use [Navy Signals Code](https://www.dcode.fr/maritime-signals-code)
	10. Flag: `PICOCTF{F1AG5AND5TUFF}`.

**Notes**
	

**References**
	