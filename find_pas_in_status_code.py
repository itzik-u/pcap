import pyshark

# Load the pcap file
cap = pyshark.FileCapture('C:/Users/i4190/Downloads/wshunt1.pcapng', display_filter='http')

for packet in cap:
    try:
            # Look for custom status codes or messages
            if 'http' in packet and hasattr(packet.http, 'response_phrase'):
                phrase = packet.http.response_phrase
                if phrase != 'OK' or phrase != "Not Modified":
                    status_code = packet.http.response_code
                    print("HTTP Status Code:", status_code)
                    print("Phrase:", phrase)

            # Check if the status code looks suspicious (like 666, 777, 2012, etc.)
            if int(status_code) >= 600 or int(status_code) < 100:
                print("!!! Suspicious Status Code — might contain hidden data:", status_code)
    except Exception as e:
        print("Error processing packet:", e)

cap.close()
