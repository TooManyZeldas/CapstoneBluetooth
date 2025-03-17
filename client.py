import bluetooth
import json

def client():
    bd_addr = "XX:XX:XX:XX:XX:XX"  # Server Bluetooth Address
    port = 30

    with open("data.json", "r") as f:
        json_data = json.load(f)

    json_str = json.dumps(json_data) + "<EOF>"

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))

    # Send data
    chunk_size = 1024
    for i in range(0, len(json_str), chunk_size):
        sock.send(json_str[i:i+chunk_size])

    # Receive response
    response = sock.recv(1024).decode("utf-8")
    print("Server response:", response)

    sock.close()

if __name__ == "__main__":
    client()