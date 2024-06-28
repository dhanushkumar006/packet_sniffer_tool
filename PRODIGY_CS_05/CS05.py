import socket
import struct
from os import name


# noinspection PyTypeChecker
def main() -> object:
    # Create a raw socket to capture packets
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(65536)
        _ , src_mac, eth_proto, data = ethernet_frame(raw_data)
        print("Ethernet Frame: Destination MAC: {dest_mac}, Source MAC: {src_mac}, Protocol: {eth_proto}")

def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack("! 6s 6s H", data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

def get_mac_addr(bytes_addr):
    bytes_str = map("{:02x}".format, bytes_addr)
    return ":".join(bytes_str)

if name == "main":
    main()