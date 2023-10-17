from xmlrpc.client import ServerProxy
from xmlrpc.client import Binary
import sys
import os

proxy = ServerProxy('http://10.0.2.2:3000')

thisdir = os.path.dirname(os.path.realpath(__file__))
mode = sys.argv[1]
filename = sys.argv[2]

if mode == "send":
	filepath = thisdir + '/' + filename
	if not os.path.exists(filepath):
		print('There is no such a thing called {}'.format(filename))
		sys.exit(1)
	
	with open(filepath, "rb") as handle:
		data_in_binary = Binary(handle.read())
		proxy.file_to_server(data_in_binary, filename)
		handle.close()
	
elif mode == "get":
	data_binary = proxy.client_get_file(filename)
	filepath = thisdir + '/' + filename
	
	if data_binary == False:
		print('There is no such a thing called {} in the server'.format(filename))
		sys.exit(1)
		
	with open(filepath, "wb") as handle:
		handle.write(data_binary.data)
		handle.close()
