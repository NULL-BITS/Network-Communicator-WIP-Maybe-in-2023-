import socket

HOST = "127.0.0.1"
PORT = 65432

def IP():
    ip = socket.gethostbyname("localhost")
    print("Your IP is: " + ip)
    listener()

def listener():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as xsocket:
        xsocket.bind((HOST, PORT))
        xsocket.listen()
        conn, addr = xsocket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                print(data.decode());
                if not data:
                    break
                conn.sendall(data)
IP()