from scapy.all import *

# Define a function to modify packets
def modify_packet(packet):
    # Modify the packet as needed
    packet[Raw].load += b" <a href='https://www.youtube.com/watch?v=2QF0ylMF0pA'>Click here</a>"  # Append a weblink to the end of the packet

    # Return the modified packet
    return packet

# Set up a packet capture filter to capture outgoing packets
capture_filter = "dst host not localhost and outbound"

# Set up a packet capture object to capture outgoing packets
capture = sniff(filter=capture_filter, prn=modify_packet)

# Start the packet capture
capture.run()
