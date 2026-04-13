**Challenge**
	
**Description**
	Can you get the real meaning from this file.Download the file [here](https://artifacts.picoctf.net/c_titan/3/enc_flag).
	**Hints**
		1. Engaging in various decoding processes is of utmost importance

**Solution**
	1. Download the file.
	2. Base64 (archivo → texto)
		<script class = "Powershell">
			$data = Get-Content enc_flag
			$data = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($data))
			$data
		</script>
	3. Remove `b' '` y decodificar otra vez
		<script class = "Powershell">
			$data = $data.Replace("b'", "").Replace("'", "")
			$data = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($data))
			$data
		</script>
	4. Execution in CLI::
		<script class = "Powershell">
			PS C:\Users\luise\Downloads> $data = Get-Content enc_flag
			PS C:\Users\luise\Downloads> $data = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($data))
			PS C:\Users\luise\Downloads> $data
			b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2kyMDRoa2o2fQ=='
			
			PS C:\Users\luise\Downloads> $data = $data.Replace("b'", "").Replace("'", "")
			PS C:\Users\luise\Downloads> $data = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($data))
			PS C:\Users\luise\Downloads> $data
			wpjvJAM{jhlzhy_k3jy9wa3k_i204hkj6}
			PS C:\Users\luise\Downloads>
		</script>
	5. Go to the site [Caesar Cipher](https://www.dcode.fr/caesar-cipher) and press the `DECRYPT (BRUTEFORCE)` button:
		![[Files 08/Caesar Cipher (Shift) Translator - Online Decoder, Encoder, Solver.png]]
	6. Flag: `picoCTF{caesar_d3cr9pt3d_b204adc6}`.

**Notes**
	https://www.dcode.fr/en

**References**
	