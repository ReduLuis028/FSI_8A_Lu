**Reto**
	
**Descripción**
	We have several pages hidden. Can you find the one with the flag? The website is running [here](http://saturn.picoctf.net:63921/).

**Solución**
	1. La solución consiste en inspeccionar el sitio y verificar carpetas superiores donde se encuentras los archivos css (cada código html corresponde al sitio superior encontrado, es decir el ultimo link de cada punto)
		1.1. En esta pagina en la sección [About](http://saturn.picoctf.net:63921/about.html) un comentario indica "!css" como si fuera importante, y lo es
			<html><head>
			    <title>About</title>
			    <!-- css -->
			    <link href="secret/assets/index.css" rel="stylesheet">
			  <link rel="stylesheet" href="chrome-extension://507c8b95-1205-4056-a9c1-a9a42bef4768/app/content-style.css"></head>
			  <!-- ***** Header Area Start ***** -->
			  <body><div class="topnav">
			    <a href="index.html">Home</a>
			    <a class="active" href="about.html">About</a>
			    <a href="contact.html">Contact</a>
			  </div>
			    <div class="above">
			      <img src="https://informaticcoolstuff.files.wordpress.com/2016/06/muscle.gif?w=1443&amp;h=1443&amp;crop=1" alt="muscle building gif">
			    </div>
			    <div class="below">
			      <h1>We are here to learn and exercise the cybersecurity muscle!!!</h1>
			    </div>
			</body></html>
		1.2. Después de inspeccionar al pagina previa, vamos a [index.css](http://saturn.picoctf.net:63921/secret/assets/index.css) y posteriormente a http://saturn.picoctf.net:63921/secret/
			<html><head>
			    <title></title>
			    <link rel="stylesheet" href="hidden/file.css">
			  <link rel="stylesheet" href="chrome-extension://507c8b95-1205-4056-a9c1-a9a42bef4768/app/content-style.css"></head>
			  <body>
			    <h1>Finally. You almost found me. you are doing well</h1>
			    <img src="https://media1.tenor.com/images/0a6aff9f825af62c05adfbd75039cc7b/tenor.gif?itemid=4648337" alt="Something Like That GIF - Andy Parksandrecreation Wtf GIFs" style="max-width: 833px; background-color: rgb(151, 121, 85);" width="833" height="937.125">
			</body></html>
		1.3. Mantenemos la dinámica [file.css](http://saturn.picoctf.net:63921/secret/hidden/file.css) pagina que nos dirige a http://saturn.picoctf.net:63921/secret/hidden/
			<html><head>
			    <title>LOGIN</title>
			    <!-- css -->
			    <link href="superhidden/login.css" rel="stylesheet">
			  <link rel="stylesheet" href="chrome-extension://507c8b95-1205-4056-a9c1-a9a42bef4768/app/content-style.css"></head>
			  <body>
			    <form>
			      <div class="container">
			          <div class="row">
			            <h2 style="text-align: center">
			              Login with Social Media or Manually
			            </h2>
			            <div class="vl">
			              <span class="vl-innertext">or</span>
			            </div>
			            <div class="col">
			              <a href="#" class="fb btn">
			                <i class="fa fa-facebook fa-fw"></i> Login with Facebook
			              </a>
			              <a href="#" class="twitter btn">
			                <i class="fa fa-twitter fa-fw"></i> Login with Twitter
			              </a>
			              <a href="#" class="google btn">
			                <i class="fa fa-google fa-fw"></i> Login with Google+
			              </a>
			            </div>
			            <div class="col">
			              <div class="hide-md-lg">
			                <p>Or sign in manually:</p>
			              </div>
			              <input type="text" name="username" placeholder="Username" required="">
			              <input type="password" name="password" placeholder="Password" required="">
			              <input type="hidden" name="db" value="superhidden/xdfgwd.html">
			              <input type="submit" value="Login" onclick="alert('Thank you for the attempt but oops! try harder. better luck next time')">
			            </div>
			          </div>
			      </div></form>
			      <div class="bottom-container">
			        <div class="row">
			          <div class="col">
			            <a href="#" style="color: white" class="btn">Sign up</a>
			          </div>
			          <div class="col">
			            <a href="#" style="color: white" class="btn">Forgot password?</a>
			          </div>
			        </div>
			      </div>
			</body></html>
		1.4. Y al final tenemos [login.css](http://saturn.picoctf.net:63921/secret/hidden/superhidden/login.css) que en http://saturn.picoctf.net:63921/secret/hidden/superhidden/ esta la bandera
			<html><head>
			    <title></title>
			    <link rel="stylesheet" href="mycss.css">
			  <link rel="stylesheet" href="chrome-extension://507c8b95-1205-4056-a9c1-a9a42bef4768/app/content-style.css"></head>
			  <body>
			    <h1>Finally. You found me. But can you see me</h1>
			    <h3 class="flag">picoCTF{succ3ss_@h3n1c@10n_39849bcf}</h3>
			</body></html>

**Notes**
	
**Referencias**
	