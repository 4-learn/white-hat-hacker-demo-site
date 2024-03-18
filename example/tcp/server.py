import socket

def start_server(host='0.0.0.0', port=9999):
    # 創建socket對象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 設置選項，重用IP和Port
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 綁定IP地址和端口號
    server_socket.bind((host, port))
    # 監聽，並設置最大連接數
    server_socket.listen(5)
    print(f"Listening on {host}:{port} ...")

    while True:
        # 接受連接請求
        client_socket, address = server_socket.accept()
        print(f"Accepted connection from {address[0]}:{address[1]}")
        # 這裡可以進行數據接收和發送
        client_socket.close()

if __name__ == '__main__':
    start_server()
