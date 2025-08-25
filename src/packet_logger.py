from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP
import csv
from datetime import datetime
import os

# Ensure data folder exists
os.makedirs("../data", exist_ok=True)

csv_file = "../data/packets.csv"

# Write CSV header if file does not exist
if not os.path.isfile(csv_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "src_ip", "dst_ip", "protocol", "src_port", "dst_port", "length"])

def packet_callback(packet):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
    elif IPv6 in packet:
        src_ip = packet[IPv6].src
        dst_ip = packet[IPv6].dst
        proto = packet[IPv6].nh
    else:
        src_ip = None
        dst_ip = None
        proto = None

    src_port = packet.sport if TCP in packet or UDP in packet else None
    dst_port = packet.dport if TCP in packet or UDP in packet else None
    length = len(packet)

    with open(csv_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, src_ip, dst_ip, proto, src_port, dst_port, length])

    print(f"{timestamp} | {src_ip} -> {dst_ip} | Proto: {proto} | Length: {length}")

sniff(prn=packet_callback, count=20)