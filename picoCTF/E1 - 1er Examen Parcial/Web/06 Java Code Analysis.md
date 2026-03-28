**Challenge (Java Code Analysis!?!)**
	
**Description**
	BookShelf Pico, my premium online book-reading service.I believe that my website is super secure. I challenge you to prove me wrong by reading the 'Flag' book!
	Here are the credentials to get you started:
		- Username: "user"
		- Password: "user"
	Source code can be downloaded [here](https://artifacts.picoctf.net/c/480/bookshelf-pico.zip).
	Website can be accessed [here!](http://saturn.picoctf.net:64422/).
	**Hints**
		1. Maybe try to find the JWT Signing Key ("secret key") in the source code? Maybe it's hardcoded somewhere? Or maybe try to crack it?
		2. The 'role' and 'userId' fields in the JWT can be of interest to you!
		3. The 'controllers', 'services' and 'security' java packages in the given source code might need your attention. We've provided a README.md file that contains some documentation.
		4. Upgrade your 'role' with the _new_ (cracked) JWT. And re-login for the new role to get reflected in browser's localStorage.

https://10015.io/tools/jwt-encoder-decoder
\bookshelf-pico\src\main\java\io\github\nandandesai\pico

**Solution**
	1. Download, unzip the source code and open the next files.
		![[Screenshot 2026-03-22 211346.png]]
	2. Go to the site [BookShelf Pico](https://artifacts.picoctf.net/c/480/bookshelf-pico.zip) inspect (F12) and copy the URL bse64 that is in the column `Request Headers` → `Authorization` on one side will be the base64:
		![[Screenshot 2026-03-22 211559.png]]
	3. Now go to `Application` → Storage → Local Storage → Clic on the URL and, you will see the key-value pairs:
		![[Screenshot 2026-03-22 211648.png]]
	4. No use the [100L5 Tools](https://10015.io/tools/jwt-encoder-decoder) to decode and encode the URLs bse64
		- Decode:
			![[Screenshot 2026-03-22 212002.png]]
		- Encode
			![[Screenshot 2026-03-22 212256.png]]
	5. For the last step, follow the steps in point 3 and replace the key-value pairs we made in the previous point:
		![[Screenshot 2026-03-22 212402.png]]
	6. Flag: `picoCTF{w34k_jwt_n0t_g00d_7745dc02}`.

**Notes**
	

**References**
	