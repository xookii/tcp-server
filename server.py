import socket

HOST = '0.0.0.0'
PORT = 8010

print(f"Starting TCP server on port {PORT}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            conn.sendall(b"Hello, world!\n")
