import socket

HOST = 'localhost'
PORT = 30000


def echo_client():
    ''' Echo Server 的 Client 端 '''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        # 接收用户输入数据并发送服务端
        #data = input('input > ')
        # 发送文件名
        file_name = input("File name:")
        data = file_name.encode("utf-8")

        # 设定退出条件
        if data == 'exit':
            break

        # 发送数据到服务端
        s.sendall(data)

        # 接收服务端数据
        rec_data = s.recv(1024)
        # 如果接收消息不为空，执行写入
        if rec_data:
            # 写入到clientdownload_filename文件中
            with open('./clientdownload_' + file_name, 'wb') as f:
                f.write(rec_data)
            print("Download Succeed!")
        else:
            print("Download Fail")
    s.close()


if __name__ == '__main__':
    echo_client()
