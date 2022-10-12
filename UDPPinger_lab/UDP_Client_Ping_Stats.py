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
        # Client send/recieve to/from server
        clientSocket.sendto(
            message.encode(), (UDP_pinger_server_name, UDP_pinger_server_port))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        # Calculate RTT for the message
        ending_time = time.time()
        elapsed_time = round(((ending_time - initial_time) * 1000), 2)
    
    # If the connection times out, tell the user
    except TimeoutError:
        print("Ping {} Request timed out.".format(i + 1))
    # Other wise print out the new message
    else:
        print("Ping {} {} RTT: {}ms".format(
            i + 1, modifiedMessage.decode(), elapsed_time))

    i = i + 1

clientSocket.close()