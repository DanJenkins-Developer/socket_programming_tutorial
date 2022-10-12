from socket import *
import time

# Establish server destination
UDP_pinger_server_name = str("127.0.0.1")
UDP_pinger_server_port = 15000

# Create UDP socket
# Setting timeout for one second
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

# 10 pings
for i in range(10):
    message = input('Input lowercase sentence: ')

    try:
        initial_time = time.time()
        clientSocket.sendto(
            message.encode(), (UDP_pinger_server_name, UDP_pinger_server_port))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        ending_time = time.time()
        elapsed_time = str(ending_time - initial_time)
    # If the connection times out, tell the user
    except TimeoutError:
        print("Ping {} Request timed out.".format(i + 1))
    # Other wise print out the new message
    else:
        print("Ping {} {} RTT: {}".format(
            i + 1, modifiedMessage.decode(), elapsed_time))

    i = i + 1

clientSocket.close()

# hello
# hello 2
