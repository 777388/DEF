import base64
from scapy.all import *

# Define a function to modify and send packets
def modify_and_send_packet(packet):
    # Base64 encode the payload of the packet
    packet[Raw].load += b" <a href='https://www.youtube.com/watch?v=2QF0ylMF0pA'>Click here</a>"  # Append a weblink to the end of the packet
    payload = packet[Raw].load
    encoded_payload = base64.b64encode(payload)

    # Replace the payload with the base64 encoded payload
    packet[Raw].load = encoded_payload

    # Send the modified packet out on the network
    send(packet)

# Set up a packet capture filter to capture outgoing packets
capture_filter = "dst host not localhost and outbound"

# Set up a packet capture object to capture outgoing packets
capture = sniff(filter=capture_filter, prn=modify_and_send_packet)

# Start the packet capture
capture.run()
