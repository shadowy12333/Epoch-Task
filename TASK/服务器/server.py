import socket
server=socket.socket()#准备

server.bind(("127.0.0.1",5002))#绑定本机

server.listen()#听用户需求

print("服务器已启动，；连接中")
while True:#开始一直执行
    connection,address=server.accept()
    print(f"有人连接了，地址:{address}")

    message="hello,whats your name?"
    connection.sendall(message.encode(encoding="utf-8"))


    data=connection.recv(1024)
    print(f"收到消息{data.decode(encoding="utf-8")}")

    message="welcome to our server"
    connection.sendall(message.encode("utf-8"))
    response=connection.recv(1024)
    connection.close()

    # connection,address=server.accept()
    # print("client",address)
    # data=connection.recv(1024)
    #
    # connection.sendall(b"client recieved"+data)
    # connection.close()