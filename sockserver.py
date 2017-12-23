import socket
import time
import threading

def deal_client(sock, addr):
	print 'A new connection from %s:%s' % addr
	sock.send('I am the server ,who are you')

	# while True:
	data = sock.recv(1024)

	if not data or data == 'exit':
		exit()

	print 'Recv from client: %s' % data
	sock.send(data)


if __name__ == '__main__':
	addr = '127.0.0.1'
	port = 8002

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	sock.bind((addr, port))

	sock.listen(5)

	print 'waiting for connections...'
	while True:
		s, address = sock.accept()

		t = threading.Thread(target=deal_client, args=(s, address))
		t.start()