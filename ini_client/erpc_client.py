from xmlrpc.client import ServerProxy
from xmlrpc.client import Binary
import sys
import os

proxy = ServerProxy('http://localhost:3000')

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

print('Client is now activated\ntype "help" to check the command list')
while True:
	arg = input('> ')
	argv = arg.split()

	mode = argv[0]
	filename = None
	if len(argv) == 2:
		filename = argv[1]
	
	if mode == 'quit' and len(argv) == 1:
		print('Closing Client...')
		sys.exit(1)
	elif mode == 'help' and len(argv) == 1:
		print("How to use this thing:\n")
		print("-  help")
		print("   ask for help\n")
		print("-  listfiles")
		print("   show list of files in the server\n")
		print("-  get [filename]")
		print("   copy a file from server to this directory\n")
		print("-  send [filename]")
		print("   copy a file from this directory to the server\n")
		print("-  quit")
		print("   to quit\n")
	elif mode == 'listfiles' and len(argv) == 1:
		print(proxy.list_files())
	elif mode == 'get':
		if filename is not None:
			mode_get(filename)
		else :
			print('Missing argument: use "get [filename]"')
	elif mode == 'send':
		if filename is not None:
			mode_send(filename)
		else :
			print('Missing argument: use "send [filename]"')
	else :
		print('Invalid Mode!')