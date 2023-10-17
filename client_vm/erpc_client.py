from xmlrpc.client import ServerProxy
from xmlrpc.client import Binary
import sys
import os

proxy = ServerProxy('http://10.0.2.2:3000')

thisdir = os.path.dirname(os.path.realpath(__file__))

def mode_send(filename):
	filepath = thisdir + '/' + filename
	if not os.path.exists(filepath):
		print('There is no such a thing called {}'.format(filename))
		return 0
	
	with open(filepath, "rb") as handle:
		data_in_binary = Binary(handle.read())
		proxy.file_to_server(data_in_binary, filename)
		handle.close()
	print('{} sended to the server'.format(filename))
	
def mode_get(filename):
	data_binary = proxy.client_get_file(filename)
	filepath = thisdir + '/' + filename
	
	if data_binary == False:
		print('There is no such a thing called {} in the server'.format(filename))
		return 0
		
	with open(filepath, "wb") as handle:
		handle.write(data_binary.data)
		handle.close()
	print('{} received'.format(filename))

print('Client is now activated')
while True:
	arg = input('> ')
	argv = arg.split()

	mode = argv[0]
	filename = None
	if len(argv) == 2:
		filename = argv[1]
	
	if mode == 'quit':
		print('Closing Client...')
		sys.exit(1)
	elif mode == 'get':
		if filename is not None:
			mode_get(filename)
		else :
			print('Missing argumen: use "get [filename]"')
	elif mode == 'send':
		if filename is not None:
			mode_send(filename)
		else :
			print('Missing argumen: use "send [filename]"')
	else :
		print('Invalid Mode!')