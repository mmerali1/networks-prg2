# TCP Client X
# Mehdi Merali

import socket, sys

def main():
    # define and init variables
    serverName = 'localhost'
    serverPort = 12000
    message = "Client X: Alice"
    waitForResponse = True

    # Create TCP socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to socket or raise exception if cannot connect
    try:
        clientSocket.connect((serverName, serverPort))
    except:
        print("Not able to connect")
        sys.exit()

    # send message to server or raise exception
    try:
        clientSocket.sendall(message.encode())
        # waits for ack
        while (waitForResponse):
            # recieves message from server here
            modMessage, serverAddr = clientSocket.recvfrom(1024)
            # if recieved message, print and set flag to break loop
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

