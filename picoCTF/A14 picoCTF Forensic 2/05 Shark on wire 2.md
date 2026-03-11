**Challenge**
	
**Description
	We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/d2051a169bcab758191e43355c6954ae40a96b0791d75ad33737c7e9ca42703b/capture.pcap). Recover the flag.

**Wireshark Solution**
	1. Abrir la captura de paquetes en Wireshark.
	2. Analyse > Follow > UDP Stream
		Avanzar cada secuencia de paquetes hasta encontrar en alguna de ellas el inicio (`start`) de los paquetes de la bandera.
	3. Una vez encontrado el inicio, verificar la dirección fuente (`source`) desde la que se enviaron, y a partir de ahí buscar todas las direcciones que coincidan con la dirección IP de inicio 10.0.0.66 `ip.addr == 10.0.0.66`.
	4. En los resultados filtrados, la columna **Info** en Wireshark muestra números como `5000`, `5112`, `5105`, etc.  Cada uno de estos valores contiene un **código ASCII oculto**. 
		4.1. **Eliminar el primer dígito (5)** de cada número.
		4.2. El número restante corresponde a un **código ASCII en formato decimal**.
		4.3. Convertir ese código ASCII a su **carácter equivalente**.
			Info
			5000 → 000 → (carácter nulo, normalmente se ignora)
			5112 → 112 → p
			5105 → 105 → i
			5099 → 099 → c
			5111 → 111 → o
			5067 → 067 → C
			5084 → 084 → T
			5070 → 070 → F
			5123 → 123 → {
			5112 → 112 → p
			5049 → 049 → 1
			5076 → 076 → L
			5076 → 076 → L
			5102 → 102 → f
			5051 → 051 → 3
			5114 → 114 → r
			5051 → 051 → 3
			5100 → 100 → d
			5095 → 095 → _
			5100 → 100 → d
			5097 → 097 → a
			5116 → 116 → t
			5097 → 097 → a
			5095 → 095 → _
			5118 → 118 → v
			5049 → 049 → 1
			5097 → 097 → a
			5095 → 095 → _
			5115 → 115 → s
			5116 → 116 → t
			5051 → 051 → 3
			5103 → 103 → g
			5048 → 048 → 0
			5125 → 125 → }
	5. Resultado: `picoCTF{p1LLf3r3d_data_v1a_st3g0}`

**Notes**
	

**References**
	