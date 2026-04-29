**Reto**
	
**Descripción**
	The factory is hiding things from all of its users.Can you login as Joe and find what they've been looking at? http://fickle-tempest.picoctf.net:54902

**Solución**
	1. Se accede al sitio utilizando el navegador Chrome.
	2. Se abre el panel de desarrollador (F12).
	3. En la pestaña Application → Cookies se inspeccionan las cookies almacenadas.
	4. Se identifica que el sitio confía en valores del lado del cliente como username o admin.
	5. Se modifica manualmente la cookie (False → True) para simular acceso como Joe.
	6. Se recarga la página después de guardar los cambios.
		<html lang="en"><head>
		    <title>Factory Login</title>
		    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">
		    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
		    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
		    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
		<link rel="stylesheet" href="chrome-extension://ihcjicgdanjaechkgeegckofjjedodee/app/content-style.css"></head>
		<body>
		    <div class="container">
		        <div class="header">
		            <nav>
		                <ul class="nav nav-pills pull-right">
		                    <li role="presentation" class="active"><a href="/">Home</a>
		                    </li>
		                    <li role="presentation"><a href="/logout" class="btn btn-link pull-right">Sign Out</a>
		                    </li>
		                </ul>
		            </nav>
		            <h3 class="text-muted">Factory Login</h3>
		        </div>
		        <div class="jumbotron">
		            <p class="lead"></p>
		            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{th3_c0nsp1r4cy_l1v3s_4d184b0d}</code></p>
		        </div>
		        <footer class="footer">
		            <p>© PicoCTF 2019</p>
		        </footer>
		    </div>
		</body></html>
	7. El sitio revela la flag: picoCTF{th3_c0nsp1r4cy_l1v3s_4d184b0d}

**Notes**
	El servidor confía en datos almacenados en cookies.  
	No existe validación adecuada del lado del servidor.  
	Técnica utilizada: Manipulación de cookies (Client-Side Trust Exploitation).

**Referencias**
	