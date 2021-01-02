import socket

HOST = 'localhost'
PORT = 30000

def server_2_client(new_client_socket, client_addr):
    """服务器发送文件函数"""
    # 获取文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("%s Need %s" % (client_addr, file_name))
    file_content = None

    # 防止没有文件或者权限造成的错误
    try:
        file = open(file_name, 'rb')  # 打开文件
        file_content = file.read()  # 读取文件
        file.close()  # 关闭文件
    # 未找到文件异常处理
    except Exception as ret:
        print("Not Found File!")

    # 若内容非空,发送文件
    if file_content:
        new_client_socket.send(file_content)
        print("OK__Send Succeed!")


def echo_server():
    ''' Echo Server 的 Server 端 '''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 对象s绑定到指定的主机和端口上
    s.bind((HOST, PORT))
    # 只接受1个连接
    s.listen(1)
    while True:
        # 接收新客户端与信息
        new_client_socket, client_addr = s.accept()
        # 输出客户端地址
        print(f'Connected by {client_addr}')
        # 调用文件发送函数
        server_2_client(new_client_socket, client_addr)
        # 关闭新客户端套接字
        new_client_socket.close()
    s.close()


if __name__ == '__main__':
    echo_server()
