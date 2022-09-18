from socket import *
# Using IP of my machine for testing.
# IP = '10.161.78.120'
serverName = input(
    'Enter the Host Name or IP Address of the server you wish to connect to: ')
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(2048)
print('From Server:', modifiedSentence.decode())
clientSocket.close()
