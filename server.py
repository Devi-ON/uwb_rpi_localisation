import socket

BIND_ADDR = ""   # represents INADDR_ANY
BIND_PORT = 50000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)
sock.bind((BIND_ADDR, BIND_PORT))

while True:

	data = ""
	
	try:
		data, recvaddr = sock.recvfrom(128)
		
	except socket.timeout:
		print("timeout occured, no data read on socket")

	print(data)

sock.close()
