import socket

def tcp_client():
    host = '127.0.0.1'  # 伺服器的地址，如果伺服器運行在不同的機器上，需要修改為該機器的IP地址
    port = 9999         # 伺服器的端口號，需要與伺服器端的端口號相匹配

    # 創建一個socket對象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 連接到指定的伺服器和端口
        s.connect((host, port))
        # 發送數據
        s.sendall(b'Hello, server')
        # 接收伺服器回應的數據
        data = s.recv(1024)
        print(f"Received {data.decode()} from the server")

if __name__ == '__main__':
    tcp_client()

