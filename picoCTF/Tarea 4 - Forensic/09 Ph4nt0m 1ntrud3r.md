**Challenge**
	
**Description**
	A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag.
	To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method.
	The attacker has cleverly concealed his moves in well timely manner.
	Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder!Find the PCAP file here [Network Traffic PCAP file](https://challenge-files.picoctf.net/c_verbal_sleep/45a9df82c8f05fd74b8547d157ae6b1be6ba783a2bad55c6f8c664e4609d88ac/myNetworkTraffic.pcap) and try to get the flag.
	**Hints**
		1. Filter your packets to narrow down your search.
		2. Attacks were done in timely manner.
		3. Time is essential

**Solution**
	1. Ordenando los paquetes por la columna `time`, en el Panel de Bytes del Paquete de Wireshark (Packet Bytes Pane) seleccionamos los paquetes que contengan un base64 en el, los cuales terminan en `==`, y los copiamos como `ASCII text`.
		Imagen:
			![[Archivos 09/Screenshot 2026-03-29 003615.png]]
		Paquete 12:
			E,@vPP i `fQ==`
		Paquete 11:
			E4@nPP L `MzE4ZGIyMg==`
		Paquete 19:
			E4@nPP `YmhfNHJfZg==`
		Paquete 14:
			E4@nPP Z `XzM0c3lfdA==`
		Paquete 20:
			E4@nPP R `bnRfdGg0dA==`
		Paquete 6:
			E4@nPP `[` `ezF0X3c0cw==`
		Paquete 17:
			E4@nPP A `cGljb0NURg==`
		Se tomarán en un orden LIFO, es decir, del paquete 17 al 12.
	2. Ejecutar el siguiente comando Powershell para decodificar el base64 y obtener la bandera:
		<script>
			$strings = @(
				"cGljb0NURg==",
				"ezF0X3c0cw==",
				"bnRfdGg0dA==",
				"XzM0c3lfdA==",
				"YmhfNHJfZg==",
				"MzE4ZGIyMg==",
				"fQ=="
			)

			($strings | ForEach-Object {
				[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($_))
			}) -join ""
		</script>
	3. Ejecución:
		<script>
			PS C:\Users\luise\Downloads> $strings = @(
			>>     "cGljb0NURg==",
			>>     "ezF0X3c0cw==",
			>>     "bnRfdGg0dA==",
			>>     "XzM0c3lfdA==",
			>>     "YmhfNHJfZg==",
			>>     "MzE4ZGIyMg==",
			>>     "fQ=="
			>> )
			PS C:\Users\luise\Downloads>
			PS C:\Users\luise\Downloads> ($strings | ForEach-Object {
			>>     [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($_))
			>> }) -join ""
			picoCTF{1t_w4snt_th4t_34sy_tbh_4r_f318db22}
			PS C:\Users\luise\Downloads>
			PS C:\Users\luise\Downloads>
		</script>
	4. Bandera: `picoCTF{1t_w4snt_th4t_34sy_tbh_4r_f318db22}`.

**Notes**
	

**References**
	