**Reto**
	
**Descripción**
	Do you know how to use the web inspector? Start searching [here](http://titan.picoctf.net:65339/) to find the flag

**Solución**
	1. Una vez en el sitio, inspeccionar y tratar de deducir en que parte del sitio puede estar, como indica el nombre del reto, WebDecode, decodificar, eso quiere decir que la bandera podría estar codificada, por lo tanto
		1.1. [About](http://titan.picoctf.net:65339/about.html) en esta parte de la página se encuentra `cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMDdiOTFjNzl9`
			<html lang="en"><head>
			  <meta charset="utf-8">
			  <meta content="IE=edge" http-equiv="X-UA-Compatible">
			  <meta content="width=device-width, initial-scale=1.0" name="viewport">
			  <link href="style.css" rel="stylesheet">
			  <link href="img/favicon.png" rel="shortcut icon" type="image/x-icon">
			  <!-- font (google) -->
			  <link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&amp;display=swap" rel="stylesheet">
			  <title>
			   About me
			  </title>
			 <link rel="stylesheet" href="chrome-extension://507c8b95-1205-4056-a9c1-a9a42bef4768/app/content-style.css"></head>
			 <body>
			  <header>
			   <nav>
			    <div class="logo-container">
			     <a href="index.html">
			      <img alt="logo" src="img/binding_dark.gif">
			     </a>
			    </div>
			    <div class="navigation-container">
			     <ul>
			      <li>
			       <a href="index.html">
			        Home
			       </a>
			      </li>
			      <li>
			       <a href="about.html">
			        About
			       </a>
			      </li>
			      <li>
			       <a href="contact.html">
			        Contact
			       </a>
			      </li>
			     </ul>
			    </div>
			   </nav>
			  </header>
			  <section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMDdiOTFjNzl9">
			   <h1>
			    Try inspecting the page!! You might find it there
			   </h1>
			   <!-- .about-container -->
			  </section>
			  <!-- .about -->
			  <section class="why">
			   <footer>
			    <div class="bottombar">
			     Copyright © 2023 Your_Name. All rights reserved.
			    </div>
			   </footer>
			  </section>
			</body></html>
		1.2. Depues realizar una decodificación base64, donde se obtendrá la bandera
			┌──(kali㉿kali)-[~]
			└─$ echo "cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMDdiOTFjNzl9" | base64 -d
			picoCTF{web_succ3ssfully_d3c0ded_07b91c79}    

**Notes**
	
**Referencias**
	