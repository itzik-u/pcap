import pyshark

# Load only ICMP packets from the pcap
cap = pyshark.FileCapture('C:/Users/i4190/Downloads/wshunt1.pcapng', display_filter='icmp')

for packet in cap:
    try:
        if 'icmp' in packet:
            raw_data = packet.ICMP.data
            # Convert hex to ASCII
            ascii_data = bytes.fromhex(raw_data).decode()
            print("📦 ICMP Payload (ASCII):", ascii_data)
    except Exception as e:
        print("⚠️ Error reading packet:", e)

cap.close()
