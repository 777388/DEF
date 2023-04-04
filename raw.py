from scapy.all import *

def modify_packets(packet):
    if IP in packet:
        # Extract the IP header
        ip = packet[IP]

        # Modify the source and destination IP addresses
        a = ip.src
        ip.src = ip.dst
        ip.dst = a

        # Recalculate the checksum of the IP header
        del ip.chksum
        del ip.len
        packet = bytes(ip) + bytes(packet[IP].payload)

        # Send the modified packet to the destination
        send(packet)

# Capture all raw packets and pass them to the modify_packets() function
sniff(prn=modify_packets, filter="ip")
