import socket

socket_server = socket.socket()

socket_server.bind(("127.0.0.1", 6666))

socket_server.listen(1)

conn, addr = socket_server.accept()

while True:
    data = conn.recv(1024).decode("utf-8")
    if data == 'exit':
        print("收到'exit'退出指令，server关闭服务")
        break
    print("接收发来的数据:", data)

    conn.send("你好呀，哈哈哈,我是你的服务器".encode("utf-8"))

conn.close()
socket_server.close()
