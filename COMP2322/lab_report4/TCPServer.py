# import the socket library 
import socket 
# create a socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print ("socket successfully created")
# reserve a port=12345 on your computer 
serverPort = 12345 
# bind to the port 
# we have not typed any ip in the ip field, instead we have inputted an empty string. 
# this makes the server listen to requests coming from other computers on the network 
serverSocket.bind(('', serverPort))
print ("socket binded to %s" %(serverPort))
# put the socket into listening mode 
serverSocket.listen(5) 
print ("socket is listening")
password = '00143' 
# a forever loop until we interrupt it or an error occurs 
while True:
# establish connection with client. 
    connectionSocket, addr = serverSocket.accept() 
    print ('got connection from', addr )
    received_password = connectionSocket.recv(1024).decode()
    print("from client:",received_password)
    if (received_password == password):
        connectionSocket.send(b'Your password is correct!')
    else:
        connectionSocket.send(b'Your password is incorrect!') 
# send a message to the client, using encode() to send byte type 
    sentence='thank you for connecting' 
    connectionSocket.send(sentence.encode())
# close the connection with the client
    connectionSocket.close() 
    break