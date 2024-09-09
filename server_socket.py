"""
Engenharia de computação
Antonio Ambrosio
Daniel Reis
Euler Gomes
"""

import socket
import threading
import os
import sys


class HTTPServer:
    def __init__(self, host, port, document_root):
        self.host = host
        self.port = port
        self.document_root = os.path.abspath(document_root)

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen()
            print(f"Servidor ouvindo em http://{self.host}:{self.port}")

            while True:
                client_socket, client_address = server_socket.accept()
                print(f"Conexão recebida de {client_address}")
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()

    def handle_client(self, client_socket):
        try:
            request = client_socket.recv(1024).decode()
            print("Requisição recebida:")
            print(request)

            file_path = self.get_requested_file_path(request)
            if file_path:
                self.send_response(client_socket, file_path)
            else:
                self.send_404_response(client_socket)
        finally:
            client_socket.close()

    def get_requested_file_path(self, request):
        lines = request.split('\r\n')
        if lines:
            request_line = lines[0]
            method, path, _ = request_line.split()
            if method == 'GET':
                if path == '/':
                    path = '/index.html'

                safe_path = os.path.normpath(path).lstrip('/')
                file_path = os.path.join(self.document_root, safe_path)

                print(f"Resolvendo o arquivo: {file_path}")

                if os.path.isfile(file_path) and os.path.commonpath(
                        [self.document_root, file_path]) == self.document_root:
                    return file_path
        return None

    def send_response(self, client_socket, file_path):
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
            response_header = 'HTTP/1.1 200 OK\r\n'
            response_header += f'Content-Length: {len(content)}\r\n'
            response_header += 'Content-Type: text/html\r\n'
            response_header += '\r\n'
            client_socket.sendall(response_header.encode() + content)
        except Exception as e:
            print(f"Erro ao enviar resposta: {e}")

    def send_404_response(self, client_socket):
        response_body = '<h1>404 Not Found</h1>'
        response_header = 'HTTP/1.1 404 Not Found\r\n'
        response_header += f'Content-Length: {len(response_body)}\r\n'
        response_header += 'Content-Type: text/html\r\n'
        response_header += '\r\n'
        client_socket.sendall(response_header.encode() + response_body.encode())


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    document_root = '.'

    server = HTTPServer(host, port, document_root)
    server.start()
