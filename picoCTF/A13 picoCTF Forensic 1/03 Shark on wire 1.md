**Challenge**
	
**Description
	We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/134d2a2cf6ec5b7e757effc9b32977af7cc324b8e99a5ddb64737794a14dc18d/capture.pcap). Recover the flag.

**Wireshark Solution**
	1. Abrir la captura de paquetes en Wireshark.
	2. Analyse > Follow > UDP Stream
		Avanzar cada *secuencia* de paquetes hasta encontrar en alguna de los paquetes la bandera.
	3. Una vez encontrada la bandera, la cual fue en la secuencia 6.
	4. Resultado: `picoCTF{StaT31355_636f6e6e}`

**Notes**
	1. ¿Qué es el número de secuencia en Wireshark?
		El número de secuencia sin procesar es **el valor real asignado al paquete** . WireShark agrupa las sesiones TCP y les asigna números de secuencia relativos (y de acuse de recibo) que empiezan desde 0 (y se incrementan en 1, según parece, para cada paquete subsiguiente) para que el usuario pueda identificar la secuencia de eventos.
	2. Aunque en UDP:
		**UDP no usa números de secuencia**, pero Wireshark permite agrupar paquetes relacionados en **UDP Streams** para analizar conversaciones entre hosts

**References**
	