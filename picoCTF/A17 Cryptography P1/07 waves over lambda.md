**Challenge**
	
**Description**
	We made a lot of substitutions to encrypt this. Can you decrypt it?
	Connect with nc fickle-tempest.picoctf.net 56147.
	**Hints**
		1. Flag is not in the usual flag format

**Solution**
	1. Connect to the server and obtain the following information::
		<script>
			Lui5-picoctf@webshell:~$ nc fickle-tempest.picoctf.net 56147
			-------------------------------------------------------------------------------
			mhpivqob fsvs tb nhzv waqi - wvsyzspmn_tb_m_hesv_aqljcq_qj75359q
			-------------------------------------------------------------------------------
			fqetpi fqc bhls otls qo ln ctbghbqa ufsp tp ahpchp, t fqc etbtosc ofs jvtotbf lzbszl, qpc lqcs bsqvmf qlhpi ofs jhhxb qpc lqgb tp ofs atjvqvn vsiqvctpi ovqpbnaeqptq; to fqc bovzmx ls ofqo bhls whvsxphuascis hw ofs mhzpovn mhzac fqvcan wqta oh fqes bhls tlghvoqpms tp csqatpi utof q phjaslqp hw ofqo mhzpovn. t wtpc ofqo ofs ctbovtmo fs pqlsc tb tp ofs skovsls sqbo hw ofs mhzpovn, dzbo hp ofs jhvcsvb hw ofvss boqosb, ovqpbnaeqptq, lhacqetq qpc jzxhetpq, tp ofs ltcbo hw ofs mqvgqoftqp lhzpoqtpb; hps hw ofs utacsbo qpc asqbo xphup ghvothpb hw szvhgs. t uqb pho qjas oh atifo hp qpn lqg hv uhvx itetpi ofs skqmo ahmqaton hw ofs mqboas cvqmzaq, qb ofsvs qvs ph lqgb hw oftb mhzpovn qb nso oh mhlgqvs utof hzv hup hvcpqpms bzvesn lqgb; jzo t whzpc ofqo jtbovtor, ofs ghbo ohup pqlsc jn mhzpo cvqmzaq, tb q wqtvan usaa-xphup gaqms. t bfqaa sposv fsvs bhls hw ln phosb, qb ofsn lqn vswvsbf ln lslhvn ufsp t oqax hesv ln ovqesab utof ltpq.
		</script>
	2. Enter the information beforehand on the [Mono-alphabetic Substitution](https://www.dcode.fr/monoalphabetic-substitution) site:
		![[Files 07/01 Monoalpha01 betic Substitution Cipher - Online Cryptogram Decoder, Sol.png]]
	3. Once done, press `DECRYPT AUTOMATICALLY` button:
		![[Files 07/02 Monoalpha01 betic Substitution Cipher - Online Cryptogram Decoder, Sol.png]]
	4. Having done the above, we have the flag: `FREQUENCY_IS_C_OVER_LAMBDA_AB75359A`.

**Notes**
	

**References**
	https://www.dcode.fr/en