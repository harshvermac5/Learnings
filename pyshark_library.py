import pyshark

# start caputring the traffic into variable
capture = pyshark.LiveCapture(interface="wlan0")
capture.sniff(timeout=10)

# printing every captured packet
for packet in capture:
    print(packet)

# applying the filter to the capture
capture = pyshark.LiveCapture(interface="eth0", display_filter="tcp.port == 80")

# printing only the required information
for packet in capture:
    print(packet.ip.src, packet.ip.dst, packet.transport_layer)

# accessing the payload data
http_packet = capture[0]
print(http_packet.http.request_uri)