import socket
client=socket.create_connection(("127.0.0.1",5000))

message="hello server"
client.sendall(message.encode("utf-8"))

response=client.recv(1024)
print(response.decode("utf-8"))#收到消息
client.close()