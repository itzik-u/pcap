import pyshark


cap = pyshark.FileCapture("C:/Users/i4190/Downloads/wshunt1.pcapng",
                          display_filter = 'http.request.method == POST')

x = 0
for packet in cap:
    x += 1
    try:
        if hasattr(packet.http,"file_data"):
            data = bytes.fromhex(packet.http.file_data.replace(":", "")).decode()
            i = 0
            for keyword in ['user','username','password','login']:
                i+=1
                if keyword in data.lower():
                    print(x,i,data,'\n')
                    break
    except:
        continue