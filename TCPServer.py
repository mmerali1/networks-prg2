#TCP Server
#Mehdi Merali

import socket, sys

def main():
    # constants     
    PORT = 12000
    ADDRESS = 'localhost'

    # create and set up server socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # bind socket to addr and port
    serverSocket.bind((ADDRESS, PORT))
    serverSocket.listen(10)

    print("Server is ready to recieve messages")
    
    # lists that hold connection, address, and messages recieved from client
    sock_list = []
    sock_list_addr = []
    message_list = []

    # Flag for if ack sent to client
    msgSent = False
    while (True):
        print("Waiting for connection", file=sys.stderr)
        # Waiting for clients to connect to it
        connectedSocket, addr = serverSocket.accept()
        print("connected with: " + str(addr[0]) + ':' + str(addr[1]), file=sys.stderr)
        # appends connection and addr to respective listts
        sock_list_addr.append(addr)
        sock_list.append(connectedSocket)
        # recieve message from socket
        message = connectedSocket.recv(1024)
        # puts message on message list
        message_list.append(message.decode())
        # after 2 messages recieved, check which sent first
        if len(message_list) == 2:
            # checks which client connected first through parsing their message
            if (message_list[0].find('X') == 7):
                newMsg = "X: Alice recieved before Y:Bob"
            elif(message_list[0].find('Y') == 7):
                newMsg = "Y: Bob recieved before X: Alice"
            # prints out messages recieved by clients and sends ack
            for i in range(0,2):
                print(message_list[i])
                sock_list[i].sendto(newMsg.encode(), sock_list_addr[i])
            print("Sent acknowledgment to both X and Y")
            # sets ack flag to break loop
            msgSent = True
        # break loop
        if msgSent: break          
    connectedSocket.close()
    serverSocket.close()



if __name__ == "__main__":
    main()

