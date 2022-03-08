import socket
HOST = ""
PORT = ""  

def address():
    global HOST
    print("What is the IP of the computer you want to connect to? ")
    HOST = input(":")
    global PORT
    print("What is the PORT of the computer you want to connect to? ")
    PORT = int(input(":"))
    connector()

def connector():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"test")
        data = s.recv(1024)
    print(f"Received {data!r}")
    
address()


