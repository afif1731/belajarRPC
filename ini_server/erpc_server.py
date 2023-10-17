from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import Binary
import os

server = SimpleXMLRPCServer(('localhost', 3000), logRequests=True)
	
def file_to_server(thedata, filename):
	dirnow = os.path.dirname(os.path.realpath(__file__))
	this_file_path = dirnow + '/shared/' + filename
	
	with open(this_file_path, "wb") as handle:
		handle.write(thedata.data)
		print('{} is uploaded'.format(filename))
		handle.close()
		return True

def client_get_file(filename):
	dirnow = os.path.dirname(os.path.realpath(__file__))
	filepath = dirnow + '/shared/' + filename
	
	if not os.path.exists(filepath):
		print('{} not found'.format(filename))
		return False
	
	print('{} sended'.format(filename))
	with open(filepath, "rb") as handle:
		data_in = Binary(handle.read())
		return data_in
		handle.close()

server.register_function(file_to_server, 'file_to_server')
server.register_function(client_get_file, 'client_get_file')

if __name__ == '__main__':
	try:
		print('servin...')
		server.serve_forever()
	except KeyboardInterrupt:
		print('Exitin...')
