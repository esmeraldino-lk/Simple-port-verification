import socket

port = 1
url = #PUT URL HERE

while port < 65635:

	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.settimeout(0.5)
	code = client.connect_ex((url, port))
	if code == 0:
		print(port, " OPEN")
	port+=1
