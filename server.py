# File contains Python server what recieves and services requests
import socket

#create address-tuple with all interfaces, port 2000 (port 80 requires admin 'sudo' permission)
host = ""
port = 2001
addr = (host, port)

#create socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #bind
    s.bind((host, port))
    s.listen()
    print(f'Server script commenced and listening on {host}:{port}')

    #Wait for connection to be accepted
    conn, addr = s.accept()

    with conn:
        print(f'Server accepted connection from {addr}')
        while True:
            #Perpetually recieve data from client
            #argument specifies max # of bytes to recieve at once
            data = conn.recv(1024)

            #Message handling switch
            #Current client behaviour requires server send reply for every message
            match data:
                #Empty bytes object indicates client has disconnected
                case b"":
                    print(f'Client {addr} has disconnected. Terminating...')
                    #Break exits loop; does not affect match
                    break
                #Inappropriate message handling
                case b"bleh":
                    #Inform server client will be disconnected
                    print(f'Woah, the client {addr} just said a no-no word; time to disconnect them.')
                    conn.send(b'You have violated our Terms of Service. Consider yourself #blocked...')
                    conn.close()
                    break
                #Default cause; send message recieved
                case _:
                    #Send message recieved
                    conn.send(b'0')
                    print(f'Data recieved:\n{data}')