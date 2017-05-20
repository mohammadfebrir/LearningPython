import urllib2

def nextTarget(page):
	for x in page:
		startlink=page.find('<td height=30 ')
		if startlink == -1:
			return None,0
		startquote=page.find('>',startlink)
		endquote=page.find('<a', startquote+1)
		var2=page[startquote+1:endquote]
		print var2
		return var2, endquote

def getAllProduct(page):
	product = []
	while True:
		url, endpos=nextTarget(page)
		if url:
			product.append(url)
			page= page [endpos:]
		else:
			break
	return product

site=("http://www.enterkomputer.com/processor.php")
ourUrl=urllib2.urlopen(site).read()
getAllProduct(ourUrl)