from socket import *
# Using IP of my machine for testing.
# IP = '10.161.78.120'
serverName = input(
    'Enter the Host Name or IP Address of the server you wish to connect to: ')
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
