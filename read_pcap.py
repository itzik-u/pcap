import subprocess

interface = "4"  # החלף לפי המספר שתראה מ-tshark -D
duration = "60"
output_file = "capture2.pcap"

# הפעלת tshark להקלטה
cmd = ["C:/Program Files/Wireshark/tshark.exe", "-i", interface, "-a", f"duration:{duration}", "-w", output_file]
print("Capturing network traffic...")
subprocess.run(cmd)
print(f"Capture saved to {output_file}")