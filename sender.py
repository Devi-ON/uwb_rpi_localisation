import socket

ADDR = ""   # represents INADDR_ANY
# ADDR = "192.168.1.37"
PORT = 50000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((ADDR, PORT))


while True:
    data = input("enter the message: ")
    sock.sendto(data.encode(), ("piTag1", PORT))
    print("message sent")
    
sock.close()