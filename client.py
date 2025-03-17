import bluetooth
import json

def client():
    bd_addr = "B8:27:EB:D0:60:19" #Kyle's phone bluetooth is 6C:AC:C2:F8:61:85
    port = 30

    with open("test.json", "r") as f: #replace test.json with your json file
        json_data = json.load(f)

    json_str = json.dumps(json_data)  #convert json to string
    json_str += "<EOF>"  #append end of file marker

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))

    chunk_size = 1024
    for i in range(0, len(json_str), chunk_size):
        sock.send(json_str[i:i+chunk_size])  #send in chunks

    sock.close()

if __name__ == '__main__':
    client()
