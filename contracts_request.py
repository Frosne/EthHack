import urllib3
import ssl


def WriteToFile (name, line):
	f =  open(name, 'w')
	f.write(line)
	f.close();

def request(address, toSave):
	http = urllib3.PoolManager()
	context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
	r = http.request('GET',address)
	WriteToFile(toSave, str(r.data))


address = 'https://etherchain.org/api/account/0xbF35fAA9C265bAf50C9CFF8c389C363B05753275/source'
request(address, '/home/anilam/temp/temp2')


