**Challenge**
	General Skills

**Description**
	We intercepted a suspiciously encoded message, but it’s clearly hiding a flag. No encryption, just multiple layers of obfuscation. Can you peel back the layers and reveal the truth?Download the [message](https://challenge-files.picoctf.net/c_plain_mesa/4986bcdd15422ff14839a371ad1807f27508401eab11d33c48acf3b4633cf6ef/message.txt).
	**Hints**
		1. The flag has been wrapped in several layers of common encodings such as ROT13, URL encoding, Hex, and Base64. Can you figure out the order to peel them back?
		2. A tool like CyberChef can be interesting.

**Solution**
	1. Guía de uso de los comandos
		1.1. Base64 to Hex: `[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String((Get-Content message.txt)))`
			==*Result 1.1.*==
		1.2. Hex to Text:
			`$hex="RESULT OF POINT 1.1"`
			`$bytes = for ($i=0; $i -lt $hex.Length; $i+=2){ [Convert]::ToByte($hex.Substring($i,2),16) }`
			`[Text.Encoding]::UTF8.GetString($bytes)`
			==*Result 1.2.*==
		1.3. URL-Decoding:
			`Add-Type -AssemblyName System.Web` ← Comando opcional, ya que puede no estar cargada una librería .NET
			`[System.Web.HttpUtility]::UrlDecode("RESULT OF POINT 1.2")`
			==*Result 1.3.*==
		1.4. ROT13:
			`$text="RESULT OF POINT 1.3"`
			`$rot13 = ($text.ToCharArray() | ForEach-Object {`
			    `if($_ -cmatch '[a-z]'){`
			        `[char]((([byte][char]$_ - 97 + 13) % 26) + 97)`
			    `} elseif($_ -cmatch '[A-Z]'){`
			        `[char]((([byte][char]$_ - 65 + 13) % 26) + 65)`
			    `} else {`
			        `$_`
			    `}`
			`}) -join ""`
			
			`$rot13` ← Result 1.4.
/
	2. Resultados
		PS C:\Users\luise\OneDrive\Dokumente\Archivos 02> `[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String((Get-Content message.txt)))`
		==637670625047532537426172666772715f72617030717661745f36366f3534323537253744== ← *Result 1.1.*
		PS C:\Users\luise\OneDrive\Dokumente\Archivos 02> `$hex="637670625047532537426172666772715f72617030717661745f36366f3534323537253744"`
		PS C:\Users\luise\OneDrive\Dokumente\Archivos 02> `$bytes = for ($i=0; $i -lt $hex.Length; $i+=2){ [Convert]::ToByte($hex.Substring($i,2),16) }`
		PS C:\Users\luise\OneDrive\Dokumente\Archivos 02> `[Text.Encoding]::UTF8.GetString($bytes)`
		==cvpbPGS%7Barfgrq_rap0qvat_66o54257%7D== ← *Result 1.2.*
		PS C:\Users\luise\OneDrive\Dokumente\Archivos 02> `Add-Type -AssemblyName System.Web`
		PS C:\Users\luise\OneDrive\Dokumente\Archivos 02> `[System.Web.HttpUtility]::UrlDecode("cvpbPGS%7Barfgrq_rap0qvat_66o54257%7D")`
		==cvpbPGS{arfgrq_rap0qvat_66o54257}== ← *Result 1.3.*
		PS C:\Users\luise\OneDrive\Dokumente\Archivos 02> `$text="cvpbPGS{arfgrq_rap0qvat_66o54257}"`
		PS C:\Users\luise\OneDrive\Dokumente\Archivos 02>
		PS C:\Users\luise\OneDrive\Dokumente\Archivos 02> `$rot13 = ($text.ToCharArray() | ForEach-Object {`
        `>>     if($_ -cmatch '[a-z]'){`
        `>>         [char]((([byte][char]$_ - 97 + 13) % 26) + 97)`
        `>>     } elseif($_ -cmatch '[A-Z]'){`
        `>>         [char]((([byte][char]$_ - 65 + 13) % 26) + 65)`
        `>>     } else {`
        `>>         $_`
        `>>     }`
        `>> }) -join ""`
		PS C:\Users\luise\OneDrive\Dokumente\Archivos 02>
		PS C:\Users\luise\OneDrive\Dokumente\Archivos 02> `$rot13`
		==picoCTF{nested_enc0ding_66b54257}== ← *Result 1.4.*
		PS C:\Users\luise\OneDrive\Dokumente\Archivos 02>
	3. Bandera: `picoCTF{nested_enc0ding_66b54257}`

**Notes**
	

**References**
	