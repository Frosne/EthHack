import urllib3
import ssl


def WriteToFile (name, line):
	f =  open(name, 'a')
	f.write(line)
	f.close();

def request(address):
	http = urllib3.PoolManager()
	context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
	r = http.request('GET',address)
	return str(r.data)

def parse(address2,toSave):
	pattern = r"<a href=\'/address/"
	text = request(address2)	
	begin = 0
	output = ''
	while (begin != -1) :
		begin = text.find(pattern,begin)
		s = text[begin+ len(pattern) :begin + len(pattern) + 42 ]
		if s[0] == '0':
			output = output +'\n' +s
		if begin != -1:
			begin  = begin +1
	WriteToFile(toSave,output)

def parseAll():
	toSave = '/home/anilam/temp/temp2'
	pattern = 'http://etherscan.io/accounts/c/'
	parse(pattern,toSave)
	for i in range (1,4197):
		print(i)
		patternC = pattern + str(i)
		parse(patternC,toSave)	
	
	

parseAll()

