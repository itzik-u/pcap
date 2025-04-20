import pyshark
import binascii

cap = pyshark.FileCapture("capture2.pcap",display_filter = 'http.request.method == POST')

for packet in cap:
    try:
        if hasattr(packet.http,'file_data'):
            print('file found')
            print(packet.http.file_data)
            data = binascii.unhexlify(packet.http.file_data.replace(':',"")).decode()
            print(data)
    except:
        continue


