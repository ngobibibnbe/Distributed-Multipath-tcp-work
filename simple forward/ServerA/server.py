import socket, threading, os
from time import sleep


host, port = '127.0.0.1', 8888


class transfer :
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #socketMPTCP=socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_MPTCP)
    mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def __init__(self,file_name):
        self.mysocket.bind((host, port))
        print(' Server is ready ..')
        self.mysocket.listen(5)
        conn, addr = self.mysocket.accept()

        
        size = os.path.getsize(file_name)
        print(' file size : {}'.format(str(size)))

        send_thread = threading.Thread(target = self.forward_file, args=(file_name, size, conn, addr, ))
        send_thread.start()

    def forward_file(self, file_name, size, conn, addr):
        with open(file_name, 'rb') as f:
            data = f.read(1024)
            conn.send(data)
            while data:
                 conn.send(data)
                 data = f.read(1024)
            conn.close

Transfer = transfer('file.mp4')
