# https://pypi.python.org/pypi/goslate#downloads
import requests
import json
arquivo = open('SentiWordNet/SentiWordNet_3.0.txt', 'r')
texto = arquivo.read()
texto = texto.split('\n')

arquivo_saida = open('saida.txt', 'a')

for linha in texto:
	coluna = linha.split('\t')
	pos = coluna[2]
	neg = coluna[3]
	palavras = coluna[4].split()
	arquivo_saida.write(pos+' '+neg+' ')
	for palavra in palavras:
		palavra = palavra.split('#')
		#Traducao para o potugues
		try:
			r = requests.get("https://www.googleapis.com/language/translate/v2?key=AIzaSyDbQWrzEx3Pr0g6X9sxQ5LA7EfY1Q5mSV8&q="+palavra[0]+"&source=en&target=pt")
			saida_json = json.loads(r.content)
			traducao = saida_json['data']['translations'][0]['translatedText']
		
		except Exception, e:
			traducao = "error"
		print palavra[0],traducao
		
		arquivo_saida.write('['+traducao.encode('utf-8')+'] ')
	arquivo_saida.write('\n')




