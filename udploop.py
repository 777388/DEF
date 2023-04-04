import socket

# Get your IP address using the socket module
your_ip_address = socket.gethostbyname(socket.gethostname())

# Loop over a range of port numbers and create a UDP server on each one
for port in range(1, 65536):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Bind the socket to a specific IP address and port
        sock.bind(("0.0.0.0", port))
    except OSError:
        # If the port is already in use, skip it and move on to the next one
        continue

    # Loop indefinitely, waiting for incoming packets
    while True:
        # Receive a packet and extract the data and client address
        data, client_addr = sock.recvfrom(1024)

        # Extract the source IP address from the packet header
        source_ip = client_addr[0]

        # Modify the packet by replacing the source IP address with your own
        modified_packet = data.replace(source_ip.encode(), your_ip_address.encode())

        # Send the modified packet back to the client
        sock.sendto(modified_packet, client_addr)
