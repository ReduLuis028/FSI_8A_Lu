**Reto**
	
**Descripción**
	Can you get the flag?Go to this [website](http://saturn.picoctf.net:51642/) and see what you can discover.

**Solución**
	1. Una vez en el sitio, inspeccionarlo, y a través de los archivos con los que funciona la pagina ir encontrando credenciales para acceder mas profundamente.
		1.1. http://saturn.picoctf.net:51642/
			<html lang="en"><head>
			    <meta charset="UTF-8">
			    <meta name="viewport" content="width=device-width, initial-scale=1.0">
			    <meta http-equiv="X-UA-Compatible" content="ie=edge">
			    <link rel="stylesheet" href="style.css">
			    <title>Secure Customer Portal</title>
			  </head>
			  <body>
			    <h1>Secure Customer Portal</h1>
			   <p>Only letters and numbers allowed for username and password.</p>
			    <form role="form" action="login.php" method="post">
			      <input type="text" name="username" placeholder="Username" required="" autofocus=""><br>
			      <input type="password" name="password" placeholder="Password" required="">
			      <button type="submit" name="login">Login</button>
			    </form>
			</body></html>
		1.2. http://saturn.picoctf.net:51642/secure.js
			<html><head><meta name="color-scheme" content="light dark"><link rel="stylesheet" href="chrome-extension://5114ecc9-9941-4c91-a2da-02ce908d182a/app/content-style.css"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">
			function checkPassword(username, password)
			{
			  if( username === 'admin' &amp;&amp; password === 'strongPassword098765' )
			  {
			    return true;
			  }
			  else
			  {
			    return false;
			  }
			}
			</pre></body></html>
		1.3. http://saturn.picoctf.net:51642/admin.php
			<html lang="en"><head>
			    <meta charset="UTF-8">
			    <meta name="viewport" content="width=device-width, initial-scale=1.0">
			    <meta http-equiv="X-UA-Compatible" content="ie=edge">
			    <link rel="stylesheet" href="style.css">
			    <title>Secure Customer Portal</title>
			  </head>
			  <body>
			    picoCTF{j5_15_7r4n5p4r3n7_a8788e61}  
			</body></html>

**Notes**
	
**Referencias**
	