import socket

client = socket.socket()
client.connect(("127.0.0.1",6666))

while True:
    data_send = input("请输入你想向服务端发送的数据")
    client.send(data_send.encode("utf-8"))
    if data_send == 'exit':
        print("client关闭客户端")
        break
    data = client.recv(1024).decode("utf-8")
    print(f"Client: 收到来自服务端的数据{data}")

client.close()
