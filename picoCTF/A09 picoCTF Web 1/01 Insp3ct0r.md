**Reto**
	
**Descripción**
	Kishor Balan tipped us off that the following code may need inspection:http://fickle-tempest.picoctf.net:65469

**Solución**
	1. Usando el navegador Chrome
		1a parte: picoCTF{tru3_d3:
			Una vez en la pagina web, se inspeccionan los elementos de la misma, es decir mirando el código HTML, puede darse cuenta de que dejaron credenciales en el mismo.
		2a parte: t3ct1ve_0r_ju5t
			Posteriormente hacemos una inspección mas a fondo de un archivo relacionado, teniendo el mismo resultado, encontrando ms credenciales.
		3a parte: _lucky?302945a7} 
			Finalmente tenemos la inspección en el ultimo archivo relacionado que hace funcionar la pagina.
			
		Resultado: picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?302945a7}
		
**Notes**
	El reto se resolvió mediante inspección manual del código fuente.
	No fue necesario explotar vulnerabilidades, únicamente revisar archivos enlazados.
	Técnica utilizada: **Análisis estático del lado del cliente (HTML, CSS y JS).**

**Referencias**
	