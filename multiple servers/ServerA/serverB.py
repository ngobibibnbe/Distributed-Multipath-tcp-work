import hydra
import socket
import threading
import os
from time import sleep


class Transfer:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def __init__(self, host, port, files_list=None):
        self.mysocket.bind((host, port))
        print(' Server is ready ..')
        self.mysocket.listen(5)

        self.peer = (peer_address, peer_port)
        conn, addr = self.mysocket.accept()

        file_name = conn.recv(2048)

        send_thread = threading.Thread(
            target=self.forward_file, args=(file_name, conn))
        send_thread.start()

    def forward_file(self, file_name, size, conn):
        with open(file_name, 'rb') as f:
            data = f.read(1024)
            conn.send(data)
            while data:
                conn.send(data)
                data = f.read(1024)
        conn.close()


@hydra.main()
def app(cfg):
    print(cfg.pretty())
    host, port = cfg.server.address, cfg.server.port
    files_list = cfg.files_list.split(',')

    Transfer(host, port, files_list)


if __name__ == "__main__":
    app()
