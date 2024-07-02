import socket
import time
import threading
import os
import sys

timeNow = ""

def find_available_port(hostName, port):
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if sock.connect_ex((hostName, port)) != 0:
            return port
        else:
            port += 1
            sock.close()
HOST = '127.0.0.1'
PORT = 8080
PORT = find_available_port(HOST, PORT)

## set the http header and log the head to file
def getHeader(statusCode, fileType, lastModTime):
    status_codes = {
        200: 'HTTP/1.1 200 OK',
        404: 'HTTP/1.1 404 File Not Found',
        400: 'HTTP/1.1 400 Bad Request',
        304: 'HTTP/1.1 304 Not Modified'
    }
    header = status_codes.get(statusCode, '')
    timeNow = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())

    header += '\nDate: {}\n'.format(timeNow)
    header += 'Connection: keep-alive\n'
    header += 'Keep-Alive: timeout=10, max=100\n'
    header += 'Last-Modified: {}\n'.format(lastModTime)

    content_types = {
        'html': 'text/html',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png'
    }
    header += 'Content-Type: {}\n\n'.format(content_types.get(fileType, fileType))

    # Store the header into the log file
    logHeaderStr = '[' + ']['.join(header.split('\n')[:-2]) + ']'
    with open((os.getcwd() + "/log.txt"), "a") as logFile:
        logFile.write(logHeaderStr + '\n')

    return header

def lastModDate(filename):
    s = os.path.getmtime(filename)
    return time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(s))


def handle_200(fileType, lastModTime):

    responseHeader = getHeader(200, fileType, lastModTime)
    return responseHeader


def handle_304(fileType, lastModTime):

    responseHeader = getHeader(304, fileType, lastModTime)
    return responseHeader


def handle_404(fileType, lastModTime):

    responseHeader = getHeader(404, fileType, lastModTime)
    return responseHeader


def handle_400(fileType, lastModTime):
    responseHeader = getHeader(400, fileType, lastModTime)
    return responseHeader


status_handlers = {
    200: handle_200,
    304: handle_304,
    404: handle_404,
    400: handle_400
}
def webServer(Socket, address):
    perConnection = False
    while True:
        try:
            msg = Socket.recv(4096).decode()
            if not msg:
                print("No msg received, closing connection...")
                Socket.close()
                break

            lines = msg.splitlines()
            if 'If-Modified-Since:' in msg:
                request = ''.join(lines)
                modifTimeFromCache = request.split(' ')[-2].split('\r')[0]
                print("If-Modified-Since: " + modifTimeFromCache)
                print("Received message: " + msg)
            requestMethod = lines[0].split(' ')[0]
            print("Method: " + requestMethod)

            if not perConnection:
                perConnection = True
                Socket.settimeout(10)

            if requestMethod == "GET" or requestMethod == "HEAD":
                fileRequested = lines[0].split(' ')[1]
                if fileRequested == "/":
                    fileRequested = "/index.html"

                fileType = fileRequested.split('.')[-1]
                print("Request: " + fileRequested + "\n")

                filePath = "./web" + fileRequested
                
                responseData = b""
                fileLastModTime = None  
                try:
                    fileLastModTime = lastModDate(filePath)
                    file = open(filePath, 'r' if fileType == 'html' else 'rb')
                    responseData = file.read()
                    file.close()
                    statusCode = 200
                except FileNotFoundError:
                    print("404 File Not Found")
                    statusCode = 404
                except Exception as e:
                    print("400 Bad Request")
                    statusCode = 400

                handler = status_handlers.get(statusCode)
                if handler:
                    responseHeader = handler(fileType, fileLastModTime)

                    print("Header: \n" + responseHeader)
                    Socket.send(responseHeader.encode())
                    if requestMethod == "GET" and statusCode != 304:
                        if fileType == 'html':
                            Socket.send(responseData.encode())
                        else:
                            Socket.send(responseData)
                else:
                    # handing the unkown code
                    # ...
                    break
            else:
                print("Closing client socket...")
                Socket.close()
                break
        except socket.timeout:
            print("Timeout, closing socket...")
            Socket.close()
            break
## Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

## Point the IP to the port, and release the website address
try:
   s.bind(('127.0.0.1', PORT))
   print("socket will be binded:", PORT)
   print("It will be Running on the: -> http://127.0.0.1:" + str(PORT))
except Exception as e:
   print("Error: could not bind to port: " + PORT)
   
   s.close()
   sys.exit(1)

s.listen(5)

while True:
   Socket, address = s.accept()
   print('Got connection from ',address,'\n')
   threading.Thread(target=webServer, args=(Socket, address)).start()


   