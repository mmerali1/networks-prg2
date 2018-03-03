# TCP Client Y
#Mehdi Merali

import socket, sys

def main():
    # define and init variables
    serverName = 'localhost'
    serverPort = 12000
    message = "Client Y: Bob"
    waitForResponse = True

    # Create TCP socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to socket or raise exception if cannot connect
    try:
        clientSocket.connect((serverName, serverPort))
    except:
        print("Not able to connect")
        sys.exit()
    # send message to server or raise exception if unable to
    try:
        clientSocket.sendall(message.encode())
        # wait for ack from server
        while (waitForResponse):
            # recieve message from server here
            modMessage, serverAddr = clientSocket.recvfrom(1024)
            # if ack recieved, print and set flag to break loop
            if modMessage:
                print(modMessage.decode())
                waitForResponse = False
    # exception handling if cannot send message
    except OSError as err:
        print(err)

    # close socket
    clientSocket.close()


if __name__ == "__main__":
    main()

