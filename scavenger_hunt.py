import binascii
import base64
import pyshark
import subprocess

from xarray.core.formatting import pretty_print

cap = pyshark.FileCapture("C:/Users/i4190/Downloads/wshunt1.pcapng",
                          display_filter = 'http.request.method == POST')


for packet in cap:
    try:
        if hasattr(packet.http,"file_data"):
            data = bytes.fromhex(packet.http.file_data.replace(":", "")).decode()
            for keyword in ['user','username','password','login']:
                if keyword in data.lower():
                    print(data)
    except:
        continue