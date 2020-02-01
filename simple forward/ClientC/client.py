import socket, sys, threading

from time import sleep

host, port = '192.168.43.112', 8888


class recv_data :
	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	mysocket.connect((host, port))

	def __init__(self):
		data = self.mysocket.recv(1024)
		f = open('newfile.txt', 'wb')
		print("lom")

		with open('received_file', 'wb') as f:
			print ('file opened')
			while True:
				print('receiving data...')
				data = self.mysocket.recv(1024)
				print(data)
				if not data:
					print('break')
					break
				f.write(data)

re = recv_data()
