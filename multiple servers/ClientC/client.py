import hydra
import socket, sys, threading

from time import sleep


class recv_data :
	

	def __init__(self,host,port,file_name,output_file=None):
		self.mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.mysocket.connect((host, port))
		self.mysocket.send(file_name.encode('utf-8'))
		data = self.mysocket.recv(1024)

		if data == 'NOT_FOUND':
			print('NOT FOUND')
			exit(0)

		if output_file==None:
			output_file = file_name

		with open(output_file, 'wb') as f:
			print ('file opened')
			while True:
				print('receiving data...')
				data = self.mysocket.recv(1024)
				print(data)
				if not data:
					print('break')
					break
				f.write(data)

@hydra.main()
def app(cfg):
	host = cfg.host
	port = cfg.port
	file_name = cfg.file
	output_file = cfg.outfile

	recv_data(host,port,file_name,output_file)


if __name__ =="__main__":
	app()
