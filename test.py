import urllib
def retext():
	quotes=open(r'wordCollection.txt')
	isifile=quotes.read()
	print(isifile)
	quotes.close()
	cekkata(isifile)
def cekkata(checkingtext):
	connection=urllib.urlopen('http://www.purgomalum.com/service/containsprofanity?text='+checkingtext)
	output=connection.read()
	print(output)
	connection.close
	if "true" in output:
		print("kata kotor")
	elif "false" in output:
		print("kata aman")
	else:
		print("kata tidak jelas")
retext()