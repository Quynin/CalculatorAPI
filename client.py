#This is a python client
import socket

#create address-tuple with all interfaces, port 2000 (port 80 requires admin 'sudo' permission)
host = ""
port = 2001
addr = (host, port)

#create client socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((host, port))
    print(f'Client script connected to {host}:{port}')
    s.send(b"Hello server!")
    while True:
        s.send(input(">>>").encode())
        serverResponse = s.recv(1024)
        match serverResponse:
            #Message sucessfully recieved--do nothing
            case b"0":
                {}
            #Abnormal message recieved from server
            case _:
                print(f'Server: {serverResponse}')