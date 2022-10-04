from socket import *

UDP_pinger_server_name = str("127.0.0.1")
UDP_pinger_server_port = 15000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

i = 0
while (i < 10):

    message = input('Input lowercase sentence: ')

    try:
        clientSocket.sendto(
            message.encode(), (UDP_pinger_server_name, UDP_pinger_server_port))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    except TimeoutError:
        print("Ping " + str(i + 1) + " Request timed out." + " RTT: ")
    else:
        print("Ping " + str(i + 1) + " " + modifiedMessage.decode() + " RTT: ")
    i = i + 1

clientSocket.close()
