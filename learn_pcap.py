import subprocess
import pyshark

interface = "4"  # שנה לפי מספר הממשק שלך
duration = "120"
output_file = "captured_session.pcap"

# הקלטה
cmd = [
    "C:/Program Files/Wireshark/tshark.exe",
    "-i", interface,
    "-a", f"duration:{duration}",
    "-w", output_file
]

print("Capturing traffic...")
subprocess.run(cmd)
print(f"Saved to {output_file}")

# ניתוח
cap = pyshark.FileCapture(output_file, display_filter="http.request.method == POST")

for pkt in cap:
    try:
        if hasattr(pkt.http, "file_data"):
            data = pkt.http.file_data
            if "pass" in data or "user" in data or "login" in data:
                print("===========")
                print(f"Source: {pkt.ip.src} → Destination: {pkt.ip.dst}")
                print(f"Host: {pkt.http.host}")
                print(f"Form Data: {data}")
                print()
    except:
        continue