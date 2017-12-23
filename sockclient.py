import socket

if __name__ == '__main__':

	addr = '127.0.0.1'
	port = 8002

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	sock.connect((addr, port))

	data = sock.recv(1024)

	print data

	sock.send('I am a client')

	print sock.recv(1000)

	sock.send('exit')